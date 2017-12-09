import click
import os

from adventofcode_2017 import cli


@cli.command("ex1")
def exercise1():
    click.echo(os.getcwd())
    with open("adventofcode_2017/input/exercise-1.txt") as file:
        data = file.read()
        result = count_neighbors(data)
        result2 = count_opposite(data)

    click.echo("Captcha Result: {0}".format(result))
    click.echo("Captcha Result 2: {0}".format(result2))


def count_neighbors(value: str) -> int:
    total = 0
    for idx, rune in enumerate(value):
        if idx + 1 >= len(value):
            compare = value[0]
        else:
            compare = value[idx + 1]

        if rune == compare:
            total += int(rune)

    return total


def comparator(idx: int, value: str) -> int:
    middle = int((len(value) - 1) / 2)
    if idx > middle:
        compare = value[idx - int(len(value) / 2)]
    else:
        compare = value[idx + int(len(value) / 2)]

    return int(compare)


def count_opposite(value: str) -> int:
    total = 0
    for idx, rune in enumerate(value):
        compare = comparator(idx, value)
        if compare == int(rune):
            total += compare

    return total
