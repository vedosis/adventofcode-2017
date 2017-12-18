import click
from collections import defaultdict
from typing import DefaultDict
from enum import Enum
from re import compile

from adventofcode_2017 import cli

lexer_regex = compile('^(?P<register>\w+)\s'
                      '(?P<operation>\w{3})\s'
                      '(?P<value>-?\d+) if '
                      '(?P<cond_register>\w+) '
                      '(?P<cond_operation>[!=><]+) '
                      '(?P<cond_value>[-\d]+)$')


@cli.command("ex8")
def exercise():
    register = defaultdict(int)
    highest_value = 0
    with open("adventofcode_2017/input/exercise-8.txt") as file:
        for line in file:
            match = lexer_regex.match(line)
            if match is None:
                click.secho("Failed to parse: `{0}`".format(line), fg='red')
            instruction = Instruction(**match.groupdict())
            process_instruction(instruction, register)
            if register[instruction.register] > highest_value:
                highest_value = register[instruction.register]

    max_value = max(register.values())
    click.echo("Maximum value: {0}".format(max_value))
    click.echo("Highest value: {0}".format(highest_value))


class Operation(Enum):
    Increment = "inc"
    Decrement = "dec"


class ConditionalEvaluation(Enum):
    GreaterThan = ">"
    GreaterThanEqualTo = ">="
    LessThan = "<"
    LessThanEqualTo = "<="
    EqualTo = "=="
    NotEqual = "!="


class Instruction(object):
    def __init__(self, register: str, operation: str, value: int, cond_register: str, cond_operation: str, cond_value: int):
        self.register = register
        self.operation = Operation(operation)
        self.value = int(value)
        self.conditional_register = cond_register
        self.conditional_operator = ConditionalEvaluation(cond_operation)
        self.conditional_value = int(cond_value)


def process_instruction(instruction: Instruction, register: DefaultDict[str, int]):
    if instruction.conditional_operator == ConditionalEvaluation.GreaterThan and \
            register[instruction.conditional_register] <= instruction.conditional_value:
        return
    if instruction.conditional_operator == ConditionalEvaluation.GreaterThanEqualTo and \
            register[instruction.conditional_register] < instruction.conditional_value:
        return
    if instruction.conditional_operator == ConditionalEvaluation.EqualTo and \
            register[instruction.conditional_register] != instruction.conditional_value:
        return
    if instruction.conditional_operator == ConditionalEvaluation.NotEqual and \
            register[instruction.conditional_register] == instruction.conditional_value:
        return
    if instruction.conditional_operator == ConditionalEvaluation.LessThanEqualTo and \
            register[instruction.conditional_register] > instruction.conditional_value:
        return
    if instruction.conditional_operator == ConditionalEvaluation.LessThan and \
            register[instruction.conditional_register] >= instruction.conditional_value:
        return

    if instruction.operation == Operation.Increment:
        register[instruction.register] += instruction.value
    if instruction.operation == Operation.Decrement:
        register[instruction.register] -= instruction.value
