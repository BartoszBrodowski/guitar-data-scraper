import time
import uuid
from selenium import webdriver
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class Guitar:
    id: str
    name: str
    manufacturer: str
    type: str
    price: str
    img: str
    url: str

class Scraper():
    def __init__(self, link):
        self.link = link
    def connect(self):
        self.driver = webdriver.Chrome()

        self.driver.get(self.link)
        time.sleep(5)
    
    def _get_soup(self):
        dynamic_page = self.driver.page_source
        self.driver.quit()

        return BeautifulSoup(dynamic_page, 'html.parser')

    def parse_guitars(self, guitar_type):
        soup = self._get_soup()
        data_element = soup.find('div', class_='product-listings')
        if data_element:
            list_entries = data_element.select('div.fx-product-list-entry')
            tags = data_element.find('div', class_='fx-overlay-loading fx-overlay-loading--top')
            list_entries = tags.find_all('div', class_='fx-product-list-entry')
            results = [Guitar (
                    id=str(uuid.uuid4()),
                    name=tag.find('span', class_='title__name').text,
                    manufacturer=tag.find('span', class_='title__manufacturer').text.strip(),
                    type=guitar_type,
                    price=tag.find('span', class_='fx-typography-price-primary').text,
                    img=tag.find('img')['src'],
                    url='https://www.thomann.de/gb/' + tag.find('a', class_='product__content')['href']
                ) for tag in list_entries]
        
            return results
        else:
            print('Dynamic data not found')
