# Installs CodeIgniter to the current directory
import urllib
import urllib.request
import os
import sys
import zipfile

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

        print('Downloading CodeIgniter from', url, 'into', sys.argv[1])

        self.download_zip(url, zip_file['name'])

        print('Done')
        print('Extracting file contents...')

        self.extract_files(zip_file['name'], sys.argv[1])

        print('Removing temprorary files...')

        os.remove(zip_file['name'])

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

    def show_message(self):
        print('Bee Gold - CodeIgniter Installer')
        print('MIT Callum John @ItsSeaJay 2018')
        print('https://github.com/ItsSeaJay/bee-gold/')
        print('Usage: python3 install.py [installation_path] [version_number]')
    
    def get_latest_release(self):
        pass

installer = Installer()

if len(sys.argv) > 1:
    installer.install()
else:
    installer.show_message()