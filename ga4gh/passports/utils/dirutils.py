import os
from ga4gh.passports.exception import PassportsAdminException

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
    def render_config_dir():
        config_dir = os.path.join(
            DirUtils.get_home_dir(),
            ".ga4gh",
            "passports"
        )
        return config_dir
    
    @staticmethod
    def get_config_dir():
        config_dir = DirUtils.render_config_dir()
        DirUtils.raise_nonexistent_file(config_dir)
        DirUtils.raise_unsecure_directory(config_dir)
        return config_dir
    
    @staticmethod
    def list_subfiles(parent_dir):
        return sorted(os.listdir(parent_dir))
    
    @staticmethod
    def create_secure_directory(dirpath):
        os.makedirs(dirpath)
        os.chmod(dirpath, int(DirUtils.SECURE_DIRECTORY, base=8))
    
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
