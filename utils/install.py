# Installs CodeIgniter to the specified directory
# Modules
import urllib
import urllib.request
import os
import sys
import shutil
import string
import zipfile

"""
    The installer class handles the download and setup of CodeIgniter,
    using the user input to determine how it should be set up.
"""
class Installer:
    def __init__(self):
        pass

    def install(self):
        # Determine where the latest version is and where the file should be stored
        version_number = '3.1.8'
        url = 'https://github.com/bcit-ci/CodeIgniter/archive/' + version_number + '.zip'
        install_path = input('Enter desired install path [\'../\']:') or '../'
        codeigniter_path = install_path + 'CodeIgniter-' + version_number
        zip_file = {
            'name': 'download.zip'
        }
        templates = self.get_templates([
            'templates/config.template.php',
            'templates/database.template.php',
            'templates/index.template.php'
        ])
        config = {
            'base_url': self.get_base_url(),
            'database': self.get_database_config()
        }
        
        print('Downloading CodeIgniter from', url, 'into', install_path, '...')

        self.download_zip(url, zip_file['name'])

        print('Done.')
        print('Extracting file contents to temporary location...')

        self.extract_files(zip_file['name'], install_path)

        print('Done')
        print('Moving CodeIgniter files into specified root...')

        self.move_files(codeigniter_path, install_path)

        print('Done.')
        print('Formatting main config file...')

        # Overwrite the main config file with a formatted template
        with open(codeigniter_path + '/application/config/config.php', 'w') as file:
            file.write(
                templates['templates/config.template.php']['contents'].format(
                    base_url = config['base_url']
                )
            )

        print('Done.')
        print('Formatting the database config file...')

        # Overwite the database config file with a formatted template
        with open(codeigniter_path + '/application/config/database.php', 'w') as file:
            file.write(
                templates['templates/database.template.php']['contents'].format(
                    hostname = config['database']['hostname'],
                    username = config['database']['username'],
                    password = config['database']['password'],
                    database = config['database']['name']
                )
            )

        print('Done.')
        print('Removing unneccessary files...')

        self.cleanup(codeigniter_path)

        print('Done.')
        print('Installation complete!')
    
    def move_files(self, source, destination):
        # Move the contents of the codeigniter folder to another location
        for file_name in os.listdir(source):
            if not os.path.exists(destination + file_name):
                shutil.move(source + file_name, destination)

    def cleanup(self, path):
        if os.path.exists(path + '/CodeIgniter-3.1.8'):
            shutil.rmtree(path + '/CodeIgniter-3.1.8')

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
        zip = urllib.request.urlretrieve(url, location)

        return zip

    def extract_files(self, name, location):
        zip = zipfile.ZipFile(name, 'r')

        zip.extractall(location)
        zip.close()

    def get_base_url(self):
        base_url = input('Enter Base URL [\'http://localhost/CodeIgniter-3.1.8\']:') or 'http://localhost/CodeIgniter-3.1.8'

        return base_url
    
    def get_database_config(self):
        print('Please enter your database configuration:')

        config = {
            'hostname': input('Enter hostname [\'localhost\']: ') or 'localhost',
            'username': input('Enter username [\'root\']: ') or 'root',
            'password': input('Enter password [\'\']: ') or '',
            'name': input('Enter database name [\'test\']: ') or 'test'
        }

        return config

installer = Installer()
installer.install()