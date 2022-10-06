from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import pandas as pd
from datetime import date 
import time 

options = webdriver.ChromeOptions()
options.add_argument('--start-maximizad')
options.add_argument('--disable-estensions')

driver_path = './Webdriver/chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

home_link = "https://www.ebay.com/"

serch_article = "discos ssd".replace(" ","+")


driver.get(home_link+'sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw='+serch_article+'&_sacat=0&LH_TitleDesc=0&loc=1003659&sitelnk=&poi=&cmpgn=6485254487&rlsatarget=kwd-297394422841&geo_id=&network=g&gclid=Cj0KCQjw4PKTBhD8ARIsAHChzRLasIoKOFzCCfnWHdzxO3RbLvnigLHcyKKuqLYp3PkwK5UCIw8yp9kaAm_dEALw_wcB&mkcid=2&_odkw=e+bay+motors.com.&norover=1&MT_ID=&adpos=&adgroupid=81878983910&matchtype=b&abcId=&keyword=e+bay+motors.com.&mkrid=711-163588-2056-0&crlp=496209241109_&device=c')

page = BeautifulSoup(driver.page_source,"html.parser")


bloque = page.find('li', attrs={'class': 's-item s-item__pl-on-bottom', 'data-view':True})
print(bloque)
# bloque = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div/div/div[2]/div')
# print(bloque.text) 