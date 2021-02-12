import click
import hashlib
import jsonpickle
import os
from ga4gh.passports.utils.dirutils import DirUtils
from ga4gh.passports.utils.salt_creator import SaltCreator
from ga4gh.passports.model.user import User
from ga4gh.passports.exception import PassportsAdminException

@click.group()
def user():
    pass

@click.command()
@click.argument("broker_name")
def create(broker_name):
    print("Attempting to create new user for broker: %s" % broker_name)
    users_dict = DirUtils.load_users_file(broker_name)

    # get new user's name from stdin
    name = input("Please enter user name: ")
    if name in users_dict.keys():
        raise PassportsAdminException("a user with the name %s already exists" % name)

    # get random salt string 
    print("Generating salt string for this user...")
    salt = SaltCreator.create_salt_string()

    # admin specifies the user's temporary password
    temp_password = input("Enter a temporary password for this user (NOTE: the new user must change their password within 24 hours):\n")

    # create the hashed password value from temp password and salt
    m = hashlib.sha256()
    m.update(bytearray(temp_password, 'utf-8'))
    m.update(bytearray(salt, 'utf-8'))
    hashed = m.hexdigest()

    # write the new user to the users.json file
    new_user = User(name, salt, hashed, True, "now")
    users_dict[name] = new_user
    DirUtils.write_users_file(broker_name, jsonpickle.encode(users_dict))

user.add_command(create)
