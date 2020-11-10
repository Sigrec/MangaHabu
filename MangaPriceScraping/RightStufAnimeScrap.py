from msedge.selenium_tools import Edge, EdgeOptions
from selenium import webdriver
import csv

#Hard-coded path
#PATH = r"C:\Users\seani\Python\edgedriver_win32\msedgedriver.exe"
options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)

#Generate RightStufAnime URL based on the title of the manga
def getMangaURL(title):
    title = title.replace(" ", "").replace("*", "")
    template = r"https://www.rightstufanime.com/category/Manga?show=96&keywords={}"
    return template.format(title)

#Gets the title the manga series the user wants to scrap for prices
def launchPage():
    mangaTitle = input("Enter Manga Title: ")
    url = getMangaURL(mangaTitle)
    print(url)
    driver.get(url)
    while(True):
        pass
    
launchPage()

# soup = BeautifulSoup(driver.page_source, 'html.parser')
# results = soup.find_all('span', {'itemprop': 'name'})
# len(results)