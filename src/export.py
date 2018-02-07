import csv
import assets.latin.year7
import assets.spanish.year7

BOOKS = [
    assets.spanish.year7.ZOOM_ESPANOL_1,
    assets.latin.year7.ZHENGLIN_YEAR7
]

for book in BOOKS:
    filename = '{user} {title}.csv'.format(user=book['user'], title=book['title'])
    with open(filename, 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for section in book['sections']:
            for exercise in section['exercises']:
                writer.writerow(exercise)

