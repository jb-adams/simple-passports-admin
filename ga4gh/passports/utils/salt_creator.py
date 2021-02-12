import random

class SaltCreator(object):

    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @staticmethod
    def create_salt_string():
        return "".join([random.choice(SaltCreator.ALPHABET) for i in range(0, 32)])
