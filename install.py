# Installs CodeIgniter to the current directory
import urllib.request
import urllib.request
import os
import sys
import zipfile

if len(sys.argv) > 1:
    version_number = '3.1.8'
    url = 'https://github.com/bcit-ci/CodeIgniter/archive/' + version_number + '.zip'
    zip_file = {
        'name': 'download.zip'
    }

    print('Downloading file', zip_file['name'], 'from', url)

    urllib.request.urlretrieve(url, zip_file['name'])

    print('Done')
    print('Extracting file contents...')

    zip_file['instance'] = zipfile.ZipFile(zip_file['name'], 'r')
    zip_file['instance'].extractall(sys.argv[1])
    zip_file['instance'].close()

    print('Removing temprorary files...')

    os.remove(zip_file['name'])

    print('Done.')
    print('Installation complete!')
else:
    print('Bee Gold - CodeIgniter Installer')
    print('MIT Callum John @ItsSeaJay 2018')
    print('https://github.com/ItsSeaJay/bee-gold/')
    print('Usage: python3 install.py [installation_path] [version_number]')
