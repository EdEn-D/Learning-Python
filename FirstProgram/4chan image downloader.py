import os
import requests
import urllib.request
from bs4 import BeautifulSoup


url = 'https://boards.4chan.org/s/thread/17409181'

def picSpider (url):
    picNumber = 0
    os.chdir(r'C:/Users/Eden/Desktop')

    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    findtitle = soup.find('span', {'class': 'subject'})     # finds the title of the subChan as well as the class and subject etc
    title = findtitle.string                                # only stores the title of the subchan

if not os.path.exists(str(title)):
    os.makedirs(str(title))                                 # creates a folder
    os.chdir(r'C:/Users/Eden/Desktop/' + str(title))
    #print(title)

    for link in soup.findAll('a', {'class': 'fileThumb'}):
        picName = str(picNumber) + ".jpg"
        href = link.get('href')
        imageLink = 'https:' + href
        urllib.request.urlretrieve(imageLink, picName)
        picNumber += 1
        print(imageLink)
        if picNumber == 100:
            break


picSpider("link...")