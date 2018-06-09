from factory import Factory
import json
import os
import sys
import string

class Model_factory(Factory):
    def __init__(self):
        pass
    
    def create(self):
        self.config = self.get_config()
        self.name = input('Enter the path of the model [\'Blog\']: ') or 'Blog'
        self.table = input('Enter the database table [\'test\']: ') or 'test'
        # Get the template of the folder
        self.template = self.get_template()
        # Build the path for the new model
        path = self.config['project']['path'] + 'application/models/' + self.name.title() + '_model.php'

        # Write the new model as a file
        with open(path, 'w') as file:
            file.write(self.template)
        
        print('Created a new model at', path)
    
    def get_template(self):        
        with open('templates/application/model.template.php', 'r') as file:
            template = file.read()
            template = template.format(
                name = self.name,
                table = self.table
            )

        return template

factory = Model_factory()
factory.create()