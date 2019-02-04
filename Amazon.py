from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

list1 = []

def amazon(item):
    url = "https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="+item
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    all_products = soup.findAll('div', attrs={'class' : 's-item-container'})
    print(all_products)

    for item in all_products:
        products = {}

        title = item.findAll('a',
                             {'class' : 'class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"'})
        print(title)

amazon('oneplus6T')