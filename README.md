# UNDER CONSTRUCTION

BLUE PRINT

First scan the http folder for files, download em
Scan again for folders
then infinitely loop both the above functions for




TODO

Download the files
Check for files in local before downloading
get a progress bar for downloading






















# download-web-directory
 Download Web Directory 















## Todo
✔️️👳‍♀️❌

Support for surface web ✔️

Support for onion links ✔️

Directory to download to

how long will the downloader go

progress bar for each file

develop a tree map

scan and skip already downloaded files and folders

get new identity in tor.exe when running for too long




## Windows

### One line installation
```
git clone https://github.com/alx-xlx/download-web-directory.git
cd download-web-directory
windows.bat
```

### OR

```
git clone https://github.com/alx-xlx/download-web-directory.git
cd download-web-directory
pip install requests
pip install -U requests[socks]
pip install bs4
pip install lxml
```

### Run

```
python surface_net.py
```

## Linux
### Install Torsocks
[torsocs](https://gitweb.torproject.org/torsocks.git/tree/README.md)

```
git clone https://git.torproject.org/torsocks.git
cd torsocks
./autogen.sh
./configure
make
sudo make install
cd ..
```

Now install `download-web-directory`

```
git clone https://github.com/alx-xlx/download-web-directory.git
cd download-web-directory
pip3 install requests
pip3 install -U requests[socks]
pip3 install bs4
pip3 install lxml

```

### Run

```
torsocks python3 deepnet.py
```