# Installs CodeIgniter to the specified directory
# Modules
import urllib
import urllib.request
import os
import sys
import string
import zipfile

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
        templates = self.get_templates([
            'templates/config.template.php',
            'templates/index.template.php'
        ])
        base_url = self.get_base_url()
        
        # Don't include the dot in the install path
        if sys.argv[1] != '.':
            path = sys.argv[1] + 'CodeIgniter-' + version_number
        else:
            path = 'CodeIgniter-' + version_number
        
        print('Downloading CodeIgniter from', url, 'into', sys.argv[1])

        # self.download_zip(url, zip_file['name'])

        print('Done.')
        print('Extracting file contents...')

        # self.extract_files(zip_file['name'], sys.argv[1])

        print('Inserting base URL into config file')

        with open(path + '/application/config/config.php', 'w') as file:
            file.write(templates['templates/config.template.php']['contents'].format(base_url = base_url))

        print('Done.')
        print('Removing temprorary files...')

        # os.remove(zip_file['name'])

        print('Done.')

        print('Installation complete!')
    
    def get_templates(self, paths):
        templates = {}

        for path in paths:
            with open(path, 'r') as file:
                template = {
                    'path': path,
                    'contents': file.read()
                }

                templates[path] = template
        
        return templates
    
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