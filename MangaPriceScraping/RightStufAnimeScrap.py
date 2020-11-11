#Scraps the RightStufAnime website for a manga or light novel series and prints the stock stats, title, and current price

from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from tabulate import tabulate
import csv
import json
import time

def filterTitle(title):
    #title = title.replace(" ", "")
    for char in ["'", "!", " "]:
        if char in title:
            title = title.replace(char, "%" + hex(ord(char))).replace("0x", "")
    return title

#Gets the URL for the Manga the user wants   
def getMangaURL(mangaTitle):
    mangaTitle = filterTitle(mangaTitle)
    mangaURL = R"https://www.rightstufanime.com/category/Manga?page=1&order=custitem_rs_release_date:asc&show=96&keywords={}".format(mangaTitle)
    print(mangaURL)
    return mangaURL

#Gets the URL to for the Light Novel the user wants
def getLightNovelURL(lightNovelTitle):
    lightNovelTitle = filterTitle(lightNovelTitle)
    lightNovelURL = R"https://www.rightstufanime.com/category/Novels?page=1&order=custitem_rs_release_date:asc&show=96&keywords={}".format(lightNovelTitle)
    print(lightNovelURL)
    return lightNovelURL

# def pagination():
#     page = driver.find_element_by_link_text

    
def getRSPrice(title, bookType):
    options = EdgeOptions()
    options.use_chromium = True
    driver = Edge(options=options)
    
    #Ask the user whether they are looking for a LightNovel or Manga
    if bookType == "M": #Checks if the booktype is a manga
        url = getMangaURL(title)
    elif bookType == "LN": #Checks if the book type is a Light Novel
        url = getLightNovelURL(title)
    else:
        print("Invalid Book Type, must be a Manga (M) or Light Novel (LN)")
        return

    driver.get(url)
    time.sleep(5)
    
    #Parse the HTML to start scraping for data
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    #Get the Title, Price, and Stock Status Data of each Manga Volume
    titles = soup.find_all('span', {'itemprop' : 'name'})
    prices = soup.find_all('span', {'itemprop' : 'price'})
    stockStatus = soup.find_all('div', {'class' : 'product-line-stock-container'})
    #print(titleData)
    
    with open ("results.csv", "w", newline = "", encoding = "utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Stock Status", "Price"])
        for stockStatus, fullTitle, price in zip(stockStatus, titles, prices): #get only the title and volume number for the series we are looking for
            if title in fullTitle.text: #Only get the data for the series the user wants
                writer.writerow([fullTitle.text, stockStatus.text, price.text])
            

#Get the book type and title from the user to find data for      
userBookType = input("Enter Book Type (LN or M): ")
userBookTitle = input("Enter Manga Title: " if userBookType == "M" else "Enter Light Novel Title: ")          
getRSPrice(userBookTitle, userBookType)