import click

from adventofcode_2017 import cli


@cli.command("ex6")
def exercise():
    with open("adventofcode_2017/input/exercise-6.txt") as file:
        data = file.read().strip('\n')

    inf_loop, cycles = balance_memory([int(x) for x in data.split('\t')])

    click.echo("Breach of Infinite Loop: {0}".format(inf_loop))
    click.echo("Length of Cycles: {0}".format(cycles))


def balance_memory(banks: list) -> (int, int):
    known_patterns = []
    idx = 0

    while True:
        string = ','.join([str(x) for x in banks])
        if string in known_patterns:
            length = len(known_patterns)
            index = known_patterns.index(string)
            return idx, length - index
        else:
            known_patterns.append(string)

        banks = balance_banks(banks[:])
        idx += 1


def balance_banks(banks: list) -> list:
    length = len(banks)
    maximum_idx = find_maximum(banks)
    maximum_value = banks[maximum_idx]
    banks[maximum_idx] = 0
    for i in range(maximum_value):
        maximum_idx += 1
        if maximum_idx >= length:
            maximum_idx = 0
        banks[maximum_idx] += 1

    return banks


def find_maximum(banks: list) -> int:
    maximum = max(banks)
    for bank, value in enumerate(banks):
        if value == maximum:
            return bank
