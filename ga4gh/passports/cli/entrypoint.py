import click
from ga4gh.passports.cli.init import init
from ga4gh.passports.cli.pool import pool

@click.group()
def main():
    pass

main.add_command(init)
main.add_command(pool)