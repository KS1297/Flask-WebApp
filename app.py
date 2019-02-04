from flask import Flask, render_template, request, redirect,url_for,abort
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/home', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        if request.form['search'] != "":
            i = request.form['search']
            item1 = ebay(i)
            item2 = flipkart(i)
            return render_template("search.html", product1=item1, product2=item2)
        else:
            return render_template("search.html")
    else:
        #abort(302)
        return render_template("search.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

def ebay(item):
    list1 = []
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

def flipkart(item):
    list1 = []
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
