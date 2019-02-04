import requests
from bs4 import BeautifulSoup

list1 = []

def ebay(item):
    url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + item + "&_sacat=0&_pgn=1"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    all_products = soup.findAll('li', {'class': 's-item'})

    for itm in all_products:
        items = {}

        title = itm.findAll('a', {'class': 's-item__link'})[0]
        #list_title.append(title.text)
        items['title']=title.text

        link = title['href']
        #list1.append(link)
        items['link']=link

        price = itm.findAll('span', {'class': 's-item__price'})[0]
        #list1.append(price.text)
        items['price']=price.text

        #for i in list_title:
        #    items[i] = "["+list1[0]+", "+list1[1]+"]"
        list1.append(items)
    return list1

# filter prices
def filter_prices(min, max, item):
    range = "&_udlo=" + str(min) + "&_udhi=" + str(max)
    url2 = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + item + range + "&_sacat=0&_pgn=1"
    html = requests.get(url2)
    soup = BeautifulSoup(html.content, 'html.parser')

    for itm in soup.findAll('li', {'class': 's-item'}):
        title = itm.findAll('a', {'class': 's-item__link'})[0]
        print(title.text)
        link = title['href']
        print(link)
        price = itm.findAll('span', {'class': 's-item__price'})[0]
        print(price.text + "\n")