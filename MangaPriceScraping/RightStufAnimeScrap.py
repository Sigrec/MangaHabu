from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from tabulate import tabulate
import csv
import json
import time

#Scraps the RightStufAnime website for a manga or light novel series and prints the stock stats, title, and current price

def filterTitle(title):
    #title = title.replace(" ", "")
    for char in ["'", "!", " "]:
        if char in title:
            title = title.replace(char, "%" + hex(ord(char))).replace("0x", "")
    return title
            
def getMangaURL(mangaTitle):
    mangaTitle = filterTitle(mangaTitle)
    mangaURL = R"https://www.rightstufanime.com/category/Manga?order=custitem_rs_release_date:asc&show=96&keywords={}".format(mangaTitle)
    # print(mangaURL)
    return mangaURL

def getLightNovelURL(lightNovelTitle):
    lightNovelTitle = filterTitle(lightNovelTitle)
    lightNovelURL = R"https://www.rightstufanime.com/category/Novels?order=custitem_rs_release_date:asc&show=96&keywords={}".format(lightNovelTitle)
    # print(lightNovelURL)
    return lightNovelURL


def getRSPrice(title, bookType):
    options = EdgeOptions()
    options.use_chromium = True
    driver = Edge(options=options)
    
    #print("BookType Test: " + bookType + "\n Title Test: " + title)
    
    #Ask the user whether they are looking for a LightNovel or Manga
    if bookType == "M": #Checks if the booktype is a manga
        url = getMangaURL(title)
    elif bookType == "LN": #Checks if the book type is a Light Novel
        url = getLightNovelURL(title)
    else:
        print("Invalid Book Type, must be a Manga (M) or Light Novel (LN)")
        return
    
    #Parse the HTML to start scraping for data
    print(url)
    driver.get(url)
    time.sleep(10) #Takes a little whiel to load the page so need to wait until it's done loading before scraping
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    #Get the Title, Price, and Stock Status Data of each Manga Volume
    titleData = soup.find_all('span', {'itemprop' : 'name'})
    priceData = soup.find_all('span', {'itemprop' : 'price'})
    stockStatusData = soup.find_all('div', {'class' : 'product-line-stock-container'})
    #print(titleData)
    
    for stockStatus, fullTitle, price in zip(stockStatusData, titleData, priceData): #get only the title and volume number for the series we are looking for
        if title in fullTitle.text: #Only get the data for the series the user wants
            print(stockStatus.text + "  " + fullTitle.text + "  " + price.text)
    

#Get the book type and title from the user to find data for      
userBookType = input("Enter Book Type (LN or M): ")
userBookTitle = input("Enter Manga Title: " if userBookType == "M" else "Enter Light Novel Title: ")          
getRSPrice(userBookTitle, userBookType)