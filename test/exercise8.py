import unittest
from collections import defaultdict
from adventofcode_2017.exercise8 import lexer_regex, Instruction, process_instruction


class TestExercise(unittest.TestCase):
    BufferInput = [
        "b inc 5 if a > 1",
        "a inc 1 if b < 5",
        "c dec -10 if a >= 1",
        "c inc -20 if c == 10",
    ]
    ResultingRegister = {
        "a": 1,
        "b": 0,
        "c": -10
    }
    HighestValue = 10

    def test_register_ops(self):
        register = defaultdict(int)
        highest_value = 0

        for buffer in self.BufferInput:
            match = lexer_regex.match(buffer)
            self.assertNotEqual(match, None)
            instruction = Instruction(**match.groupdict())
            process_instruction(instruction, register)

            if register[instruction.register] > highest_value:
                highest_value = register[instruction.register]

        for key, value in self.ResultingRegister.items():
            self.assertEqual(value, register[key])

        self.assertEqual(self.HighestValue, highest_value)

        self.assertEqual(len(self.ResultingRegister.keys()), len(register.keys()))
