import unittest
from adventofcode_2017.exercise3 import calculate_steps


class TestExercise(unittest.TestCase):
    LocationData = {
        1: 0,
        12: 3,
        23: 2,
        28: 3,
        48: 5,
        49: 6,
        74: 7,
        77: 4,
        79: 6,
        1024: 31,
    }

    NeighborData = {
        1: 1,
        2: 1,
        3: 2,
        4: 4,
        5: 5,
        6: 10,
        7: 11,
        8: 23,
        9: 25,
        10: 26,
    }

    def test_calculate_steps(self):
        for key, value in self.LocationData.items():
            result = calculate_steps(key)
            self.assertEqual(value, result, "Target: {0}".format(key))
