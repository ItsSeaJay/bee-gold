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
    using user input to determine how it should be configured.
"""
class Installer:
    def __init__(self):
        pass

    """
        Welcomes the user to the program
    """
    def welcome(self):
        print('CodeIgniter Honey - Installer')
        print('MIT Callum John @ItsSeaJay 2018')

    """
        Handles the installation process
    """
    def install(self):
        # Get the configuration for this
        self.config = self.get_config()
        # Build the download URL based on the chosen version number
        download_url = 'https://github.com/bcit-ci/CodeIgniter/archive/' + config['codeigniter']['version'] + '.zip'
        # Get the templates from the templates folder
        templates = self.get_templates([
            'templates/config/config.template.php',
            'templates/config/database.template.php',
            'templates/index.template.php'
        ])
        # Determine where the zip file will be downloaded
        zip_file = config['application']['path'] + 'CodeIgniter-' + config['codeigniter']['version'] + '.zip'

        print('Verifying install directory...')

        # Make the install directory if it doesn't already exist
        if not os.path.exists(config['application']['path']):
            os.makedirs(config['application']['path'])
        
        print(
            'Downloading CodeIgniter from',
            url,
            'into',
            config['paths']['install'], 
            '...'
        )

        self.download(download_url, zip_file)

        print('Extracting file contents to temporary location...')

        self.extract_files(zip_file], config['paths']['install'])

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

        self.save_config()

        print('Installation complete!')

    def get_config(self):
        config = {
            'codeigniter': {
                version: input('Enter the CodeIgniter version [\'3.1.8\']') or '3.1.8'
            },
            'application': {
                # The application path needs to be based off the root utilities folder
                'path': '../../' + input('Enter desired install path [\'../\']: ') or '../../' + '../',
                'name': input('Enter your application name [\'My CodeIgniter Application\']') or 'My CodeIgniter Application'
                'author': input('Enter your name [\'John \'Rasmuslerdorf\' Doe\']: ') or 'John \'Rasmuslerdorf\' Doe',
                'base_url': input('')
            },
            'database': {
                'hostname': input('Enter database hostname [\'localhost\']:  ') or 'localhost',
                'username': input('Enter database username [\'root\']:  ') or 'root',
                'password': input('Enter database password [\'\']:  ') or '',
                'name': input('Enter database name [\'test\']:  ') or 'test'
            }
        }
        # The codeigniter path requires previous knowledge of the config dictionary
        # so set it after everything else
        config['codeigniter']['path'] = config['paths']['install'] + 'CodeIgniter-' + version_number + '/'

        return config
    
    def save_config(self):
        with open('config.json', 'w') as file:
            # Convert the user's configuration into a json file
            json.dump(
                config, # Data
                file, # File to output to
                sort_keys = True, # Whether to sort the keys or not
                indent = 4, # Number of spaces to indent by
                separators = (',', ':')
            )

    def download(self, source, destination):
        urllib.request.urlretrieve(source, destination)

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