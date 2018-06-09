import json

class Factory:
    def __init__(self):
        pass
    
    @staticmethod
    def create(self):
        pass

    @staticmethod
    def get_template(self):
        pass
    
    def get_config(self):
        with open('json/config.json', 'r') as file:
            # Convert the contents of the file to a Python dictionary
            config = json.loads(file.read())

        return config