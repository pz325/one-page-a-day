# -*- coding: utf-8 -*-
# pylint: disable=C0301


'''
This module generate one page exercise
'''


import os
import random

import latex_util

import assets.spanish.year7
import assets.latin.year7


def random_vocabulary_exercise(book, sections=None):
    '''
    random vocabulary exercise, in table style
    @param book
    @param sections range of sections. None means all sections
    @return including answer pages
    '''
    # just to fit in one page
    num_exercises = 30

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
    ret['subject'] = book['subject']
    ret['template'] = book['template']

    ret['sections'] = []
    section_to_english = {}
    section_to_english['title'] = 'Translate into English'
    random_exercises = random.sample(all_exercises, num_exercises)
    section_to_english['exercises'] = [(x.decode('utf8'), r'') for x, _ in random_exercises]

    section_to_english_answer = {}
    section_to_english_answer['title'] = 'Translate into English (Answer)'
    section_to_english_answer['exercises'] = [(x.decode('utf8'), y) for x, y in random_exercises]

    section_to_subject = {}
    section_to_subject['title'] = 'Translate into {subject}'.format(subject=book['subject'])
    random_exercises = random.sample(all_exercises, num_exercises)
    section_to_subject['exercises'] = [(x, r'') for _, x in random_exercises]

    section_to_subject_answer = {}
    section_to_subject_answer['title'] = 'Translate into {subject} (Answer)'.format(subject=book['subject'])
    section_to_subject_answer['exercises'] = [(y, x.decode('utf8')) for x, y in random_exercises]

    ret['sections'].append(section_to_english)
    ret['sections'].append(section_to_subject)
    ret['sections'].append(section_to_english_answer)
    ret['sections'].append(section_to_subject_answer)

    return ret


def main():
    '''
    Generate one page exercise
    '''
    if not os.path.exists(latex_util.TARGET_PATH):
        os.mkdir(latex_util.TARGET_PATH)

    # Spanish vocablary exercise
    latex_util.generate_table(random_vocabulary_exercise(
        assets.spanish.year7.ZOOM_ESPANOL_1, [0, 1]))

    # Latin vocabulary exercise
    latex_util.generate_table(random_vocabulary_exercise(
        assets.latin.year7.ZHENGLIN_YEAR7))



if __name__ == '__main__':
    main()
