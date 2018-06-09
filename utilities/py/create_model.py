# Adds a new model to a CodeIgniter Installation
import json
import os
import sys
import string

# Get the version number
version_number = '3.1.8'
# Get the path of the new class
name = input('Enter the name of the new model [\'Super_model\']: ') or 'Super'
# Format the name of the new model into a valid name
name = name.lower().capitalize()
name = name + '_model'
# Get the name of the table used by this model
table = input('Enter the database table that this model will use [\'test\']: ') or 'test'

# Get the contents of the config file and convert it to a Python dictionary
with open('config.json', 'r') as file:
    config = json.loads(file.read())

# Get the contents of the template and format it into a model
with open('templates/model.template.php', 'r') as file:
    template = file.read()
    model = template.format(
        name = name, # The name of the class
        table = table # The database table that it uses
    )

# Write that model to the appropriate folder
base_name = config['paths']['install'] + 'application/models/' + os.path.dirname(name)

# Make sure that the directories exist
if not os.path.exists(base_name):
    os.makedirs(base_name)

# Then write the file into that location
file_path = config['paths']['install'] + 'application/models/' + name + '.php'

with open(file_path, 'w') as file:
    file.write(model)

print('Created new model at', file_path)