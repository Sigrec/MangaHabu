#Master scraping file that asks the user for input and what websites he wants to scrape and compares the data
from RightStufAnimeScrape import getRightStufAnimeData
from RobertsAnimeCornerStoreScrape import getRobertsAnimeCornerStoreData
from multiprocessing import Process
import time
import csv

def getRightStufData(userMemberStatus, userBookType, websites, userBookTitle):
    getRightStufAnimeData(userMemberStatus, userBookTitle, userBookType, 1)
    
def getRobertsData(websites, userBookTitle, bookType):
    getRobertsAnimeCornerStoreData(userBookTitle, bookType)

if __name__ == "__main__":
    websites = list(map(str, input(R"What Websites Do You want to Compare Data For: ").split()))
    userBookTitle = input(R"Enter Series Title: ")
    userBookType = input(R"Enter Book Type (LN or M): ")
    
    if "RS" in websites:
        userMemberStatus = input((R"Are You a GotAnime Member (T/True or F/False): "))
        Process(target = getRightStufData, args = (userMemberStatus, userBookType, websites, userBookTitle)).start()
    
    if "R" in websites:
        Process(target = getRobertsData, args = (websites, userBookTitle, userBookType)).start()

                        
            
                    