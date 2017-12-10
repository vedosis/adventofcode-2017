import unittest
from adventofcode_2017.exercise5 import traverse_maze


class TestExercise(unittest.TestCase):
    MazeData = [0, 3, 0, 1, -3]
    MazeStepsV1 = 5
    MazeStepsV2 = 10

    def test_traverse_maze(self):
        result = traverse_maze(self.MazeData[:])
        self.assertEqual(self.MazeStepsV1, result, "Maze Steps V1")

    def test_traverse_maze_v2(self):
        result = traverse_maze(self.MazeData[:], True)
        self.assertEqual(self.MazeStepsV2, result, "Maze Steps V2")
