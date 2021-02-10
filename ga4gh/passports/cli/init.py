import click
import os
from ga4gh.passports.utils.dirutils import DirUtils

@click.command()
def init():
    config_dir = DirUtils.render_config_dir()
    if os.path.exists(config_dir):
        print("config dir %s already exists" % config_dir)
    else:
        DirUtils.create_secure_directory(config_dir)
