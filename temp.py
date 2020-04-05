import os
import sys
import requests
import urllib
from bs4 import BeautifulSoup
from tqdm import tqdm

proxies = {
	'http':  'socks5h://127.0.0.1:9050',
	'https': 'socks5h://127.0.0.1:9050'
	}
# TODO: Let user decide how deep to scrape?

def scrapeFolder(url, destFolder):

	# TODO: Progress bar for each file download
	
	# If requests can't get the url somehow, print the error message and exit
	try:
		page = requests.get(url, proxies=proxies)
	except requests.exceptions.RequestException as e:
		print(e)
		sys.exit(1)

	soup = BeautifulSoup(page.content, 'html.parser')

	# Array comprising of the relative links of all files in this folder
	allFiles = []
	j = 0
	for img in soup.find_all('img',{'src':True}):
		if not (img['src'] == '/icons/blank.gif' or img['src'] =='/icons/back.gif' or img['src'] == '/icons/folder.gif'):
			allFiles.append(img.find_next('a')['href'])
			print(' ' + str(j+1) + ' of ' + str(len(soup.find_all('img',{'src':True}))) + '  ' + img.find_next('a')['href'])
			# sys.stdout.write('\x1b[1A')
			# sys.stdout.write('\x1b[2K')
	# For each relative link in allFiles, turn it into an absolute link and download it into destFolder
	for i in range(len(allFiles)):
		relativeLink = allFiles[i]
		absoluteLink = url + relativeLink
		filename = urllib.parse.unquote(relativeLink)
		if filename in file_entries:
			print('Skipping ', filename)
			continue
		r = requests.get(absoluteLink, stream=True, proxies=proxies)
		total_size = int(r.headers.get('content-length',0))
		block_size = 1024
		t=tqdm(total=total_size, unit='iB', unit_scale=True)
		with open(destFolder + '/' + filename, 'wb') as f:
			for data in r.iter_content(block_size):
				t.update(len(data))
				f.write(data)
		t.close()
		sys.stdout.write('\x1b[1A')
		sys.stdout.write('\x1b[2K')
		if total_size != 0 and t.n != total_size:
			print("ERROR, something went wrong")
		print('File ' + str(i+1) + ' of ' + str(len(allFiles)) + ' is downloaded: ' + '  ' + filename)

	print('All files downloaded from:')
	print(url)


def getChildrenDir(url, destFolder, dirArray):

	# If requests can't get the url somehow, print the error message and exit
	try:
		page = requests.get(url, proxies=proxies)
	except requests.exceptions.RequestException as e:
		print(e)
		sys.exit(1)

	soup = BeautifulSoup(page.content, 'html.parser')

	# Append the name and absolute link of every folder in the directory tree to dirArray
	for img in soup.find_all('img',{'src':True}):
		if img['src'] == '/icons/folder.gif':
			subfolderName = img.find_next('a')['href']
			subfolder = (destFolder + '/' + subfolderName, url + subfolderName)
			dirArray.append(subfolder)


if (len(sys.argv) == 2 or len(sys.argv) == 3):

	url = sys.argv[1]
	file_entries = os.listdir(sys.argv[2])

	if len(sys.argv) == 2:
		file_entries = os.listdir('Downloads')
		destFolder = 'Downloads'

	else:
		destFolder = sys.argv[2]

	dirArray = []

	# Get subfolders and scrape files from top directory
	if not os.path.exists(destFolder):
		os.makedirs(destFolder)

	getChildrenDir(url, destFolder, dirArray)
	scrapeFolder(url, destFolder)
	
	# Traverse the directory tree, getting subfolders and scraping files
	while dirArray:
		subfolder = dirArray.pop(0)
		url = subfolder[1]
		destFolder = urllib.parse.unquote(subfolder[0])

		if not os.path.exists(destFolder):
			os.makedirs(destFolder)

		getChildrenDir(url, destFolder, dirArray)
		scrapeFolder(url, destFolder)

else:

	print('Usage: python http-directory-downloader.py url [destFolder]')