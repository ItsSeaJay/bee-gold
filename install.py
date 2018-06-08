# Installs CodeIgniter to the current directory
# Modules
import urllib
import urllib.request
import os
import sys
import zipfile
from string import Template

"""
    The installer class handles the download and setup of CodeIgniter,
    using the command line arguments to determine how it should be set up.
"""
class Installer:
    def __init__(self):
        pass

    def install(self):
        # Determine where the latest version is and where the file should be stored
        version_number = '3.1.8'
        url = 'https://github.com/bcit-ci/CodeIgniter/archive/' + version_number + '.zip'
        zip_file = {
            'name': 'download.zip'
        }
        templates: {
            'test': {
                'path': 'templates/test.template.php'
            }
        }
        base_url = self.get_base_url()
        print(base_url)

        with open(templates['test']['path'], 'r') as template:
            templates['test']['contents'] = print(template.read())
        
        print(templates['test']['contents'])
        print(base_url)
        print('Downloading CodeIgniter from', url, 'into', sys.argv[1])

        # self.download_zip(url, zip_file['name'])

        print('Done.')
        print('Extracting file contents...')

        # self.extract_files(zip_file['name'], sys.argv[1])

        print('Removing temprorary files...')

        # os.remove(zip_file['name'])

        print('Done.')

        print('Installation complete!')
    
    def download_zip(self, url, location):
        try:
            zip = urllib.request.urlretrieve(url, location)
        except Exception as e:
            pass # TODO: Figure out how to output error messages

    def extract_files(self, name, location):
        zip = zipfile.ZipFile(name, 'r')
        zip.extractall(location)
        zip.close()

    def get_base_url(self):
        base_url = input('Enter Base URL:')

        return base_url

    def show_message(self):
        parameters = [
            '[installation_path]',
            '[version_number]',
            '[base_url]'
        ]
        usage = 'Usage: python3 install.py'

        print('Bee Gold - CodeIgniter Installer')
        print('MIT Callum John @ItsSeaJay 2018')
        print('https://github.com/ItsSeaJay/bee-gold/')

        # Build the usage string based on the kinds of parameters in the list
        for parameter in parameters:
            usage = usage + ' ' + parameter
        
        print(usage)

installer = Installer()

if len(sys.argv) > 1:
    installer.install()
else:
    installer.show_message()