import click


@click.command()
@click.argument('f', type=click.Path(exists=True))
def touch(f):
    click.echo(click.format_filename(f))
    


# @click.group()
# def greet():
#     pass


# @greet.command()
# @click.argument('name') # add argument
# def hello(**kwargs):
#     print('Hello, {0}!'.format(kwargs['name']))
    
    
# @click.command()
# @click.argument('input', type=click.File('rb'))
# @click.argument('output', type=click.File('wb'))
# def inout(input, output):
#     while True:
#         chunk = input.read(1024)
#         if not chunk:
#             break
#         output.write(chunk)