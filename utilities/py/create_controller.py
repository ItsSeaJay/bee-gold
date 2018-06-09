# Adds a new controller to a CodeIgniter Installation
import json
import os
import sys
import string

# Get the version number
version_number = '3.1.8'
# Get the path of the new class
location = input('Enter the location of the new controller [\'Super\']: ') or 'Super'
# Get the base name from the location
base_name = os.path.basename(os.path.normpath(location))

# Get the contents of the config file and convert it to a Python dictionary
with open('config.json', 'r') as file:
    config = json.loads(file.read())

# Get the contents of the template and format it into a controller
with open('templates/controller.template.php', 'r') as file:
    template = file.read()
    controller = template.format(name = base_name)

# Write that controller to the appropriate folder
base_name = config['paths']['install'] + 'application/controllers/' + os.path.dirname(location)

# Make sure that the directories exist
if not os.path.exists(base_name):
    os.makedirs(base_name)

# Then write the file into that location
file_path = config['paths']['install'] + 'application/controllers/' + location + '.php'

with open(file_path, 'w') as file:
    file.write(controller)

print('Created new controller at', file_path)