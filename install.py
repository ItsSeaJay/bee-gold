# Installs CodeIgniter to the current directory
import urllib.request
import os
import sys
import zipfile

url = 'https://github.com/bcit-ci/CodeIgniter/archive/3.1.8.zip'
zip_file = {
    'name': 'temp.zip'
}

print('Downloading file ', zip_file['name'], ' from ', url)

urllib.request.urlretrieve(url, zip_file['name'])

print('Done')
print('Extracting file contents...')

zip_file['instance'] = zipfile.ZipFile(zip_file['name'], 'r')
zip_file['instance'].extractall(sys.argv[1] or '')
zip_file['instance'].close()

print('Removing temprorary files...')

os.remove(zip_file['name'])

print('Done.')
print('Installation complete!')
