
from typing import List
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import time 

options = webdriver.ChromeOptions()
options.add_argument('--start-maximizad')
options.add_argument('--disable-estensions')

driver_path = './Webdriver/chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

home_link = "https://www.amazon.com/"

serch_article = "disco duro interno ssd".replace(" ","+")


driver.get(home_link+"s?k="+serch_article+"&__mk_es_US=ÅMÅŽÕÑ&crid=2KF9RH1YKNFPP&sprefix=disco+duro+interno+ssd%2Caps%2C125&ref=nb_sb_noss_1")

page = BeautifulSoup(driver.page_source,"html.parser")

itme_title = []
itme_link = []
itme_score = []
itme_review_number = []
itme_price = []
itme_price_before_sale = []
itme_envio_Gratis = []
itme_sponsored = []

pag_amount = 5

def item_confirm(item, item_append: List):
    if item:
        item_append.append(item.text)
    else:
        item_append.append(None)

def item_confirm_link(item, item_append: List):
    if item:
        item_append.append(item['href'])
    else:
        item_append.append(None)


def item_confirm_bool(item, item_append: List):
    if item:
        item_append.append(True)
    else:
        item_append.append(False)

for i in range(0, pag_amount):
    for item in page.findAll('div', attrs={'class':'s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16', 'data-component-type':'s-search-result'}):
        title = item.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
        item_confirm(title, itme_title)

        link = item.find('a', attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
        item_confirm_link(link, itme_link)

        score = item.find('span', attrs={'class':'a-icon-alt'})
        item_confirm(score, itme_score)


        review_number = item.find('span', attrs={'class':'a-size-base s-underline-text'})
        item_confirm(review_number, itme_review_number)
       

        price = item.find('span', attrs={'class':'a-price-whole'})
        price_decimal = item.find('span', attrs={'class':'a-price-fraction'})
        item_confirm(price,  itme_price)
        


        price_before_sale = item.find('span', attrs={'class':'a-offscreen'})
        item_confirm(price_before_sale, itme_price_before_sale)
        

        envio_Gratis = item.find('span', attrs={'class':'a-color-base a-text-bold'})
        item_confirm_bool(envio_Gratis, itme_envio_Gratis)
        

        sponsored = item.find('span', attrs={'class':'a-color-secondary'})
        item_confirm_bool(sponsored,  itme_sponsored)
        
    next_btn = driver.find_element(By.CSS_SELECTOR, '.s-pagination-item s-pagination-next s-pagination-button s-pagination-separator'.replace(' ', '.'))
    next_btn.click()
    time.sleep(2)
                                  

item_excel = pd.DataFrame({
    'TITLE': itme_title,
    'LINK':itme_link,
    'SCORE': itme_score,
    'REVIEW': itme_review_number,
    'PRICE': itme_price,
    'PRICE BEFORE SALE': itme_price_before_sale,
    'ENVIO GRATIS': itme_envio_Gratis,
    'SPONSORED': itme_sponsored
})
item_excel.to_csv(r'./Excel_datos/discos_durosn_ssd_Amazon.csv', index=None, header=True, encoding='utf-8-sig')

driver.quit()


