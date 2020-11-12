#Master scraping file that asks the user for input and what websites he wants to scrape and compares the data
from msedge.selenium_tools import Edge, EdgeOptions
from RightStufAnimeScrape import getRightStufAnimeData

#Starts wevdriver to scrape edge chromium
options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)

websites = list(map(str, input(R"What Websites Do You want to Compare Data For: ").split()))
userBookTitle = input(R"Enter Manga or Light Novel Title: ")

if "RS" in websites:
    userBookType = input(R"Enter Book Type (LN or M): ")
    userMembershipStatus = input((R"Are You a GotAnime Member (T/True or F/False): "))
    startingPageNum = 1
    RS_CSV_File = getRightStufAnimeData(driver, userMembershipStatus, userBookTitle, userBookType, startingPageNum)
    
driver.quit()