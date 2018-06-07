# Installs CodeIgniter to the current directory
import urllib
import os
import zipfile

url = 'https://github.com/bcit-ci/CodeIgniter/archive/3.1.8.zip'
zip_file = {
    'name': 'temp.zip'
}

urllib.urlretrieve(url, zip_file['name'])

# Extract the zip file to the current folder
zip_file['instance'] = zipfile.ZipFile(zip_file['name'], 'r')
zip_file['instance'].extractall()
zip_file['instance'].close()

# Delete the downloaded zip file
os.remove(zip_file['name'])