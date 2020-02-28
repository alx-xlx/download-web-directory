import requests
from bs4 import BeautifulSoup
import os
import sys
import urllib

URL = "http://hcmaslov.d-real.sci-nnov.ru/public/texts/%d0%97%d0%b0%d0%b4%d0%b0%d1%87%d0%b0%20%d0%bd%d0%b0%20%d1%81%d0%be%d0%be%d0%b1%d1%80%d0%b0%d0%b7%d0%b8%d1%82%d0%b5%d0%bb%d1%8c%d0%bd%d0%be%d1%81%d1%82%d1%8c/%d0%91%d1%83%d1%80%d0%b0%d1%82%d0%b8%d0%bd%d0%be%20%d0%b8%20%d1%8f%d0%b1%d0%bb%d0%be%d0%ba%d0%b8/"



# get sub dir


# 


# def main():


# Get Subdirectory
def subDir(URL,dir):
    rawSubFolder = requests.get(url)
    soup = BeautifulSoup(rawSubFolder.content, 'lxml')
    for img in soup.find_all('img',{'src':True}):
        if img['src'] == '/icons/folder.gif':
            subddir_name = img.find_next('a')['href']
            subddir_url = URL + subddir_name
            dir.append(subddir)

def download(URL):

    root = requests.get(URL)
    soup = BeautifulSoup(root.content,'lxml')

    files = []
    dir = []
    # Gather all the files
    for img in soup.find_all('img',{'src':True}):
        if (img['src'] == '/icons/blank.gif' or img['src'] == '/icons/back.gif' or img['src'] == '/icons/folder.gif'):
            continue
        files.append(img.find_next('a')['href'])

        print(files)


    file_entries = os.listdir('Downloaded')


    # Download those files

    for eachfile in range(len(files)):
        download_link = URL + files[eachfile]              # Download LInk
        filename = urllib.parse.unquote(files[eachfile])   # Filename


        # Check if files are already downloaded
        if filename in file_entries:
            print('>>>  Skipping >>>>  ',filename)
            continue
        
        rawfile = requests.get(download_link)
        with open(filename, 'wb') as f:
            f.write(rawfile.content)

        print(' ' + filename + ' Done !! ' + str(eachfile+1) + '/' +  len(files))





def main():
    
    dir = []

    subDir(URL, dir)
    download(URL)


    while dir:
        subDir = dir.pop(0)
        print('Subfolder - ', subDir)
        url = subDir[1]
        print('URL - ', url)