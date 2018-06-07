# Installs CodeIgniter to the current Directory

import urllib

url = 'https://github.com/bcit-ci/CodeIgniter/archive/3.1.8.zip'
file_name = 'CodeIgniter.zip'

urllib.urlretrieve(url, file_name)