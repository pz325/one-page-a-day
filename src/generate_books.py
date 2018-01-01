# -*- coding: utf-8 -*-
# pylint: disable=C0301


'''
This module generate books
'''

import os
import sys

import latex_util
import assets.shanghai_maths_project.year6
import assets.spanish.year7


reload(sys)
sys.setdefaultencoding('utf8')


BOOKS = [
    assets.shanghai_maths_project.year6.ZHENGLIN_YEAR6,
    assets.spanish.year7.ZHENGLIN_YEAR7,
    assets.spanish.year7.ZOOM_ESPANOL_1,
    # assets.chinese.year2.YU_WEN_SHANG,
]


def generage_books():
    '''
    Generate books
    '''

    if not os.path.exists(latex_util.TARGET_PATH):
        os.mkdir(latex_util.TARGET_PATH)

    generators = {}
    generators['exam'] = latex_util.generate_exam
    generators['table'] = latex_util.generate_table
    generators['textbook'] = latex_util.generate_textbook

    for book in BOOKS:
        template = book['template']
        if template in generators:
            generators[template](book)
        else:
            print 'Unknown template: {template}'.format(template=template)


if __name__ == '__main__':
    generage_books()
