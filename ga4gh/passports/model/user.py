from ga4gh.passports.model.serializable import Serializable

class User(Serializable):

    def __init__(self, name, salt, hashed, pwd_is_temp, created):
        super().__init__()
        self.name = name
        self.salt = salt
        self.hashed = hashed
        self.pwd_is_temp = pwd_is_temp
        self.created = created
