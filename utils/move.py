import os
import shutil

source = '../CodeIgniter-3.1.8/'
destination = '../'

for file_name in os.listdir(source):
    shutil.move(source + file_name, destination)