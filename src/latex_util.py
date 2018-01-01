# -*- coding: utf-8 -*-
# pylint: disable=C0301

from pylatex import Document, Section, Command, LongTabu, Package
from pylatex.base_classes import Environment
from pylatex.utils import NoEscape

TARGET_PATH = 'dist'
_TABLE_FORMAT = "X[l] X[r]"


class Parts(Environment):
    r'''
    Template for parts block used with \question
    \begig{parts}
        \part part 1
        \part part 2
    \end{parts}
    '''
    omit_if_empty = True

    def add_part(self, part):
        r'''
        append a \part item
        '''
        self.append(Command('part'))
        self.append(part)


class Questions(Environment):
    r'''
    Template for questions block used with exam documentclass
    \begin{questions}
        \question A question
        \question Another question
    \end{questions}
    '''
    omit_if_empty = True

    def add_question(self, question):
        r'''
        append a \question item
        '''
        self.append(Command('question'))
        self.append(question)


def _setup_doc(doc, book):
    doc.packages.append(Package('ctex'))
    doc.preamble.append(Command('title', NoEscape(book['title'])))
    doc.preamble.append(Command('author', book['user']))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    return doc


def generate_exam(book):
    '''
    this is used to generate in exam style.
    Suitable for Math
    '''
    print 'generating book: {title}'.format(title=book['title'])
    doc = Document(documentclass='exam')
    doc = _setup_doc(doc, book)

    for section in book['sections']:
        with doc.create(Section(section['title'], numbering=False)):
            with doc.create(Questions()) as questions:
                for exercise in section['exercises']:
                    if isinstance(exercise, basestring):
                        questions.add_question(NoEscape(exercise))
                    else:
                        questions.add_question(
                            NoEscape(exercise['description']))
                        with questions.create(Parts()) as parts:
                            for sub_exercise in exercise['exercises']:
                                parts.add_part(NoEscape(sub_exercise))

    book_name = '{target_path}/{user} {title}'.format(
        target_path=TARGET_PATH, user=book['user'], title=book['title'])
    # import pdb; pdb.set_trace()
    doc.generate_pdf(book_name, clean_tex=False, compiler='xelatex')


def generate_table(book):
    '''
    this is used to generate in table style.
    suitable for language learning: e.g. Spanish / English etc
    '''
    print 'generating book: {title}'.format(title=book['title'])
    doc = Document()
    doc = _setup_doc(doc, book)
    # doc.append(NoEscape(r'\maketitle'))

    for section in book['sections']:
        with doc.create(Section(section['title'], numbering=False)):
            with doc.create(LongTabu(_TABLE_FORMAT, row_height=2.0)) as table:
                table.end_table_header()
                for exercise in section['exercises']:
                    table.add_row(
                        [NoEscape(exercise[0]), NoEscape(exercise[1])])
                    # table.add_hline()

    book_name = '{target_path}/{user} {title}'.format(
        target_path=TARGET_PATH, user=book['user'], title=book['title'])
    doc.generate_pdf(book_name, clean_tex=True, compiler='xelatex')


def generate_textbook(book):
    '''
    this is used to generate textbook
    '''
    pass
