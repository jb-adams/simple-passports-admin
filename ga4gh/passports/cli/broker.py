import click
import os
from ga4gh.passports.utils.dirutils import DirUtils

@click.group()
def broker():
    pass

@click.command()
def ls():
    brokers = DirUtils.list_subfiles(DirUtils.get_brokers_dir())
    if len(brokers) == 0:
        print("no brokers found")
    else:
        print("\n".join(brokers))

@click.command()
@click.argument('broker_name')
def create(broker_name):
    single_broker_dir = DirUtils.render_single_broker_dirpath(broker_name)
    if os.path.exists(single_broker_dir):
        print("cannot create broker directory, %s already exists" % broker_name)
    else:
        DirUtils.create_secure_directory(single_broker_dir)
        DirUtils.write_secure_file(DirUtils.render_users_filepath(broker_name), "{}")

broker.add_command(ls)
broker.add_command(create)
