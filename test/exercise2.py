import unittest
from adventofcode_2017.exercise2 import calculate_line_checksum, calculate_divisor_checksum


class TestExercise(unittest.TestCase):
    ChecksumDataA = {
        "5\t1\t9\t5": 8,
        "7\t5\t3": 4,
        "2\t4\t6\t8": 6
    }

    ChecksumDataB = {
        "5\t9\t2\t8": 4,
        "9\t4\t7\t3": 3,
        "3\t8\t6\t5": 2,
    }

    def test_calculate_line_checksum(self):
        for key, value in self.ChecksumDataA.items():
            result = calculate_line_checksum(key)
            self.assertEqual(value, result)

    def test_calculate_divisor_checksum(self):
        for key, value in self.ChecksumDataB.items():
            result = calculate_divisor_checksum(key)
            self.assertEqual(value, result)
