import click
from ga4gh.passports.cli.init import init
from ga4gh.passports.cli.broker import broker
from ga4gh.passports.cli.user import user

@click.group()
def main():
    pass

main.add_command(init)
main.add_command(broker)
main.add_command(user)