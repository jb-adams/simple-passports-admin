import click
import os
from ga4gh.passports.utils.dirutils import DirUtils

@click.command()
def init():
    brokers_dir = DirUtils.render_brokers_dir()
    if os.path.exists(brokers_dir):
        print("config dir %s already exists" % brokers_dir)
    else:
        DirUtils.create_secure_directory(brokers_dir)
