import unittest
from adventofcode_2017.exercise6 import balance_memory


class TestExercise(unittest.TestCase):
    Banks = [0, 2, 7, 0]
    LoopResult = 5

    def test_balance_memory(self):
        result = balance_memory(self.Banks)
        self.assertEqual(self.LoopResult, result, "Balance Memory")
