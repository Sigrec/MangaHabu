#Master scraping file that asks the user for input and what websites he wants to scrape and compares the data
from RightStufAnimeScrape import getRightStufAnimeData
from RobertsAnimeCornerStoreScrape import getRobertsAnimeCornerStoreData
from multiprocessing import Process, Pool
import time

def getRightStufData(userMemberStatus, userBookType, dataFileNames, websites, userBookTitle):
    dataFileNames.append(getRightStufAnimeData(userMemberStatus, userBookTitle, userBookType, 1))
    
def getRobertsData(dataFileNames, websites, userBookTitle):
    if "R" in websites:
        dataFileNames.append(getRobertsAnimeCornerStoreData(userBookTitle))

if __name__ == "__main__":
    dataFileNames = []
    file = open("ExeTime.txt", "w")
    
    websites = list(map(str, input(R"What Websites Do You want to Compare Data For: ").split()))
    userBookTitle = input(R"Enter Manga or Light Novel Title: ")
    
    if "RS" in websites:
        userBookType = input(R"Enter Book Type (LN or M): ")
        userMemberStatus = input((R"Are You a GotAnime Member (T/True or F/False): "))
        Process(target = getRightStufData, args = (userMemberStatus, userBookType, dataFileNames, websites, userBookTitle)).start()
    
    Process(target = getRobertsData, args = (dataFileNames, websites, userBookTitle,)).start()


    