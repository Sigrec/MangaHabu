from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import csv

class UI_DataTablesGUI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1036, 753)
        
        font = QtGui.QFont()
        font.setPointSize(16)
        
        self.rightStufDataTable = QtWidgets.QTableWidget(Form)
        #self.rightStufDataTable.horizontalHeader().setStretchLastSection(True)
        self.rightStufDataTable.setGeometry(QtCore.QRect(50, 70, 441, 600))
        self.rightStufDataTable.setColumnCount(3)
        self.rightStufDataTable.setObjectName("rightStufDataTable")
        
        self.robertsDataTable = QtWidgets.QTableWidget(Form)
        self.robertsDataTable.setGeometry(QtCore.QRect(550, 70, 441, 600))
        self.robertsDataTable.setColumnCount(3)
        self.robertsDataTable.setObjectName("robertsDataTable")
        
        self.rightStufDataTitle = QtWidgets.QLabel(Form)
        self.rightStufDataTitle.setGeometry(QtCore.QRect(170, 29, 201, 31))
        self.rightStufDataTitle.setFont(font)
        self.rightStufDataTitle.setObjectName("rightStufDataTitle")
        
        self.robertsDataTitle = QtWidgets.QLabel(Form)
        self.robertsDataTitle.setGeometry(QtCore.QRect(620, 30, 321, 31))
        self.robertsDataTitle.setFont(font)
        self.robertsDataTitle.setObjectName("robertsDataTitle")
        
        self.printTypeLabel = QtWidgets.QLabel(Form)
        self.printTypeLabel.setGeometry(QtCore.QRect(425, 675, 231, 25))
        self.printTypeLabel.setObjectName("specificPrintFinder")
        
        self.printTypeInput = QtWidgets.QLineEdit(Form)
        self.printTypeInput.setGeometry(QtCore.QRect(380, 705, 281, 20))
        self.printTypeInput.setPlaceholderText("Search...")
        self.printTypeInput.textChanged.connect(self.searchData)
        self.printTypeInput.setObjectName("specificPrintType")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def searchData(self, key):
        findVolRS = self.rightStufDataTable.findItems(key, Qt.MatchContains)
        findVolRobert = self.robertsDataTable.findItems(key, Qt.MatchContains)
        if findVolRS or findVolRobert:
            foundTitleOne = findVolRS[0]
            foundTitleTwo = findVolRobert[0]
            self.rightStufDataTable.setCurrentItem(foundTitleOne)
            self.robertsDataTable.setCurrentItem(foundTitleTwo)
    
    def convertRightStufData(self, dataList):
        with open("RightStufAnimeData.csv", "r") as dataFile:
            self.rightStufDataTable.setRowCount(sum(1 for row in csv.reader(dataFile)))
        
        with open("RightStufAnimeData.csv", "r") as dataFile:
            rightStufData = csv.reader(dataFile)
            numRows = 0
            for dataRow in rightStufData:
                dataList = list(dataRow)
                self.rightStufDataTable.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(dataList[0])))
                self.rightStufDataTable.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(dataList[1])))
                self.rightStufDataTable.setItem(numRows, 2, QtWidgets.QTableWidgetItem(str(dataList[2])))
                numRows += 1
        
        self.rightStufDataTable.setRowCount(len(dataList))
        numRows = 0
        for dataRow in rightStufData:
            dataList = list(dataRow)
            self.rightStufDataTable.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(dataList[0])))
            self.rightStufDataTable.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(dataList[1])))
            self.rightStufDataTable.setItem(numRows, 2, QtWidgets.QTableWidgetItem(str(dataList[2])))
            numRows += 1
    
    def convertRobertsData(self, dataList):
        with open("AnimeCornerStore.csv", "r") as dataFile:
            self.robertsDataTable.setRowCount(sum(1 for row in csv.reader(dataFile)))
        
        with open("AnimeCornerStore.csv", "r") as dataFile:
            robertsData = csv.reader(dataFile)
            numRows = 0
            for dataRow in robertsData:
                dataList = list(dataRow)
                self.robertsDataTable.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(dataList[0])))
                self.robertsDataTable.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(dataList[1])))
                self.robertsDataTable.setItem(numRows, 2, QtWidgets.QTableWidgetItem(str(dataList[2])))
                numRows += 1
                
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.robertsDataTable.setSortingEnabled(True)
        self.printTypeLabel.setText(_translate("MangaScrapeGUI", "Enter Print Type Below:"))
        self.rightStufDataTitle.setText(_translate("Form", "RightStufAnime Data"))
        self.robertsDataTitle.setText(_translate("Form", "Robert\'s Anime Corner Store Data"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = UI_DataTablesGUI()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
