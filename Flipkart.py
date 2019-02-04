import requests
from bs4 import BeautifulSoup

list1 = []

def flipkart(item):
    url = "https://www.flipkart.com/search?q="+item+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    all_products = soup.findAll('div', {'class': '_3O0U0u'})
    #print(all_products)

    for item in all_products:
        products = {}

        try:
            title = item.find_all('div', {'class': '_3wU53n'})[0]
            products['title'] = title.text
            # print(products['title'])

            # image = item.find_all('img')[0]
            # if image.get("data-src"):
            #    img_url = image.get("data-src")
            # else:
            #    img_url = image.get("src")
            # products['image']=i
            # print(img_url)

            t = item.find_all('a')[0]
            link = t['href']
            products['link'] = "https://www.flipkart.com" + link
            # print(products['link'])

            price = item.findAll('div', {'class': '_1vC4OE _2rQ-NK'})[0]
            products['price'] = price.text
            # print(products['price'])

            list1.append(products)
        except IndexError:
            a = item.find_all('a', {'class': '_2cLu-l'})[0]
            title = a['title']
            products['title'] = title
            # print(products['title'])

            # image = item.find_all('img')[0]
            # if image.get("data-src"):
            #    img_url = image.get("data-src")
            # else:
            #    img_url = image.get("src")
            # products['image']=i
            # print(img_url)

            link = a['href']
            products['link'] = "https://www.flipkart.com" + link
            # print(products['link'])

            price = item.findAll('div', {'class': '_1vC4OE'})[0]
            products['price'] = price.text
            # print(products['price'])

            list1.append(products)

    return list1

#flipkart('xbox')