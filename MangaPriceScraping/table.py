from PyQt5 import QtCore, QtGui, QtWidgets
import csv

class UI_DataTablesGUI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1036, 753)
        self.rightStufDataTable = QtWidgets.QTableWidget(Form)
        self.rightStufDataTable.horizontalHeader().setStretchLastSection(True)
        self.rightStufDataTable.setGeometry(QtCore.QRect(50, 70, 441, 641))
        # self.rightStufDataTable.setRowCount(20)
        self.rightStufDataTable.setColumnCount(3)
        self.rightStufDataTable.setObjectName("rightStufDataTable")
        
        self.robertsDataTable = QtWidgets.QTableWidget(Form)
        self.robertsDataTable.setGeometry(QtCore.QRect(550, 70, 441, 641))
        self.robertsDataTable.setRowCount(20)
        self.robertsDataTable.setColumnCount(3)
        self.robertsDataTable.setObjectName("robertsDataTable")
        
        self.rightStufDataTitle = QtWidgets.QLabel(Form)
        self.rightStufDataTitle.setGeometry(QtCore.QRect(170, 29, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        
        self.rightStufDataTitle.setFont(font)
        self.rightStufDataTitle.setObjectName("rightStufDataTitle")
        self.robertsDataTitle = QtWidgets.QLabel(Form)
        self.robertsDataTitle.setGeometry(QtCore.QRect(620, 30, 321, 31))
        
        font = QtGui.QFont()
        font.setPointSize(16)
        
        self.robertsDataTitle.setFont(font)
        self.robertsDataTitle.setObjectName("robertsDataTitle")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        with open("C:\MangaHabu\RightStufAnimeData.csv", "r") as dataFile:
            self.rightStufDataTable.setRowCount(sum(1 for row in csv.reader(dataFile)))
        
        with open("C:\MangaHabu\RightStufAnimeData.csv", "r") as dataFile:
            rightStufData = csv.reader(dataFile)
            numRows = 0
            for dataRow in rightStufData:
                dataList = list(dataRow)
                self.rightStufDataTable.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str(dataList[0])))
                self.rightStufDataTable.setItem(numRows, 1, QtWidgets.QTableWidgetItem(str(dataList[1])))
                self.rightStufDataTable.setItem(numRows, 2, QtWidgets.QTableWidgetItem(str(dataList[2])))
                numRows += 1
                
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.robertsDataTable.setSortingEnabled(True)
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
