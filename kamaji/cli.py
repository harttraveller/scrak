import click

@click.group()
def entry():
    pass

@entry.command()
def key():
    pass

@entry.command()
def start():
    pass