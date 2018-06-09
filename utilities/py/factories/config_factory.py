from factory import Factory
import json
import os
import sys
import string

class Config_factory(Factory):
    def __init__(self):
        pass
    
    def create(self):
        self.config = self.get_config()
        self.name = input('Enter the name of the config file [\'custom\']: ') or 'custom'
        self.template = self.get_template(self.name)
        # Build the path for the new config file
        path = self.config['project']['path'] + 'application/config/' + self.name.lower() + '.php'

        with open(path, 'w') as file:
            file.write(self.template)
        
        print('Created a new config file at', path)
    
    def get_template(self, name):        
        with open('templates/application/config.template.php', 'r') as file:
            template = file.read()
            template = template.format(
                name = name
            )

        return template

factory = Config_factory()
factory.create()