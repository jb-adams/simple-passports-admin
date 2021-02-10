import click
import os
from ga4gh.passports.utils.dirutils import DirUtils

@click.group()
def pool():
    pass

@click.command()
def ls():
    pools = DirUtils.list_subfiles(DirUtils.get_config_dir())
    if len(pools) == 0:
        print("no pools found")
    else:
        print("\n".join(pools))

@click.command()
@click.argument('poolname')
def create(poolname):
    existing_poolnames = DirUtils.list_subfiles(DirUtils.get_config_dir())
    if poolname in set(existing_poolnames):
        print("cannot create pool, %s already exists" % poolname)
    else:
        pool_dir = os.path.join(DirUtils.get_config_dir(), poolname)
        DirUtils.create_secure_directory(pool_dir)

pool.add_command(ls)
pool.add_command(create)
