import csv


def read(path):
    """
    :param path:
    :return list of (string, string, float)
    """
    with open(path, 'rt') as fin:
        cin = csv.reader(fin, delimiter='|')
        rows = [row for row in cin]
        for row in rows:
            if len(row) != 3:
                return None
        return rows


def write(path, rows):
    """
    :param path:
    :param rows: list of (string, string, float)
    :return: None
    """
    with open(path, 'wt') as fout:
        csvout = csv.writer(fout, delimiter='|')
        csvout.writerows(rows)
