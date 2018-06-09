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
        Performs the installation process
    """
    def install(self):
        # Get the configuration for this
        self.config = self.get_config()
        # Build the download URL based on the chosen version number
        download_url = 'https://github.com/bcit-ci/CodeIgniter/archive/' + self.config['codeigniter']['version'] + '.zip'
        # Get the templates from the templates folder
        templates = self.get_templates([
            'templates/config/config.template.php',
            'templates/config/database.template.php',
            'templates/index.template.php'
        ])
        # Determine where the zip file will be downloaded
        zip_file = self.config['project']['path'] + 'CodeIgniter-' + self.config['codeigniter']['version'] + '.zip'

        print('Verifying install directory...')

        # Make the install directory if it doesn't already exist
        if not os.path.exists(self.config['project']['path']):
            os.makedirs(self.config['project']['path'])
        
        print(
            'Downloading CodeIgniter from',
            download_url,
            'into',
            self.config['project']['path'], 
            '...'
        )

        # Download the zip file from the internet and store it locally
        self.download(download_url, zip_file)

        print('Extracting file contents to temporary location...')

        # Extract everything from the zip folder
        self.extract_files(zip_file, self.config['project']['path'])

        print('Moving CodeIgniter files into specified root...')

        # Move everything from the top level folder into the project folder
        self.move_files(self.config['codeigniter']['path'], self.config['project']['path'])

        print('Formatting main config file...')

        # Overwrite the main config file with a formatted template
        with open(self.config['project']['path'] + '/application/config/config.php', 'w') as file:
            file.write(
                templates['templates/config/config.template.php'].format(
                    base_url = self.config['base_url']
                )
            )

        print('Formatting the database config file...')

        # Overwite the database config file with a formatted template
        with open(self.config['project']['path'] + '/application/config/database.php', 'w') as file:
            file.write(
                templates['templates/config/database.template.php'].format(
                    hostname = self.config['database']['hostname'],
                    username = self.config['database']['username'],
                    password = self.config['database']['password'],
                    database = self.config['database']['name']
                )
            )
        
        print('Creating public assets...')

        if not os.path.exists(self.config['project']['path'] + 'public'):
            os.makedirs(self.config['project']['path'] + 'public')

        # Create a new index file in it's own folder
        with open(self.config['project']['path'] + 'public/index.php', 'w') as file:
            file.write(templates['templates/index.template.php'])

        print('Done.')
        print('Removing unneccessary files...')

        self.cleanup(self.config['project']['path'], zip_file['name'])

        print('Done.')
        print('Saving input as config.json...')

        self.save_config()

        print('Installation complete!')

    """
        Gets the install configuration from user input.
    """
    def get_config(self):
        config = {
            'codeigniter': {
                'version': input('Enter the CodeIgniter version [\'3.1.8\']: ') or self.get_latest_version()
            },
            'project': {
                # The project path needs to be based off the root utilities folder
                'path': input('Enter desired install path [\'../\']: ') or '../',
                'name': input('Enter your project\'s name [\'My CodeIgniter Application\']: ') or 'My CodeIgniter Application',
                'author': input('Enter your name [\'John \'Rasmuslerdorf\' Doe\']: ') or 'John \'Rasmuslerdorf\' Doe',
                'base_url': input('Input your project\'s base URL [\'http://localhost/bee-gold/public/\']: ') or 'http://localhost/bee-gold/public/'
            },
            'database': {
                'hostname': input('Enter database hostname [\'localhost\']:  ') or 'localhost',
                'username': input('Enter database username [\'root\']:  ') or 'root',
                'password': input('Enter database password [\'\']:  ') or '',
                'name': input('Enter database name [\'test\']:  ') or 'test'
            }
        }
        # Setting the path to CodeIgniter requires the config dictionary exists
        config['codeigniter']['path'] = config['project']['path'] + 'CodeIgniter-' + config['codeigniter']['version'] + '/'

        return config

    """
        Saves the install configuration as a JSON file
    """
    def save_config(self):
        with open('../../json/config.json', 'w') as file:
            # Convert the user's configuration into a json file
            # and store it on disk
            json.dump(
                config, # Data to encode
                file, # Name of the file to output to
                sort_keys = True, # Whether to sort the keys or not
                indent = 4, # Number of spaces to indent by
                separators = (',', ' : ') # How the seperators should be formatted
            )

    """
        Returns a list of templates based on their relative path
    """
    def get_templates(self, paths):
        templates = {}

        for path in paths:
            with open(path, 'r') as file:
                templates[path] = file.read()
        
        return templates

    """
        Gets the latest version of CodeIgniter
    """
    # TODO: Get the return value from CodeIgniter's online RSS feed
    def get_latest_version(self):
        return '3.1.8'

    """
        Downloads a given file from the internet
    """
    def download(self, source, destination):
        urllib.request.urlretrieve(source, destination)

    """
        Extracts the codeigniter files to a proper location
    """
    def extract_files(self, name, location):
        zip = zipfile.ZipFile(name, 'r')

        zip.extractall(location)
        zip.close()

    """
        Moves a tree of files from one location to another
    """
    def move_files(self, source, destination):
        # Move the contents of the chosen folder to another location
        # so long as it exists
        for file_name in os.listdir(source):
            if not os.path.exists(destination + file_name):
                shutil.move(source + file_name, destination)

    """
        Removes excess files left after installation
    """
    def cleanup(self, path, zip):
        # TODO: take the version number into account
        shutil.rmtree(path + 'CodeIgniter-' + self.config['codeigniter']['version'])

        # Remove the old index file
        if os.path.exists(zip):
            os.remove(zip)
        
        # Remove the old index file
        if os.path.exists(path + 'index.php'):
            os.remove(path + 'index.php')
        
        # Remove the old index file
        if os.path.exists(zip):
            os.remove(zip)