import requests
from bs4 import BeautifulSoup


def pigiame(url):
    page =  requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    divbox = 'listings-cards__list-item'
    divs = soup.findAll(class_= divbox)  
    for div in divs:
        try:
            description = 'listing-card__description'
            description = div.find(attrs={'class': description}).text.strip()
            price = 'listing-card__price__value'
            price = div.find(attrs={'class': price}).text.strip()
            condition = 'listing-card__header__tags__item'
            condition = div.find(attrs={'class': condition}).text.strip()
            print(f"CONDITION : {condition}\n{description}\nPRICE {price}\n\n")
        except Exception as ex:
            # print(ex)
            pass
def jumia(url):
    divbox = 'image-wrapper default-state'
    brand = 'brand'
    name = 'name'
    price = 'price'
    page =  requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    divs = soup.findAll(class_= divbox)  
    for div in divs:
        try:
            brand = div.find(attrs={'class': brand}).text.strip()
            name = div.find(attrs={'class': name}).text.strip()
            price = div.find(attrs={'class': price}).text.strip()
            print(f"brand {brand}\n description {name}\nprice {price}")
        except Exception as ex:
            print(ex)
            pass


if __name__ == "__main__":
    query = str(input('what would you like to search for? '))
    url = f'https://www.pigiame.co.ke/classifieds?q={query}'
    # url = f'https://www.jumia.co.ke/catalog/?q={query}'
    pigiame(url)