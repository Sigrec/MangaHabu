#Master scraping file that asks the user for input and what websites he wants to scrape and compares the data
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QButtonGroup, QGroupBox
from PyQt5.QtGui import QFont
from DataTableWidget import UI_DataTablesGUI
from MasterScrape import getPriceData
import sys
        
class Ui_MangaScrapeGUI(object):
    def setupUi(self, MangaScrapeGUI):
        MangaScrapeGUI.setObjectName("MangaScrapeGUI")
        MangaScrapeGUI.resize(319, 230)
        MangaScrapeGUI.setMinimumSize(QtCore.QSize(319, 230))
        MangaScrapeGUI.setMaximumSize(QtCore.QSize(319, 230))
        MangaScrapeGUI.setAutoFillBackground(False)
        
        self.MangaScrapeWidget = QtWidgets.QWidget(MangaScrapeGUI)
        self.MangaScrapeWidget.setEnabled(True)
        self.MangaScrapeWidget.setMinimumSize(QtCore.QSize(319, 250))
        self.MangaScrapeWidget.setMaximumSize(QtCore.QSize(319, 250))
        self.MangaScrapeWidget.setMouseTracking(True)
        self.MangaScrapeWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.MangaScrapeWidget.setAcceptDrops(False)
        self.MangaScrapeWidget.setAccessibleName("")
        self.MangaScrapeWidget.setFont(QFont('Arial', 8)) 
        self.MangaScrapeWidget.setObjectName("MangaScrapeWidget")
        
        self.seriesTitleLabel = QtWidgets.QLabel(self.MangaScrapeWidget)
        self.seriesTitleLabel.setGeometry(QtCore.QRect(20, 10, 231, 16))
        self.seriesTitleLabel.setObjectName("seriesTitleLabel")
        
        self.seriesTitleInput = QtWidgets.QLineEdit(self.MangaScrapeWidget)
        self.seriesTitleInput.setGeometry(QtCore.QRect(20, 30, 281, 20))
        self.seriesTitleInput.setPlaceholderText("Series Title...")
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
        
        self.websiteList = []
        self.rightstufCheckBox = QtWidgets.QCheckBox(self.MangaScrapeWidget)
        self.rightstufCheckBox.setGeometry(QtCore.QRect(30, 120, 101, 17))
        self.rightstufCheckBox.setObjectName("rightstufCheckBox")
        self.rightstufCheckBox.stateChanged.connect(self.getRSWebsite)
        
        self.memberStatus = False
        self.gotAnimeMemberStatus = QtWidgets.QCheckBox(self.MangaScrapeWidget)
        self.gotAnimeMemberStatus.setGeometry(QtCore.QRect(100, 145, 140, 17))
        self.gotAnimeMemberStatus.setObjectName("gotAnimeMemberStatus")
        self.gotAnimeMemberStatus.stateChanged.connect(self.getMemberStatus)
        self.gotAnimeMemberStatus.hide()
        
        self.robertsCheckBox = QtWidgets.QCheckBox(self.MangaScrapeWidget)
        self.robertsCheckBox.setGeometry(QtCore.QRect(140, 120, 161, 17))
        self.robertsCheckBox.setObjectName("robertsCheckBox")
        self.robertsCheckBox.stateChanged.connect(self.getRobertWebsite)
    
        self.progressBar = QtWidgets.QProgressBar(self.MangaScrapeWidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 190, 121, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        
        self.runScrape = QtWidgets.QPushButton(self.MangaScrapeWidget)
        self.runScrape.setGeometry(QtCore.QRect(115, 150, 41, 31))
        self.runScrape.setObjectName("pushButton")
        MangaScrapeGUI.setCentralWidget(self.MangaScrapeWidget)
        self.runScrape.clicked.connect(self.getPrices)
        #self.runScrape.clicked.connect(self.printData)
        
        self.printDataButton = QtWidgets.QPushButton(self.MangaScrapeWidget)
        self.printDataButton.setGeometry(QtCore.QRect(165, 150, 41, 31))
        self.printDataButton.setObjectName("printDataButton")
        MangaScrapeGUI.setCentralWidget(self.MangaScrapeWidget)
        self.printDataButton.clicked.connect(self.printData)
        
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
        self.gotAnimeMemberStatus.setText(_translate("MangaScrapeGUI", "GotAnime Member"))
        self.robertsCheckBox.setText(_translate("MangaScrapeGUI", "Roberts Anime Corner Store"))
        self.progressBar.setFormat(_translate("MangaScrapeGUI", "%p%"))
        self.runScrape.setText(_translate("MangaScrapeGUI", "Run"))
        self.printDataButton.setText(_translate("MangaScrapeGUI", "Show"))
    
    #Determines the book type (manga or light novel) the user wants data for
    def getBookType(self, button):
        if button.text() == "Light Novel":
            self.bookType = "LN"
        elif button.text() == "Manga":
            self.bookType = "M"

    #Determines whether the user is a GotAnime member if they want to scrape RightStufAnime
    def getMemberStatus(self):
        if self.gotAnimeMemberStatus.isChecked():
            self.memberStatus = True
        elif not self.gotAnimeMemberStatus.isChecked():
            self.memberStatus = False
    
    #Determines whether the user wants to scrape RightStufAnime and if so resize the window for the member status checkbox
    def getRSWebsite(self):
        if self.rightstufCheckBox.isChecked():
            MangaScrapeGUI.setMinimumSize(QtCore.QSize(319, 250))
            MangaScrapeGUI.setMaximumSize(QtCore.QSize(319, 250))
            self.gotAnimeMemberStatus.show()
            self.runScrape.setGeometry(QtCore.QRect(115, 170, 41, 31))
            self.printDataButton.setGeometry(QtCore.QRect(165, 170, 41, 31))
            self.progressBar.setGeometry(QtCore.QRect(100, 210, 121, 23))
            self.websiteList.append("RS")
        elif not self.rightstufCheckBox.isChecked():
            MangaScrapeGUI.setMinimumSize(QtCore.QSize(319, 230))
            MangaScrapeGUI.setMaximumSize(QtCore.QSize(319, 230))
            self.gotAnimeMemberStatus.hide()
            self.printDataButton.setGeometry(QtCore.QRect(165, 150, 41, 31))
            self.runScrape.setGeometry(QtCore.QRect(115, 150, 41, 31))
            self.progressBar.setGeometry(QtCore.QRect(100, 190, 121, 23))
            self.websiteList.remove("RS")
    
    #Determines whether the user wants to scrape Roberts Anime Corner Store  
    def getRobertWebsite(self):
        if self.robertsCheckBox.isChecked():
            self.websiteList.append("R")
        elif not self.robertsCheckBox.isChecked():
            self.websiteList.remove("R")
    
    #Runs the progress by incrementing counter ever 3/10 oth a second
    # def runProgressBar(self):
    #     for x in range(101):
    #         time.sleep(25 / 100)
    #         self.progressBar.setValue(x)
            
    def printData(self):
        self.window = QtWidgets.QMainWindow()
        self.tablesGUI = UI_DataTablesGUI()
        self.tablesGUI.setupUi(self.window)
        self.tablesGUI.convertRightStufData()
        self.tablesGUI.convertRobertsData()
        self.window.show()
    
    #Runs the manga scrape script to get data    
    def getPrices(self):
        if self.runScrape.isChecked() and ((len(self.bookType) == 0) or (not self.seriesTitleInput.text()) or (websiteList == [])): #Check to see if the user hit run, picked a book type, entered a series title, and picked a website to scrape
            print("Error!!!")
        else:
            getPriceData(self.memberStatus, self.seriesTitleInput.text(), self.bookType, self.websiteList)
            
            
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MangaScrapeGUI = QtWidgets.QMainWindow()
    ui = Ui_MangaScrapeGUI()
    ui.setupUi(MangaScrapeGUI)
    MangaScrapeGUI.show()
    sys.exit(app.exec_())
          
            
                    