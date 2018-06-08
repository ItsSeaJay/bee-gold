import os
import shutil

source = '../CodeIgniter-3.1.8/'
destination = '../'

# Move the contents of the codeigniter folder to another location
for file_name in os.listdir(source):
    if not os.path.exists(destination + file_name):
        shutil.move(source + file_name, destination)

shutil.rmtree(source)