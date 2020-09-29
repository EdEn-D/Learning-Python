import requests
from bs4 import BeautifulSoup



def porsche_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.kijiji.ca/b-cars-vehicles/ontario/porsche/page-' + str(page) +'/k0c27l9004?price=5000__100000'
        source_code = requests.get(url)
        plainText = source_code.text
        soup = BeautifulSoup(plainText, "html.parser")
        for link in soup.findAll('a', {'class': 'title enable-search-navigation-flag '}):
            href = 'http://www.kijiji.ca' + link.get('href')
            title = link.string
            print (title)
            print(href)
            getItemData(href)
        page += 1

def getItemData(itemUrl):
    source_code = requests.get(itemUrl)
    plainText = source_code.text
    soup = BeautifulSoup(plainText, "html.parser")
    for itemPrice in soup.findAll('span', {'itemprop':'price'}):
        print(itemPrice.string)
    for link in soup.findAll('a'):
        href = 'http://www.kijiji.ca' + link.get('href')
        print (href)

porsche_spider(5)