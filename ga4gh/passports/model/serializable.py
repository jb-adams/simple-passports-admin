class Serializable(object):

    @staticmethod
    def from_json(json_dict):
        return Serializable(**json_dict)
    
    @staticmethod
    def to_json():
        print("serializing to json")

    def __init__(self):
        pass
