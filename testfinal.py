# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 00:08:29 2019

@author: Shashwat
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
products=[] #List to store name of the product
prices=[] #List to store price of the product
page = BeautifulSoup(requests.get(url).text, "lxml")
for a in page.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    products.append(name.text)
    prices.append(price.text) 
    
df = pd.DataFrame({'Product Name':products,'Price':prices}) 
df.to_csv('productspd.csv', index=False, encoding='utf-8')