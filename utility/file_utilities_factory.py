from enum import Enum
import csv


def create(file_type):
    if file_type == 'POSITIONAL':
        return PositionalFileUtility()
    return CsvFileUtility()

class CsvFileUtility:
    def read(self, path):
        """
        :param path:
        :return list of (string, string, string)
        """
        with open(path, 'rt') as fin:
            cin = csv.reader(fin, delimiter='|')
            rows = [row for row in cin]
            if self.rows_format_is_valid(rows):
                return rows

    def write(self, path, rows):
        """
        :param path:
        :param rows: list of (string, string, float)
        :return: None
        """
        with open(path, 'wt') as fout:
            csvout = csv.writer(fout, delimiter='|')
            csvout.writerows(rows)

class PositionalFileUtility:
    positional_format = [19, 24, 30]

    def read(self, path):
        """
        :param path:
        :return list of (string, string, float)
        """
        with open(path, 'rt') as fin:
            rows = [(row[0:19], row[20:24], row[25:30].replace('\n', '')) for row in fin.readlines()]
            return rows

    def write(self, path, rows):
        """
        :param path:
        :param rows: list of (string, string, float)
        :return None
        """
        text = ''
        for row in rows:
            text += row[0] + self.create_spaces(20 - len(row[0])) \
                    + row[1] + self.create_spaces(5 - len(row[1])) \
                    + str(row[2]) + '\n'

        with open(path, 'wt') as fout:
            fout.write(text)

    def create_spaces(self, count):
        return ''.join([' ' for i in range(count)])