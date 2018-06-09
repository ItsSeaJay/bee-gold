# Installs CodeIgniter to the specified directory
# Modules
import json
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
        # Get the configuration for this
        config = self.get_config()
        # Build the download URL based on the chosen version number
        url = 'https://github.com/bcit-ci/CodeIgniter/archive/' + config['codeigniter']['version'] + '.zip'
        templates = self.get_templates([
            'templates/config/config.template.php',
            'templates/config/database.template.php',
            'templates/index.template.php'
        ])
        # Determine where the zip file will be downloaded
        zip_file = {
            'name': config['paths']['install'] + 'download.zip'
        }

        print('Verifying install directory...')

        if not os.path.exists(config['paths']['install']):
            os.makedirs(config['paths']['install'])
        
        print('Downloading CodeIgniter from', url, 'into', config['paths']['install'], '...')

        self.download_zip(url, zip_file['name'])

        print('Extracting file contents to temporary location...')

        self.extract_files(zip_file['name'], config['paths']['install'])

        print('Moving CodeIgniter files into specified root...')

        self.move_files(config['paths']['codeigniter'], config['paths']['install'])

        print('Formatting main config file...')

        # Overwrite the main config file with a formatted template
        with open(config['paths']['install'] + '/application/config/config.php', 'w') as file:
            file.write(
                templates['templates/config/config.template.php'].format(
                    base_url = config['base_url']
                )
            )

        print('Formatting the database config file...')

        # Overwite the database config file with a formatted template
        with open(config['paths']['install'] + '/application/config/database.php', 'w') as file:
            file.write(
                templates['templates/config/database.template.php'].format(
                    hostname = config['database']['hostname'],
                    username = config['database']['username'],
                    password = config['database']['password'],
                    database = config['database']['name']
                )
            )
        
        print('Creating public assets...')

        if not os.path.exists(config['paths']['install'] + 'public'):
            os.makedirs(config['paths']['install'] + 'public')

        # Create a new index file in it's own folder
        with open(config['paths']['install'] + 'public/index.php', 'w') as file:
            file.write(templates['templates/index.template.php'])

        print('Done.')
        print('Removing unneccessary files...')

        self.cleanup(config['paths']['install'], zip_file['name'])

        print('Done.')
        print('Saving input as config.json...')

        with open('config.json', 'w') as file:
            # Convert the user's configuration into a json file
            json.dump(
                config, # Path
                file, # File to output to
                sort_keys = True, # Whether to sort the keys or not
                indent = 4, # Number of spaces to indent by
                separators = (',', ':')
            )

        print('Installation complete!')
    
    def welcome(self):
        print('CodeIgniter Honey - Installer')
        print('MIT Callum John @ItsSeaJay 2018')

    def download_zip(self, url, location):
        urllib.request.urlretrieve(url, location)

    def extract_files(self, name, location):
        zip = zipfile.ZipFile(name, 'r')

        zip.extractall(location)
        zip.close()

    def move_files(self, source, destination):
        # Move the contents of the chosen folder to another location
        for file_name in os.listdir(source):
            if not os.path.exists(destination + file_name):
                shutil.move(source + file_name, destination)

    def cleanup(self, path, zip):
        # TODO: take the version number into account
        shutil.rmtree(path + 'CodeIgniter-3.1.8')
        shutil.rmtree(path + 'user_guide')

        # Remove the old index file
        if os.path.exists(zip):
            os.remove(zip)
        
        # Remove the old index file
        if os.path.exists(path + 'index.php'):
            os.remove(path + 'index.php')
        
        # Remove the old index file
        if os.path.exists(zip):
            os.remove(zip) 

    def get_templates(self, paths):
        templates = {}

        for path in paths:
            with open(path, 'r') as file:
                templates[path] = file.read()
        
        return templates

    def get_base_url(self):
        base_url = input('Enter Base URL [\'http://localhost/CodeIgniter-3.1.8\']: ') or 'http://localhost/CodeIgniter-3.1.8'

        return base_url
    
    def get_config(self):
        config = {
            'codeigniter': {
                version: input('Enter the CodeIgniter version [\'3.1.8\']') or '3.1.8'
            },
            'application': {
                # The application path needs to be based off the root utilities folder
                'path': '../../' + input('Enter desired install path [\'../\']: ') or '../../' + '../',
                'name': input('Enter your application name [\'My CodeIgniter Application\']') or 'My CodeIgniter Application'
                'author': input('Enter your name [\'John \'Rasmuslerdorf\' Doe\']: ') or 'John \'Rasmuslerdorf\' Doe'
            },
            'database': {
                'hostname': input('Enter database hostname [\'localhost\']:  ') or 'localhost',
                'username': input('Enter database username [\'root\']:  ') or 'root',
                'password': input('Enter database password [\'\']:  ') or '',
                'name': input('Enter database name [\'test\']:  ') or 'test'
            },
            'base_url': self.get_base_url(),
            'database': self.get_database_config()
        }
        # The codeigniter path requires previous knowledge of the config dictionary
        # so set it after everything else
        config['codeigniter']['path'] = config['paths']['install'] + 'CodeIgniter-' + version_number + '/'

        return config

installer = Installer()
installer.welcome()
installer.install()