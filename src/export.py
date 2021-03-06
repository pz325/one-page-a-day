import csv
import os
import assets.spanish.year7
import assets.latin.year7
import assets.chinese.year1
import assets.latin.year8
import assets.spanish.year8

BOOKS = [
    # assets.spanish.year7.ZOOM_ESPANOL_1,
    assets.latin.year7.XINRONG_LATIN_1,
    assets.latin.year7.XINONG_OAK,
    # assets.spanish.year7.SPELLING_BEE,
    # assets.latin.year8.ZHENGLIN_YEAR8,
    # assets.spanish.year7.TUTOR,
    # assets.chinese.year1.YU_WEN_SHIZI,
    # assets.chinese.year1.YU_WEN_XIEZI,
    # assets.spanish.year8.TUTOR,
    # assets.spanish.year8.ISEB_SPANISH_VOCABULARY
]


TARGET_PATH = './dist'
if not os.path.exists(TARGET_PATH):
    os.mkdir(TARGET_PATH)

for book in BOOKS:
    filename = '{target_path}/{user} {title}.csv'.format(
        target_path=TARGET_PATH, user=book['user'], title=book['title'])
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for section in book['sections']:
            for exercise in section['exercises']:
                writer.writerow(exercise)
