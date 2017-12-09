import unittest
from adventofcode_2017.exercise1 import count_neighbors, count_opposite, comparator


class TestExercise(unittest.TestCase):
    DataP1 = {
        "1122": 3,
        "1111": 4,
        "1234": 0,
        "91212129": 9,
    }

    ComparatorInput = "123456"
    ComparatorValues = {
        0: 4,
        1: 5,
        2: 6,
        3: 1,
        4: 2,
        5: 3
    }

    DataP2 = {
        "1212": 6,
        "1221": 0,
        "123425": 4,
        "123123": 12,
        "12131415": 4,
    }

    def test_count_duplicates(self):
        for key, value in self.DataP1.items():
            result = count_neighbors(key)
            self.assertEqual(value, result)

    def test_comparator(self):
        for key, value in self.ComparatorValues.items():
            result = comparator(key, self.ComparatorInput)
            self.assertEqual(value, result)

    def test_count_opposite(self):
        for key, value in self.DataP2.items():
            result = count_opposite(key)
            self.assertEqual(value, result)
