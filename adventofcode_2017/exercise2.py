import click
from adventofcode_2017 import cli


@cli.command("ex2")
def exercise():
    with open("adventofcode_2017/input/exercise-2.txt") as file:
        checksum_1 = 0
        checksum_2 = 0

        for line in file:
            checksum_1 += calculate_line_checksum(line)
            checksum_2 += calculate_divisor_checksum(line)

    click.echo("Checksum A: {0}".format(checksum_1))
    click.echo("Checksum B: {0}".format(checksum_2))


def calculate_line_checksum(line: str) -> int:
    parts = [int(x) for x in line.split('\t')]
    return max(parts) - min(parts)


def calculate_divisor_checksum(line: str) -> int:
    parts = [int(x) for x in line.split('\t')]
    parts.sort()

    for part in parts:
        for divisor in parts:
            if part == divisor:
                continue
            if divisor % part == 0:
                return int(divisor / part)

    return 0
