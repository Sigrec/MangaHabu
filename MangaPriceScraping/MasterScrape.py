#Master scraping file that asks the user for input and what websites he wants to scrape and compares the data
from RightStufAnimeScrape import getRightStufAnimeData
from RobertsAnimeCornerStoreScrape import getRobertsAnimeCornerStoreData
from multiprocessing import Process
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup, QGroupBox
import sys
import time
import csv

websiteList = []
count = 0
exitCode1, exitCode2 = 1, 1

#Gets the data from the RightStufAnime website
def getRightStufData(userMemberStatus, userBookType, userBookTitle):
    getRightStufAnimeData(userMemberStatus, userBookTitle, userBookType, 1)

#Get the data from Robert's Anime Corner Store website  
def getRobertsData(userBookTitle, bookType):
    getRobertsAnimeCornerStoreData(userBookTitle, bookType)
    
def getPriceData(userBookTitle, userBookType):
    global count
    global exitCode1
    global exitCode2
    # websites = list(map(str, input(R"What Websites Do You want to Compare Data For: ").split()))
    # userBookTitle = input(R"Enter Series Title: ")
    # userBookType = input(R"Enter Book Type (LN or M): ")
    
    if "RS" in websiteList:
        #userMemberStatus = input((R"Are You a GotAnime Member (T/True or F/False): "))
        proc1 = Process(target = getRightStufData, args = (False, userBookType, userBookTitle))
        proc1.start()
        exitCode1 = proc1.exitcode
    
    if "R" in websiteList:
        proc2 = Process(target = getRobertsData, args = (userBookTitle, userBookType))
        proc2.start()
        exitCode2 = proc2.exitcode
        
class Ui_MangaScrapeGUI(object):
    def setupUi(self, MangaScrapeGUI):
        MangaScrapeGUI.setObjectName("MangaScrapeGUI")
        MangaScrapeGUI.resize(319, 230)
        MangaScrapeGUI.setMinimumSize(QtCore.QSize(319, 230))
        MangaScrapeGUI.setMaximumSize(QtCore.QSize(319, 270))
        MangaScrapeGUI.setAutoFillBackground(False)
        
        self.MangaScrapeWidget = QtWidgets.QWidget(MangaScrapeGUI)
        self.MangaScrapeWidget.setEnabled(True)
        self.MangaScrapeWidget.setMinimumSize(QtCore.QSize(319, 250))
        self.MangaScrapeWidget.setMaximumSize(QtCore.QSize(319, 250))
        self.MangaScrapeWidget.setMouseTracking(True)
        self.MangaScrapeWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.MangaScrapeWidget.setAcceptDrops(False)
        self.MangaScrapeWidget.setAccessibleName("")
        
        self.MangaScrapeWidget.setObjectName("MangaScrapeWidget")
        self.seriesTitleLabel = QtWidgets.QLabel(self.MangaScrapeWidget)
        self.seriesTitleLabel.setGeometry(QtCore.QRect(20, 10, 231, 16))
        self.seriesTitleLabel.setObjectName("seriesTitleLabel")
        
        self.seriesTitleInput = QtWidgets.QLineEdit(self.MangaScrapeWidget)
        self.seriesTitleInput.setGeometry(QtCore.QRect(20, 30, 281, 20))
        self.seriesTitleInput.setText("")
        self.seriesTitleInput.setObjectName("seriesTitleInput")
        
        self.bookType = ""
        self.bookTypeMangaButton = QtWidgets.QPushButton(self.MangaScrapeWidget)
        self.bookTypeMangaButton.setGeometry(QtCore.QRect(50, 70, 101, 31))
        self.bookTypeMangaButton.setCheckable(True)
        self.bookTypeMangaButton.setObjectName("bookTypeMangaButton")
        
        self.bookTypeNovelButton = QtWidgets.QPushButton(self.MangaScrapeWidget)
        self.bookTypeNovelButton.setGeometry(QtCore.QRect(170, 70, 91, 31))
        self.bookTypeNovelButton.setCheckable(True)
        self.bookTypeNovelButton.setObjectName("bookTypeNovelButton")
        
        self.groupBookTypeButtons = QButtonGroup()
        self.groupBookTypeButtons.setExclusive(True)
        self.groupBookTypeButtons.addButton(self.bookTypeMangaButton)
        self.groupBookTypeButtons.addButton(self.bookTypeNovelButton)
        self.groupBookTypeButtons.buttonClicked.connect(self.getBookType)
        
        self.rightstufCheckBox = QtWidgets.QCheckBox(self.MangaScrapeWidget)
        self.rightstufCheckBox.setGeometry(QtCore.QRect(30, 120, 101, 17))
        self.rightstufCheckBox.setObjectName("rightstufCheckBox")
        self.rightstufCheckBox.stateChanged.connect(self.getRSWebsite)
        
        self.robertsCheckBox = QtWidgets.QCheckBox(self.MangaScrapeWidget)
        self.robertsCheckBox.setGeometry(QtCore.QRect(140, 120, 161, 17))
        self.robertsCheckBox.setObjectName("robertsCheckBox")
        self.robertsCheckBox.stateChanged.connect(self.getRobertWebsite)
        
        exeTime = 0
        self.progressBar = QtWidgets.QProgressBar(self.MangaScrapeWidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 190, 121, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        
        self.runScrape = QtWidgets.QPushButton(self.MangaScrapeWidget)
        self.runScrape.setGeometry(QtCore.QRect(140, 150, 41, 31))
        self.runScrape.setObjectName("pushbutton")
        MangaScrapeGUI.setCentralWidget(self.MangaScrapeWidget)
        self.runScrape.clicked.connect(self.getPrices)
        #self.runScrape.clicked.connect(self.progressBarUpdate)
        
        self.statusbar = QtWidgets.QStatusBar(MangaScrapeGUI)
        self.statusbar.setObjectName("statusbar")
        MangaScrapeGUI.setStatusBar(self.statusbar)

        self.retranslateUi(MangaScrapeGUI)
        QtCore.QMetaObject.connectSlotsByName(MangaScrapeGUI)

    def retranslateUi(self, MangaScrapeGUI):
        _translate = QtCore.QCoreApplication.translate
        MangaScrapeGUI.setWindowTitle(_translate("MangaScrapeGUI", "Manga Scrape"))
        self.seriesTitleLabel.setText(_translate("MangaScrapeGUI", "Enter Series Title Below:"))
        self.bookTypeMangaButton.setText(_translate("MangaScrapeGUI", "Manga"))
        self.bookTypeNovelButton.setText(_translate("MangaScrapeGUI", "Light Novel"))
        self.rightstufCheckBox.setText(_translate("MangaScrapeGUI", "RightStufAnime"))
        self.robertsCheckBox.setText(_translate("MangaScrapeGUI", "Roberts Anime Corner Store"))
        self.progressBar.setFormat(_translate("MangaScrapeGUI", "%p%"))
        self.runScrape.setText(_translate("MangaScrapeGUI", "Run"))
    
    def getBookType(self, button):
        if button.text() == "Light Novel":
            self.bookType = "LN"
        elif button.text() == "Manga":
            self.bookType = "M"
    
    def getRSWebsite(self):
        if  self.rightstufCheckBox.isChecked():
            websiteList.append("RS")
        elif not self.rightstufCheckBox.isChecked():
            websiteList.remove("RS")
        
    def getRobertWebsite(self):
        if self.robertsCheckBox.isChecked():
            websiteList.append("R")
        elif not self.robertsCheckBox.isChecked():
            websiteList.remove("R")
            
    def getPrices(self):
        if (len(self.bookType) == 0) or (not self.seriesTitleInput.text()) or (websiteList == []):
            print("Error!!!")
        else:
            self.runScrape.setCheckable(True)
            getPriceData(self.seriesTitleInput.text(), self.bookType)
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MangaScrapeGUI = QtWidgets.QMainWindow()
    ui = Ui_MangaScrapeGUI()
    ui.setupUi(MangaScrapeGUI)
    MangaScrapeGUI.show()
    sys.exit(app.exec_())
    
          
            
                    