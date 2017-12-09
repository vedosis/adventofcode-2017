import click


@click.group()
def cli():
    pass


from adventofcode_2017 import exercise1, exercise2
