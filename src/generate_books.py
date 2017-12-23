# -*- coding: utf-8 -*-
'''
This module generate books
'''

from pylatex import Document, Section, Itemize, Command
from pylatex.utils import NoEscape
import assets.shanghai_maths_project.year6

BOOKS = [
    assets.shanghai_maths_project.year6.ZHENGLIN_YEAR6
]


def generage_books():
    '''
    Generate books
    '''
    for book in BOOKS:
        doc = Document()
        doc.preamble.append(Command('title', book['title']))
        doc.preamble.append(Command('author', book['user']))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.append(NoEscape(r'\maketitle'))

        for section in book['sections']:
            with doc.create(Section(section['title'], numbering=False)):
                with doc.create(Itemize()) as items:
                    for exercise in section['exercies']:
                        if isinstance(exercise, basestring):
                            items.add_item(NoEscape(exercise))
                        else:
                            items.add_item(NoEscape(exercise['description']))
                            with items.create(Itemize()) as sub_items:
                                for sub_exercise in exercise['exercises']:
                                    sub_items.add_item(NoEscape(sub_exercise))

        book_name = '{user} {title}'.format(user=book['user'], title=book['title'])
        doc.generate_pdf(book_name, clean_tex=False)


if __name__ == '__main__':
    generage_books()
