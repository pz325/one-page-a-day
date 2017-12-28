# -*- coding: utf-8 -*-
# pylint: disable=C0301


'''
This module generate one page exercise
'''


import os
import random

from pylatex import Document, Section, Command, LongTabu

from pylatex.utils import NoEscape
import assets.shanghai_maths_project.year6
import assets.spanish.year7

BOOKS = [
    # assets.shanghai_maths_project.year6.ZHENGLIN_YEAR6,
    assets.spanish.year7.ZOOM_ESPANOL_1,
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
                    # table.add_hline()

    book_name = '{target_path}/{user} {title}'.format(
        target_path=TARGET_PATH, user=book['user'], title=book['title'])
    doc.generate_pdf(book_name, clean_tex=True)

def random_spanish_exercise(book, sections=None):
    '''
    random spanish exercise, in table style
    @param book
    @param sections range of sections. None means all sections
    @return 

    one-page exercies has two section: translate into English / translate into Spanish
    also generate one-page, with answers to the two sections
    '''
    num_exercises = 9

    # collect all exercises
    all_exercises = []
    if sections:
        for section_index in sections:
            if section_index < 0 or section_index >= len(book['sections']):
                continue
            for exercise in book['sections'][section_index]['exercises']:
                all_exercises.append(exercise)
    else:
        for section in book['sections']:
            for exercise in section['exercises']:
                all_exercises.append(exercise)

    ret = {}
    ret['title'] = book['title'] + ' one page exercise'
    ret['user'] = book['user']
    ret['template'] = book['template']
    ret['sections'] = []

    section_to_english = {}
    section_to_english['title'] = 'Translate into English'
    random_exercises = random.sample(all_exercises, num_exercises)
    section_to_english['exercises'] = [(x, r'') for x, _ in random_exercises]

    section_to_english_answer = {}
    section_to_english_answer['title'] = 'Translate into English (Answer)'
    section_to_english_answer['exercises'] = random_exercises

    section_to_spanish = {}
    section_to_spanish['title'] = 'Translate into Spanish'
    random_exercises = random.sample(all_exercises, num_exercises)
    section_to_spanish['exercises'] = [(x, r'') for _, x in random_exercises]

    section_to_spanish_answer = {}
    section_to_spanish_answer['title'] = 'Translate into Spanish (Answer)'
    section_to_spanish_answer['exercises'] = [(y, x) for x, y in random_exercises]

    ret['sections'].append(section_to_english)
    ret['sections'].append(section_to_spanish)
    ret['sections'].append(section_to_english_answer)
    ret['sections'].append(section_to_spanish_answer)

    return ret


def main():
    '''
    Generate one page exercise
    '''
    if not os.path.exists(TARGET_PATH):
        os.mkdir(TARGET_PATH)

    for book in BOOKS:
        if book['template'] == 'table' and book['subject'] == 'spanish':
            generate_table(random_spanish_exercise(book, [0]))


if __name__ == '__main__':
    main()
