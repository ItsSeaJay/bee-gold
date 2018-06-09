from factory import Factory
import json
import os
import sys
import string

class Controller_factory(Factory):
    def __init__(self):
        pass
    
    def create(self):
        self.config = self.get_config()
        location = input('Enter the path of the controller [\'Super\']: ') or 'Super'
        # Get the name of the controller entered
        self.name = os.path.basename(os.path.normpath(location))
        # Get the template of the folder
        self.template = self.get_template()
        # Get the name of the folder that this controller will use
        folder = self.config['project']['path'] + 'application/controllers/' + os.path.dirname(location)
        # Build the path for the new controller
        path = folder + '/' + self.name.title() + '.php'

        # Make sure that the controller's subfolder exists
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Write the new controller as a file
        with open(path, 'w') as file:
            file.write(self.template)
        
        print('Created a new controller at', path)
    
    def get_template(self):        
        with open('templates/application/controller.template.php', 'r') as file:
            template = file.read()
            template = template.format(
                name = self.name
            )

        return template

factory = Controller_factory()
factory.create()