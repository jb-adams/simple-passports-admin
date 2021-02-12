import jsonpickle
import os
from ga4gh.passports.exception import PassportsAdminException
from ga4gh.passports.model.user import User

class DirUtils(object):

    SECURE_DIRECTORY = '700'
    SECURE_FILE = '600'

    @staticmethod
    def get_home_dir():
        home_dir = os.getenv("HOME")
        if not home_dir:
            raise PassportsAdminException("home directory not detected, set HOME environment variable")
        return home_dir
    
    @staticmethod
    def render_brokers_dirpath():
        brokers_dir = os.path.join(
            DirUtils.get_home_dir(),
            ".ga4gh",
            ".simple-passport-broker",
            "brokers"
        )
        return brokers_dir
    
    @staticmethod
    def get_brokers_dir():
        config_dir = DirUtils.render_brokers_dirpath()
        DirUtils.raise_nonexistent_file(config_dir)
        DirUtils.raise_unsecure_directory(config_dir)
        return config_dir
    
    @staticmethod
    def render_single_broker_dirpath(broker_name):
        single_broker_dir = os.path.join(
            DirUtils.get_brokers_dir(),
            broker_name
        )
        return single_broker_dir
    
    @staticmethod
    def get_single_broker_dir(broker_name):
        single_broker_dir = DirUtils.render_single_broker_dirpath(broker_name)
        DirUtils.raise_nonexistent_file(single_broker_dir)
        DirUtils.raise_unsecure_directory(single_broker_dir)
        return single_broker_dir
    
    @staticmethod
    def render_users_filepath(broker_name):
        users_filepath = os.path.join(
            DirUtils.get_single_broker_dir(broker_name),
            "users.json"
        )
        return users_filepath
    
    @staticmethod
    def get_users_file(broker_name):
        users_filepath = DirUtils.render_users_filepath(broker_name)
        DirUtils.raise_nonexistent_file(users_filepath)
        DirUtils.raise_unsecure_file(users_filepath)
        return users_filepath
    
    @staticmethod
    def load_users_file(broker_name):
        users_filepath = DirUtils.get_users_file(broker_name)
        users_file = open(users_filepath, "r")
        users_dict = users_file.read()
        users_file.close()
        return jsonpickle.decode(users_dict)
    
    @staticmethod
    def write_users_file(broker_name, content):
        users_filepath = DirUtils.get_users_file(broker_name)
        users_file = open(users_filepath, "w")
        users_file.write(content)
        users_file.close()
    
    @staticmethod
    def list_subfiles(parent_dir):
        return sorted(os.listdir(parent_dir))
    
    @staticmethod
    def create_secure_directory(dirpath):
        os.makedirs(dirpath)
        os.chmod(dirpath, int(DirUtils.SECURE_DIRECTORY, base=8))
    
    @staticmethod
    def write_secure_file(filepath, content):
        output_file = open(filepath, "w")
        output_file.write(content)
        os.chmod(filepath, int(DirUtils.SECURE_FILE, base=8))
    
    @staticmethod
    def raise_nonexistent_file(filepath):
        if not os.path.exists(filepath):
            raise PassportsAdminException("file/dir %s does not exist" % filepath)
    
    @staticmethod
    def raise_unsecure_directory(dirpath):
        st_mode = os.stat(dirpath).st_mode
        permission = oct(st_mode & 0o777)[-3:]
        if permission != DirUtils.SECURE_DIRECTORY:
            raise PassportsAdminException(
                "%s is not secure, expected a permission of %s, found %s" % (
                    dirpath,
                    DirUtils.SECURE_DIRECTORY, 
                    permission
                )
            )
    
    @staticmethod
    def raise_unsecure_file(filepath):
        st_mode = os.stat(filepath).st_mode
        permission = oct(st_mode & 0o777)[-3:]
        if permission != DirUtils.SECURE_FILE:
            raise PassportsAdminException(
                "%s is not secure, expected a permission of %s, found %s" % (
                    filepath,
                    DirUtils.SECURE_FILE, 
                    permission
                )
            )
