import click

from adventofcode_2017 import cli


@cli.command("ex4")
def exercise():
    with open("adventofcode_2017/input/exercise-4.txt") as file:
        good = 0
        gooder = 0
        for line in file:
            line = line.strip('\n')

            if check_passphrase(line):
                good += 1
            if check_passphrase_v2(line):
                gooder += 1

        click.echo("Good Passphrase: {0}".format(good))
        click.echo("Gooder Passphrase: {0}".format(gooder))


def check_dupes(parts: list) -> bool:
    for part in parts:
        new_list = parts[:]
        new_list.remove(part)
        if part in new_list:
            return False
    return True


def check_passphrase(line: str) -> bool:
    parts = line.split(' ')
    return check_dupes(parts)


def check_passphrase_v2(line: str) -> bool:
    parts = [''.join(sorted(x)) for x in line.split(' ')]
    return check_dupes(parts)
