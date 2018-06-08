# Adds a new controller to a CodeIgniter Installation
import os
import sys
import string

# Get the version number
version_number = '3.1.8'
# Get the path of the new class
location = input('Enter the location of the new controller [\'Super\']') or 'Super'
# Get the name from the location
base_name = os.path.basename(os.path.normpath(location))

# Get the contents of the template and format it into a controller
with open('templates/controller.template.php', 'r') as file:
    template = file.read()
    controller = template.format(name = base_name)

# Write that controller to the appropriate folder
base_name = 'CodeIgniter-' + version_number + '/application/controllers/' + os.path.dirname(location)

# Make sure that the directories exist
os.makedirs(base_name)

# Then write the file into that locations
file_path = 'CodeIgniter-' + version_number + '/application/controllers/' + location + '.php'

with open(file_path, 'w') as file:
    file.write(controller)

print(controller)