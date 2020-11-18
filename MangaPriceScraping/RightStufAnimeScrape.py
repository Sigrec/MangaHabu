#Scrapes the RightStufAnime website for a manga or light novel series and prints the stock stats, title, and current price

from msedge.selenium_tools import Edge, EdgeOptions
from bs4 import BeautifulSoup
from natsort import natsorted
import string
import csv
import re
import time

#Empty list that holds final data
dataFile = []

#Checks to see if whether to user is a GotAnime member
def checkMembershipStatus(membershipStatus):
    if membershipStatus in {"T", "True"}:
        memberBool = True
    elif membershipStatus in {"F", "False"}:
        memberBool = False
    else:
        print("Error!!!! Invalid Membership Status Input")
    return memberBool

#Checks to see whether the user inputted a valid book type and if valid return the type
def checkBookType(bookType):
    if bookType in {"M", "Manga"}:
        bookType = "Manga"
    elif bookType in {"LN", "Light Novel"}:
        bookType = "Novels"
    else:
        print("Invalid Book Type, must be a Manga (M) or Light Novel (LN)")
    return bookType

#Converts the title give n into a valid string that will create a valid url for RightStu
def filterTitle(bookTitle):
    for char in [" ", "'", "!", "-"]: #Common non alphanumeric characters used in Light Novel & Manga titles
        if char in bookTitle:
            bookTitle = bookTitle.replace(char, "%" + hex(ord(char)).replace("0x", ""))
    return bookTitle

#Gets the URL to for the Light Novel or Manga the user wants
def getPageURL(bookType, currPageNum, bookTitle):
    pageURL = R"https://www.rightstufanime.com/category/{}?page={}&show=96&keywords={}".format(checkBookType(bookType), currPageNum, filterTitle(bookTitle))
    print(pageURL)
    return pageURL

#Removes spacing and lowercases all letters
def deParseString(title):
    return re.sub(r"\W+", "", title.lower()) 

#Main logic function that does all the scraping and formats data into a csv
def getRightStufAnimeData(memberStatus, title, bookType, currPageNum):
    #Starts wevdriver to scrape edge chromium
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("-inprivate")
    options.add_argument("--headless")
    driver = Edge(options=options)
    
    #Create a empty list for all the data types we want to track
    titleList, priceList, stockStatusList = [], [], []

    #Get the URL for the page we are going to scrape for data
    driver.get(getPageURL(bookType, currPageNum, title))
    
    #Need to wait so the website can finish loading
    time.sleep(5)

    #Parse the HTML to start scraping for data
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    #Get the Title, Price, and Stock Status Data of each Manga Volume and whether or not next page button exists
    titleList = soup.find_all("span", {"itemprop" : "name"})
    priceList = soup.find_all("span", {"itemprop" : "price"})
    stockStatusList = soup.find_all("div", {"class" : "product-line-stock-container"})
    nextPageButton = soup.find("li", {"class" : "global-views-pagination-next"})
    
    #Check to see if the title given by the user generates a valid URL for RightStufAnime
    if not titleList:
        print("Error!!! Invalid Title, Use English Title Variant w/ Appropriate Spacing & Capitalization")
        return
    else: #If the URL is a "valid" RightStufAnime website URL
        websiteName = "RightStufAnime"
        gotAnimeDiscount = 0.05 #5% Manga discount
        
        #Format data into a single list
        for fullTitle, price, stockStatus in zip(titleList, priceList, stockStatusList): #get only the title and volume number for the series we are looking for
            if deParseString(title) in deParseString(fullTitle.text): #Fixes issue with capitilization
                if memberStatus: #If user is a member add discount
                    priceVal = float(price.text[1:])
                    priceText = "$" + str(round((priceVal - (priceVal * gotAnimeDiscount)), 2)) #Add discount
                else:
                    priceText = price.text
                
                stockCheck = stockStatus.text
                if stockCheck.find("Out of Stock") != -1:
                    stockCheck = "OOS"
                elif stockCheck.find("No Longer Available") != -1:
                    stockCheck = "OOP"
                else:
                    stockCheck = "Available"
                dataFile.append([fullTitle.text, priceText, stockCheck])
                
        #Check to see if there is another page
        if nextPageButton != None:
            currPageNum += 1
            print(title)
            getRightStufAnimeData(memberStatus, title, bookType, currPageNum)
    
    #Initialize the a CSV to write into w/ appropiate headers
    csvFile = websiteName + "Data.csv"
    with open (csvFile, "w", newline = "", encoding = "utf-8") as file:
        writeToFile = csv.writer(file)
        writeToFile.writerow(["Title", "Price", "Stock Status"])
        writeToFile.writerows(natsorted(dataFile)) #Sort data by title and write to the file
    driver.quit()
    return csvFile
