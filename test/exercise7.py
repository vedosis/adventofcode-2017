import unittest
from random import choice
from typing import Dict
from adventofcode_2017.exercise7 import Program


class TestExercise(unittest.TestCase):
    InputLines = [
        'pbga (66)',
        'xhth (57)',
        'ebii (61)',
        'havc (66)',
        'ktlj (57)',
        'fwft (72) -> ktlj, cntj, xhth',
        'qoyq (66)',
        'padx (45) -> pbga, havc, qoyq',
        'tknk (41) -> ugml, padx, fwft',
        'jptl (61)',
        'ugml (68) -> gyxo, ebii, jptl',
        'gyxo (61)',
        'cntj (57)',
    ]

    TopProgram = 'tknk'
    Unbalanced = 'ugml'
    TargetWeight = 60

    def test_balance_memory(self):
        programs = {}  # type: Dict[str, Program]
        for line in self.InputLines:
            program = Program(line)
            programs[program.name] = program
        for key, program in programs.items():
            program.resolve_children(programs)
        target = choice([value for key, value in programs.items()])
        while target.parent:
            target = target.parent
        self.assertEqual(self.TopProgram, target.name)

        unbalanced, target_weight = target.find_unbalanced_program()
        self.assertEqual(self.Unbalanced, unbalanced.name)
        self.assertEqual(self.TargetWeight, target_weight)
