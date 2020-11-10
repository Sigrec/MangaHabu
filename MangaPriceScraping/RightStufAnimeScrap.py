from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
import re
import codecs

#Generate RightStufAnime URL based on the title of the manga

def filterMangaTitle(mangaTitle):
    mangaTitle = mangaTitle.replace(" ", "")
    for char in ['\'', '!']:
        if char in mangaTitle:
            mangaTitle = mangaTitle.replace(char, "%" + hex(ord(char))).replace("0x", "")
    return mangaTitle
            
def getMangaURL(mangaTitle):
    mangaTitle = filterMangaTitle(mangaTitle)
    url = R"https://www.rightstufanime.com/category/Manga?order=custitem_rs_release_date:asc&show=96&keywords={}".format(mangaTitle)
    print(url)
    return url


def getRSPrice(mangaTitle):
    #Hard-coded path
    #PATH = "Some Path"
    options = EdgeOptions()
    options.use_chromium = True
    driver = Edge(options=options)
    
    driver.get(getMangaURL(mangaTitle))
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    #Get the Title and Price Data of each Manga Volume
    titleData = soup.find_all('span', {'itemprop' : 'name'})
    priceData = soup.find_all('span', {'itemprop' : 'price'})
    
    for title, price in zip(titleData, priceData): #get only the title and volume number for the series we are looking for
        if mangaTitle.lower() in title.text.lower(): #Check to see if the series's title is present
            print(title.text + '    ' + price.text)
            
getRSPrice(input("Enter Manga Title: "))