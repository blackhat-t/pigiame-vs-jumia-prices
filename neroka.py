import requests
from bs4 import BeautifulSoup
import grequests

def exctractlinks(url):
    page =  requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    divbox = 'product-categories'
    divs = soup.findAll(class_= divbox)
    links = []
    for li in divs:
        for link in  li.find_all('a'):
            links.append(link.get('href'))
    return links


def scraper(url):
    page =  requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    main = 'content-area'
    divs = soup.findAll(class_=main)  
    for div in divs:
        products = div.findAll(class_='products') 
        for prod in products:
            product = prod.findAll(class_= 'product') 
            for item in product:
                try:
                    title = 'woocommerce-loop-product__title'
                    price = 'woocommerce-Price-amount amount'
                    title = div.find(attrs={'class': title}).text.strip()
                    price = div.find(attrs={'class': price}).text.strip()
                    print(title, price)
                except Exception:
                    print('Error occured')

def main():
    url = 'https://arduino.co.ke/'
    links = exctractlinks(url)
    for link in links:
        scraper(link)



if __name__ == "__main__":
    main()
    