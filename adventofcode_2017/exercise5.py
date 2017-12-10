import click

from adventofcode_2017 import cli


@cli.command("ex5")
def exercise():
    maze = []
    with open("adventofcode_2017/input/exercise-5.txt") as file:
        for line in file:
            maze.append(int(line.strip('\n')))

    steps = traverse_maze(maze[:])
    steps_v2 = traverse_maze(maze[:], True)

    click.echo("Steps to traverse maze: {0}".format(steps))
    click.echo("Steps to traverse maze v2: {0}".format(steps_v2))


def traverse_maze(maze: list, new_offset: bool = False) -> int:
    step_total = 1
    current_step = 0
    while True:
        next_step = maze[current_step] + current_step
        if next_step > len(maze) - 1:
            return step_total

        if new_offset and maze[current_step] >= 3:
            maze[current_step] -= 1
        else:
            maze[current_step] += 1

        current_step = next_step
        step_total += 1