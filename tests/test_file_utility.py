import unittest
from utility import file_utility

class TestFileUtility(unittest.TestCase):

    def setUp(self):
        pass
        # valid_file = open('valid_file.txt', 'wt')
        # valid_file.write(self.valid_data)
        # valid_file.close()

    def tearDown(self):
        pass

    def test_write(self):
        rows = ("Иванов", "Ш", 105), ("Петров", "А", 106.3)
        file_utility.write('testing_write.txt', rows)
        fin = open('testing_write.txt', 'rt')
        lines = fin.readlines()
        fin.close()
        writen_text = ""
        for line in lines:
            writen_text += line
        test_text = 'Иванов|Ш|105\nПетров|А|106.3\n'
        self.assertEqual(writen_text, test_text)