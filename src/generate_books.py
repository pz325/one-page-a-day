# -*- coding: utf-8 -*-
# pylint: disable=C0301


'''
This module generate books
'''

import os

from pylatex import Document, Section, Itemize, Command, Enumerate
from pylatex.utils import NoEscape
import assets.shanghai_maths_project.year6
import assets.spanish.year6


BOOKS = [
    assets.shanghai_maths_project.year6.ZHENGLIN_YEAR6,
    assets.spanish.year6.ZHENGLIN_YEAR6
]

TARGET_PATH = 'dist'


def generage_books():
    '''
    Generate books
    '''

    if not os.path.exists(TARGET_PATH):
        os.mkdir(TARGET_PATH)

    for book in BOOKS:
        doc = Document()
        doc.preamble.append(Command('title', NoEscape(book['title'])))
        doc.preamble.append(Command('author', book['user']))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.append(NoEscape(r'\maketitle'))

        for section in book['sections']:
            with doc.create(Section(section['title'], numbering=False)):
                with doc.create(Enumerate()) as items:
                    for exercise in section['exercies']:
                        if isinstance(exercise, basestring):
                            items.add_item(NoEscape(exercise))
                        else:
                            items.add_item(NoEscape(exercise['description']))
                            with items.create(Itemize()) as sub_items:
                                for sub_exercise in exercise['exercises']:
                                    sub_items.add_item(NoEscape(sub_exercise))

        book_name = '{target_path}/{user} {title}'.format(target_path=TARGET_PATH, user=book['user'], title=book['title'])
        doc.generate_pdf(book_name, clean_tex=True)


if __name__ == '__main__':
    generage_books()
