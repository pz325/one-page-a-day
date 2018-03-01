import csv
import os
import assets.spanish.year7
import assets.latin.year7
import assets.chinese.year1

BOOKS = [
    assets.spanish.year7.ZOOM_ESPANOL_1,
    assets.latin.year7.ZHENGLIN_YEAR7,
    assets.spanish.year7.SPELLING_BEE,
    assets.chinese.year1.YU_WEN_SHIZI,
    assets.chinese.year1.YU_WEN_XIEZI
]


TARGET_PATH = './dist'
if not os.path.exists(TARGET_PATH):
    os.mkdir(TARGET_PATH)

for book in BOOKS:
    filename = '{target_path}/{user} {title}.csv'.format(target_path=TARGET_PATH, user=book['user'], title=book['title'])
    with open(filename, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for section in book['sections']:
            for exercise in section['exercises']:
                writer.writerow(exercise)

