# -*- coding: utf-8 -*-
# pylint: disable=C0301


'''
This module generate one page exercise
'''


import os
import random

from pylatex import Document, Section, Command, LongTabu
from pylatex.base_classes import Environment

from pylatex.utils import NoEscape
import assets.shanghai_maths_project.year6
import assets.spanish.year6

BOOKS = [
    assets.shanghai_maths_project.year6.ZHENGLIN_YEAR6,
    assets.spanish.year6.ZHENGLIN_YEAR6
]

TARGET_PATH = 'dist'

def generate_table(book):
    '''
    this is used to generate in table style.
    suitable for language learning: e.g. Spanish / English etc
    '''
    print 'generating book: {title}'.format(title=book['title'])
    doc = Document()
    doc.preamble.append(Command('title', NoEscape(book['title'])))
    doc.preamble.append(Command('author', book['user']))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    # doc.append(NoEscape(r'\maketitle'))

    TABLE_FORMAT = "X[l] X[r]"
    for section in book['sections']:
        with doc.create(Section(section['title'], numbering=False)):
            with doc.create(LongTabu(TABLE_FORMAT, row_height=2.0)) as table:
                table.end_table_header()
                for exercise in section['exercises']:
                    table.add_row([NoEscape(exercise[0]), NoEscape(exercise[1])])
                    table.add_hline()

    book_name = '{target_path}/{user} {title}'.format(
        target_path=TARGET_PATH, user=book['user'], title=book['title'])
    doc.generate_pdf(book_name, clean_tex=True)


def random_table_exercise(book):
    '''
    random table style exercise
    '''
    num_exercises = 9
    exercises = []
    for section in book['sections']:
        for exercise in section['exercises']:
            exercises.append(exercise)

    ret = {}
    ret['title'] = book['title'] + ' one page exercise'
    ret['user'] = book['user']
    ret['template'] = book['template']
    ret['sections'] = []
    section1 = {}
    section1['title'] = 'Translate'
    section1['exercises'] = [(x, r'') for x, _ in random.sample(exercises, num_exercises)]
    section2 = {}
    section2['title'] = 'Translate'
    section2['exercises'] = [(r'', x) for _, x in random.sample(exercises, num_exercises)]
    ret['sections'].append(section1)
    ret['sections'].append(section2)

    return ret


def generate_exercise():
    '''
    Generate one page exercise
    '''
    if not os.path.exists(TARGET_PATH):
        os.mkdir(TARGET_PATH)

    for book in BOOKS:
        if book['template'] == 'table':
            generate_table(random_table_exercise(book))


if __name__ == '__main__':
    generate_exercise()
