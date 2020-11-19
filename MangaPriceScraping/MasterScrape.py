from RightStufAnimeScrape import getRightStufAnimeData
from RobertsAnimeCornerStoreScrape import getRobertsAnimeCornerStoreData
from multiprocessing import Process

#Gets the data from the RightStufAnime website
def getRightStufData(userMemberStatus, userBookType, userBookTitle):
    getRightStufAnimeData(userMemberStatus, userBookTitle, userBookType, 1)

#Get the data from Robert's Anime Corner Store website  
def getRobertsData(userBookTitle, bookType):
    getRobertsAnimeCornerStoreData(userBookTitle, bookType)

#Gets the price data from the websites the user wants
def getPriceData(gotAnimeMemberStatus, userBookTitle, userBookType, websiteList):
    if "RS" in websiteList:
        proc1 = Process(target = getRightStufData, args = (gotAnimeMemberStatus, userBookType, userBookTitle))
        proc1.start()
    
    if "R" in websiteList:
        proc2 = Process(target = getRobertsData, args = (userBookTitle, userBookType))
        proc2.start()