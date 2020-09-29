import requests
from bs4 import BeautifulSoup



def newbostonSpider():
    url = 'https://thenewboston.com/forum/topic.php?id=1610'
    source_code = requests.get(url)
    plainText = source_code.text
    soup = BeautifulSoup(plainText, "html.parser")
    for code in soup.findAll('code', {'class': 'hljs python'}):
        final = code.string
        print (final)

def getItemData(itemUrl):
    source_code = requests.get(itemUrl)
    plainText = source_code.text
    soup = BeautifulSoup(plainText, "html.parser")
    for itemPrice in soup.findAll('span', {'itemprop':'price'}):
        print(itemPrice.string)
    for link in soup.findAll('a'):
        href = 'http://www.kijiji.ca' + link.get('href')
        print (href)

newbostonSpider()