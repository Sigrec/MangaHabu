#Scrapes the RightStufAnime website for a manga or light novel series and prints the stock stats, title, and current price

from msedge.selenium_tools import Edge, EdgeOptions
from bs4 import BeautifulSoup
from tabulate import tabulate
from natsort import natsorted
import re
import csv
import time

#Starts wevdriver to scrape edge chromium
options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)

#Filters the users input title to create a valid url
def filterTitle(title):
    for char in ["'", "!", " "]: #Common non alphanumeric characters used in Light Novel & Manga titles
            if char in title:
                title = title.replace(char, "%" + hex(ord(char)).replace("0x", ""))
    return title

#Gets the URL for the Manga the user wants   
def getMangaURL(mangaTitle, currPageNum):
    mangaTitle = filterTitle(mangaTitle)
    mangaURL = R"https://www.rightstufanime.com/category/Manga?page={}&show=96&keywords={}".format(currPageNum, mangaTitle)
    print(mangaURL)
    return mangaURL

#Gets the URL to for the Light Novel the user wants
def getLightNovelURL(lightNovelTitle, currPageNum):
    lightNovelTitle = filterTitle(lightNovelTitle)
    lightNovelURL = R"https://www.rightstufanime.com/category/Novels?page={}&show=96&keywords={}".format(currPageNum, lightNovelTitle)
    print(lightNovelURL)
    return lightNovelURL

#Checks to see if there are multiple pages to scrape
def paginationCheck(memberStatus, title, bookType, nextPage, currPageNum):
    if nextPage == None: #Checks to to see if the button to go to a proceeding page is there
        return
    else: #If there is another page to scrape increment the page to the next page and get the data
        currPageNum += 1
        getRSData(memberStatus, title, bookType, currPageNum)

#Check to see if the user inputted a correct book type    
def checkUserTypeInput(title, bookType, currPageNum):
    if bookType in {"M", "m" "Manga", "manga"}: #Checks if the booktype is a manga
        pageURL = getMangaURL(title, str(currPageNum))
    elif bookType in {"LN", "ln", "Light Novel", "lightnovel", "LightNovel", "light novel"}: #Checks if the book type is a Light Novel
        pageURL = getLightNovelURL(title, str(currPageNum))
    else:
        print("Invalid Book Type, must be a Manga (M) or Light Novel (LN)")
        RightStufAnimeScrape()
        return
    return pageURL

#Checks to see if whether to user is a GotAnime member
def checkUserMemberInput(memberStatus, bookType):
    if memberStatus in {"Y", "y", "Yes", "yes"}:
        memberBool = True
    elif memberStatus in {"N", "n", "No", "no"}:
        memberBool = False
    else:
        print("Error!!!! Invalid Membership Status Input")
        RightStufAnimeScrape()
        return
    return memberBool

#Main logic function that does all the scraping and formats data into a csv
def getRSData(memberStatus, title, bookType, currPageNum):
    pageURL = checkUserTypeInput(title, bookType, currPageNum)
    driver.get(pageURL)
    time.sleep(10) #Wait for the website to load before scraping

    #Parse the HTML to start scraping for data
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    #Checks if there is another page to scrape
    nextPage = soup.find("li", {"class" : "global-views-pagination-next"})
    paginationCheck(memberStatus, title, bookType, nextPage, currPageNum)
    
    #Get the Title, Price, and Stock Status Data of each Manga Volume
    titleList.extend(soup.find_all("span", {"itemprop" : "name"}))
    priceList.extend(soup.find_all("span", {"itemprop" : "price"}))
    stockStatusList.extend(soup.find_all("div", {"class" : "product-line-stock-container"}))

    #Check to see if the title given by the user generates a valid URL for RightStufAnime
    if not titleList:
        print("Error!!! Invalid Title, Use English Title Variant w/ Approprate Spacing & Capitalization")
        RightStufAnimeScrape()
        return
    else: #If the URL is a "valid"
        websiteName = "RightStufAnime"
        gotAnimeDiscount = 0.05 #5% Manga discount
        dataFile = []
        
        for fullTitle, price, stockStatus in zip(titleList, priceList, stockStatusList): #get only the title and volume number for the series we are looking for
            if fullTitle.text.replace(" ", "").lower().find(title.replace(" ", "").lower()) != -1: #Fixes issue with capitilization
                if memberStatus: #If user is a member add discount
                    priceVal = float(price.text[1:])
                    priceText = "$" + str(round((priceVal - (priceVal * gotAnimeDiscount)), 2)) #Add discount
                else:
                    priceText = price.text
                dataFile.append([fullTitle.text, stockStatus.text, priceText, websiteName])
        #print(natsorted(dataFile))
        
        csvFile = websiteName + "Data.csv"
        with open (csvFile, "w", newline = "", encoding = "utf-8") as file:
            #Initialize the a CSV to write into w/ appropiate headers
            writeToFile = csv.writer(file)
            writeToFile.writerow(["Title", "Stock Status", "Price", "Website"])
            writeToFile.writerows(natsorted(dataFile)) #Sort data by title and write to the file        
    return csvFile

#Intitializes the script, change it so if type or status has a wrong input it only asks to redo that specific input
# and if the title has no url just ask for the title and save the type and status
def RightStufAnimeScrape():
    userMembershipStatus = input(R"Are You a GotAnime Member (Y/Yes or N/No): ")
    userBookType = input(R"Enter Book Type (LN or M): ")
    userBookTitle = input(R"Enter Manga Title: " if userBookType == "M" else "Enter Light Novel Title: ")
    startingPageNum = 1
    memberStatus = checkUserMemberInput(userMembershipStatus, userBookType)
    return getRSData(memberStatus, userBookTitle, userBookType, startingPageNum)

#Being Data Collection
titleList, priceList, stockStatusList = [], [], []
RightStufAnimeScrape()