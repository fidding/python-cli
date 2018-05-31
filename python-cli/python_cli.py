import click


@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    click.echo('Hello World!' + name)


if __name__ == '__main__':
    hello()
