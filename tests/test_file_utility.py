import unittest
from utility import file_utilities_factory


class TestFileUtility(unittest.TestCase):
    def setUp(self):
        pass
        self.testing_rows = ("Иванов", "Ш", 105), ("Петров", "А", 106.3)

    def tearDown(self):
        pass

    def test_csv_write(self):
        self.create_and_test('CSV', 'Иванов|Ш|105\nПетров|А|106.3\n')

    def test_positional_write(self):
        self.create_and_test('POSITIONAL', 'Иванов              Ш    105\n'
                                           'Петров              А    106.3\n')

    def create_and_test(self, file_type, expected_text):
        file_utility = file_utilities_factory.create(file_type)
        filename = 'write_test' + file_type + '.txt'
        file_utility.write(filename, self.testing_rows)
        fin = open(filename)
        writen_text = "".join([line for line in fin.readlines()])
        fin.close()
        self.assertEqual(writen_text, expected_text)
