import click

@click.group()
def entry():
    pass

@entry.group()
def key():
    pass

@key.command()
def view():
    pass

@key.command()
def setup():
    pass

@entry.group()
def agent():
    pass

@agent.command()
def view():
    pass

@agent.command()
def select():
    pass

@entry.command()
def start():
    pass