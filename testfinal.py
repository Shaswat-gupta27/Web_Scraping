# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 00:08:29 2019

@author: Shashwat
"""

from bs4 import BeautifulSoup #Library used for web scraping
import requests #Library used to request url
import pandas as pd #Library used for mantain dataframe

url = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off" #calls the specific url
products=[] #List to store name of the product
prices=[] #List to store price of the product
page = BeautifulSoup(requests.get(url).text, "lxml")              #page method will be created which will request url and use it for web scraping
for a in page.findAll('a',href=True, attrs={'class':'_31qSD5'}):  #this loop will find all the products on the page
    name=a.find('div', attrs={'class':'_3wU53n'})                 #this will store product name 
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})        #this will store product price
    products.append(name.text)                                    #this will append name in products list
    prices.append(price.text)                                     #this will append price in prices list
    
df = pd.DataFrame({'Product Name':products,'Price':prices}) #A dataframe having products and prices list is created
df.to_csv('productspd.csv', index=False, encoding='utf-8')  #The dataframe is converted into .csv file
