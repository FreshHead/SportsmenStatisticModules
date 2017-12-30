import csv


def read(path):
    with open(path, 'rt') as fin:
        cin = csv.reader(fin, delimiter='|')
        return [row for row in cin]


def write(path, rows):
    with open(path, 'wt') as fout:
        csvout = csv.writer(fout, delimiter='|')
        csvout.writerows(rows)
