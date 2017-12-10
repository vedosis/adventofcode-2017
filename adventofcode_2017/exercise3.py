import click

from adventofcode_2017 import cli


@cli.command("ex3")
def exercise():
    with open("adventofcode_2017/input/exercise-3.txt") as file:
        data = int(file.read())

    steps = calculate_steps(data)

    click.echo("Number of Steps: {0}".format(steps))
    click.echo("https://oeis.org/A141481/b141481.txt")


def calculate_steps(target: int) -> int:
    if target <= 1:
        return 0

    idx = 1
    while True:
        x = (idx * 2) + 1
        square = int(pow(x, 2))
        if target > square:
            idx += 1
            continue

        difference = square - target
        modulo = difference % (x - 1)

        if modulo > (x / 2):
            circular_movement = modulo - int(x / 2)
        else:
            circular_movement = int(x / 2) - modulo

        movement = circular_movement + idx

        return movement

#
# def calculate_sum_spiral(target: int) -> int:
#     grid = {}
#     x = y = 0
#     dx = 0
#     dy = 1
#
#     grid[(0, 0)] = 1
#     while True:
#
