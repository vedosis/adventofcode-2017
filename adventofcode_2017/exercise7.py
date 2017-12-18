import click
from random import choice
from typing import List, Dict
from re import compile

from adventofcode_2017 import cli

line_parse = compile("^(?P<name>\w+)\s\((?P<weight>\d+)\)(\s->\s(?P<children>[\w,\s]+))?$")


@cli.command("ex7")
def exercise():
    programs = {}
    with open("adventofcode_2017/input/exercise-7.txt") as file:
        for line in file:
            program = Program(line.strip())
            programs[program.name] = program
    for name, program in programs.items():
        program.resolve_children(programs)

    target = choice([value for key, value in programs.items()])  # type: Program
    while target.parent:
        target = target.parent
    click.echo("Parent Program: {0}".format(target.name))
    unbalanced, target_weight = target.find_unbalanced_program()
    click.echo("Unbalanced Program: {0}\nCurrent Weight: {1}\nTarget Weight: {2}".format(
        unbalanced.name,
        unbalanced.weight,
        target_weight
    ))


class Program(object):
    def __init__(self, string: str):
        matches = line_parse.match(string)
        self.weight = int(matches.group('weight'))
        self.total_weight = None  # type: int
        self.name = matches.group('name')
        self.children = matches.group('children')  # type: List[Program]
        self.parent = None  # type: Program

    def resolve_children(self, programs: Dict[str, 'Program']):
        if isinstance(self.children, str):
            children = self.children.split(", ")
            children_objects = []
            for child in children:
                children_objects.append(programs[child])
                programs[child].parent = self
            self.children = children_objects

    def render_weight(self):
        if self.total_weight:
            return self.total_weight

        weight = self.weight
        if self.children:
            for child in self.children:
                child.render_weight()
                weight += child.total_weight
        self.total_weight = weight

    def find_unbalanced_program(self) -> ('Program', int):
        values = {}
        for child in self.children:
            child.render_weight()
            if child.total_weight not in values.keys():
                values[child.total_weight] = []
            values[child.total_weight].append(child)
        if len(values.keys()) == 1:
            return None, 0

        target_weight = 0
        actual_weight = 0
        for key, value in values.items():
            if len(value) == 1:
                actual_weight = key
            else:
                target_weight = key
        unbalanced_node = values[actual_weight][0]

        imbalanced_subnode, target_sub_weight = unbalanced_node.find_unbalanced_program()
        if imbalanced_subnode is None:
            return unbalanced_node, unbalanced_node.weight - (actual_weight - target_weight)
        else:
            return imbalanced_subnode, target_sub_weight
