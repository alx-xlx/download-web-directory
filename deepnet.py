import requests
from bs4 import BeautifulSoup
import os
import sys
import urllib

URL = "http://awaken4u2655myzx.onion/F3thinker%2001/"

proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

root = requests.get(URL)
soup = BeautifulSoup(root.content,'lxml')

files = []
dir = []
# Gather all the files
for img in soup.find_all('img',{'src':True}):
    if (img['src'] == '/icons/blank.gif' or img['src'] == '/icons/back.gif' or img['src'] == '/icons/folder.gif'):
        continue
    if img['src'] == '/icons/folder.gif':
        subddir_name = img.find_next('a')['href']
        subddir_url = URL + subddir_name
        dir.append(subddir)
    files.append(img.find_next('a')['href'])

    print(files)

# Download those files

for eachfile in range(len(files)):
    download_link = URL + files[eachfile]              # Download LInk
    filename = urllib.parse.unquote(files[eachfile])   # Filename

    rawfile = requests.get(download_link)
    with open(filename, 'wb') as f:
        f.write(rawfile.content)

    print(' ' + filename + ' Done !! ' + str(eachfile+1) + '/' +  len(files))

