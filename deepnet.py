import requests
from bs4 import BeautifulSoup
import os
import sys
import urllib

URL = "http://awaken4u2655myzx.onion/F3thinker%2001/"

proxies = {
    'http': 'socks5h://127.0.0.1:9050',        # Port 9050 if using tor.exe
    'https': 'socks5h://127.0.0.1:9050'        # Port 9051 OR 9052 if using Tor Browser
}

root = requests.get(URL, proxies=proxies)
soup = BeautifulSoup(root.content,'lxml')
