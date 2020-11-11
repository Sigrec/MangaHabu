#Scrapes the RightStufAnime website for a manga or light novel series and prints the stock stats, title, and current price

from msedge.selenium_tools import Edge, EdgeOptions
from bs4 import BeautifulSoup
from tabulate import tabulate
from natsort import natsorted
import re
import csv
import time

#Filters the users input title to create a valid url
def filterTitle(title):
    for char in ["'", "!", " "]: #Common non alphanumeric characters used in Light Novel & Manga titles
            if char in title:
                title = title.replace(char, "%" + hex(ord(char)).replace("0x", ""))
    return title

#Gets the URL for the Manga the user wants   
def getMangaURL(mangaTitle):
    mangaTitle = filterTitle(mangaTitle)
    mangaURL = R"https://www.rightstufanime.com/category/Manga?page={}&show=96&keywords={}".format(1, mangaTitle)
    print(mangaURL)
    return mangaURL

#Gets the URL to for the Light Novel the user wants
def getLightNovelURL(lightNovelTitle):
    lightNovelTitle = filterTitle(lightNovelTitle)
    lightNovelURL = R"https://www.rightstufanime.com/category/Novels?page={}&show=96&keywords={}".format(1, lightNovelTitle)
    print(lightNovelURL)
    return lightNovelURL


def getRSData(memberStatus, title, bookType):
    options = EdgeOptions()
    options.use_chromium = True
    driver = Edge(options=options)
    
    #Checks to see if whether to user is a GotAnime member
    if memberStatus in {"Y", "y", "Yes", "yes"}:
        memberBool = True
    elif memberStatus in {"N", "n", "No", "no"}:
        memberBool = False
    else:
        print("Error!!!! Invalid Membership Status Input")
        RightStufAnimeScrape()
        return
    
    #Ask the user whether they are looking for a LightNovel or Manga
    if bookType == "M": #Checks if the booktype is a manga
        driver.get(getMangaURL(title))
    elif bookType == "LN": #Checks if the book type is a Light Novel
       driver.get(getLightNovelURL(title))
    else:
        print("Invalid Book Type, must be a Manga (M) or Light Novel (LN)")
        RightStufAnimeScrape()
        return

    time.sleep(5) #Wait for the website to load before scraping
    
    #Parse the HTML to start scraping for data
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    #Get the Title, Price, and Stock Status Data of each Manga Volume
    titles = soup.find_all('span', {'itemprop' : 'name'})
    prices = soup.find_all('span', {'itemprop' : 'price'})
    stockStatus = soup.find_all('div', {'class' : 'product-line-stock-container'})
    #print(titles), #just a simple print to make sure data is actuall scraped
    
    if not titles: #Checks to see if the title given by user generates a url that has data
        print("Error!!! Invalid Title, Use English Title Variant w/ Approprate Spacing & Capitalization")
        RightStufAnimeScrape()
        return
    else: #Check to see if the users title input is formatted correctly
        website = "RightStufAnime"
        csvFile = website + "Data.csv"
        gotAnimeDiscount = 0.05 #5% Manga discount
        dataFile  = []
        
        with open (csvFile, "w", newline = "", encoding = "utf-8") as file:
            #Initialize the a CSV to write into w/ appropiate headers
            writeToFile = csv.writer(file)
            writeToFile.writerow(["Title", "Stock Status", "Price", "Website"])
            for stockStatus, fullTitle, price in zip(stockStatus, titles, prices): #get only the title and volume number for the series we are looking for
                if fullTitle.text.replace(" ", "").lower().find(title.replace(" ", "").lower()) != -1: #Fixes issue with capitilization
                    if memberBool: #Checks to see if the user is a member
                        priceVal = float(price.text[1:])
                        priceText = "$" + str(round((priceVal - (priceVal * gotAnimeDiscount)), 2)) #Add discount to price
                    dataFile.append([fullTitle.text, stockStatus.text, priceText, website])

            #Sort data by title and write to the file
            writeToFile.writerows(natsorted(dataFile)) 
    return csvFile

#Intitializes the script, change it so if type or status has a wrong input it only asks to redo that specific input
# and if the title has no url just ask for the title and save the type and status
def RightStufAnimeScrape():
    userMembershipStatus = input(R"Are You a GotAnime Member (Y/Yes or N/No): ")
    userBookType = input(R"Enter Book Type (LN or M): ")
    userBookTitle = input(R"Enter Manga Title: " if userBookType == "M" else "Enter Light Novel Title: ")          
    return getRSData(userMembershipStatus, userBookTitle, userBookType)

#Being Data Collection
RightStufAnimeScrape()