# -*- coding: utf-8 -*-
# pylint: disable=C0301


'''
This module generate one page exercise
'''


import os
import random

import latex_util

import assets.shanghai_maths_project.year6
import assets.spanish.year7

BOOKS = [
    # assets.shanghai_maths_project.year6.ZHENGLIN_YEAR6,
    assets.spanish.year7.ZOOM_ESPANOL_1,
]

TARGET_PATH = 'dist'
_TABLE_FORMAT = "X[l] X[r]"


def random_spanish_exercise(book, sections=None):
    '''
    random spanish exercise, in table style
    @param book
    @param sections range of sections. None means all sections
    @return

    one-page exercies has two section: translate into English / translate into Spanish
    also generate one-page, with answers to the two sections
    '''
    num_exercises = 7

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
    section_to_english['exercises'] = [(x.decode('utf8'), r'') for x, _ in random_exercises]

    section_to_english_answer = {}
    section_to_english_answer['title'] = 'Translate into English (Answer)'
    section_to_english_answer['exercises'] = [(x.decode('utf8'), y) for x, y in random_exercises]

    section_to_spanish = {}
    section_to_spanish['title'] = 'Translate into Spanish'
    random_exercises = random.sample(all_exercises, num_exercises)
    section_to_spanish['exercises'] = [(x, r'') for _, x in random_exercises]

    section_to_spanish_answer = {}
    section_to_spanish_answer['title'] = 'Translate into Spanish (Answer)'
    section_to_spanish_answer['exercises'] = [(y, x.decode('utf8')) for x, y in random_exercises]

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
            latex_util.generate_table(random_spanish_exercise(book, [0]))


if __name__ == '__main__':
    main()
