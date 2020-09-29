import random
import os
import urllib.request

name = 0

def downloadImg(url):
    fullName = str(name) + ".jpg"

    os.chdir(r'C:/Users/Eden/Desktop')
    urllib.request.urlretrieve(url, fullName)




downloadImg("link...")