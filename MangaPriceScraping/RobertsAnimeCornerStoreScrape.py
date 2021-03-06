#

import string
import csv
import time
import re
from msedge.selenium_tools import Edge, EdgeOptions
from DataTableWidget import UI_DataTablesGUI
from bs4 import BeautifulSoup

#Gets the URLs needed to scrape the data from using the user input series title
def getURL(title, nextPage):
    #Maps all of the website URLs to there respective letters check RobertsAnimeCornerStore.txt
    urlMapDict = {
        "mangrapnovag": list(string.ascii_letters[0:2]),
        "mangrapnovhp": list(string.ascii_letters[2:4]),
        "mangrapnovqz": list(string.ascii_letters[4:7]),
        "magrnomo": list(string.ascii_letters[7:11]),
        "magrnops": list(string.ascii_letters[11:14]),
        "magrnotz": list(string.ascii_letters[14:17]),
        "magrnors": list(string.ascii_letters[17:19]),
        "magrnotv": list(string.ascii_letters[19:22]),
        "magrnowz": list(string.ascii_letters[22:26])
    }
    
    if not nextPage: #Gets the starting page based on first letter
        firstLetter = title[0]
        valueList = list(urlMapDict.values())
        for letters in valueList:
            if (firstLetter.lower() in ''.join(letters)) or (not firstLetter.isalpha()):
                url = R"https://www.animecornerstore.com/{}.html".format(list(urlMapDict.keys())[valueList.index(letters)])
                print(url)
                return url
    else: #Gets the actual page that houses the data that will be scraped from
        url = R"https://www.animecornerstore.com/{}".format(title)
        print(url)
        return url

#Removes spacing and lowercases all letters
def deParseString(title):
    return re.sub(r"\W+", "", title.lower()) 

def getDataPage(driver, title, soup, bookType):
    #Gets the page to find the URL to scrape the data
    driver.get(getURL(title, False))
        
    #Wait for the page to load
    time.sleep(5)
    
    #Initialize the HTML parser to grab elements and extract needed data
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    #Finds the correct url where the data will be scraped
    findSeries = soup.find_all("a", href=True)[1::2][:-19] #[1::2][:-19] Removes all none titles
    for series in findSeries:
        webPageTitle = deParseString(series.text)
        if deParseString(title) in deParseString(webPageTitle): #Checks to see if the series is being sold by the store
            if (bookType == "M") and ("graphic" in webPageTitle):
                return getURL(series["href"], True)
            elif (bookType == "LN") and (webPageTitle.find("graphic") == -1):
                return getURL(series["href"], True)

#Main logic function that uses the input and scrapes the data into a csv file
def getRobertsAnimeCornerStoreData(title, bookType):
    #Starts wevdriver to scrape edge chromium
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("-inprivate")
    options.add_argument("--headless")
    driver = Edge(options=options)
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    newPage = getDataPage(driver, title, soup, bookType)
    if not newPage:
        print(title)
        print("Error!!!!! Invalid Series Title")
        return
    else:
        #Start scraping the URL where the data is found
        driver.get(newPage)
        
        #Wait for the web page to finish loading
        time.sleep(5)
        
        #Start parsing the web pages html and css
        soup2 = BeautifulSoup(driver.page_source, "html.parser")
        
        #Get the Title and Price of each manga or light novel
        dataList, titleList = [], []
        titleParse = soup2.find_all("tr", {"valign" :"top"})[1:] #Remove first element cause it pulls unwanted text
        priceList = soup2.select('font[color="#ffcc33"]')[1::2] #[1::2] to remove the RACS Price text (every odd element in the list)
        
        #Convert title list to strings so you can remove any black/empyt spaces
        for bookTitle in titleParse:
            seriesTitle = bookTitle.find("font", {"size" : "2"}).b.text
            if seriesTitle != " ":
                titleList.append(seriesTitle)
        del titleParse #Remove list from memory as we don't need it anymore
        
        stockStatus = ""
        for titles, prices in zip(titleList, priceList):
            specTitle = str(titles).replace(",", "")
            if specTitle.find("Pre Order") != -1:
                stockStatus = "Pre-Order"
            else:
                stockStatus = "Available"
            dataList.append([specTitle, prices.text, stockStatus])

        csvFile = "AnimeCornerStore.csv"
        with open(csvFile, "w", newline = "", encoding = "utf-8") as file:
            writeToFile = csv.writer(file)
            writeToFile.writerow(["Title", "Price", "Stock Status"])
            writeToFile.writerows(dataList)
        #TableGUI.robertsDataTable.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(dataList[0])))
        return dataList
    