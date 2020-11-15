# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scrapegui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.bookTypeMangaButton = QtWidgets.QPushButton(self.MangaScrapeWidget)
        self.bookTypeMangaButton.setGeometry(QtCore.QRect(50, 70, 101, 31))
        self.bookTypeMangaButton.setCheckable(True)
        self.bookTypeMangaButton.setChecked(False)
        self.bookTypeMangaButton.setAutoExclusive(True)
        self.bookTypeMangaButton.setObjectName("bookTypeMangaButton")
        self.bookTypeNovelButton = QtWidgets.QPushButton(self.MangaScrapeWidget)
        self.bookTypeNovelButton.setGeometry(QtCore.QRect(170, 70, 91, 31))
        self.bookTypeNovelButton.setCheckable(True)
        self.bookTypeNovelButton.setAutoExclusive(True)
        self.bookTypeNovelButton.setObjectName("bookTypeNovelButton")
        self.rightstufCheckBox = QtWidgets.QCheckBox(self.MangaScrapeWidget)
        self.rightstufCheckBox.setGeometry(QtCore.QRect(30, 120, 101, 17))
        self.rightstufCheckBox.setObjectName("rightstufCheckBox")
        self.robertsCheckbox = QtWidgets.QCheckBox(self.MangaScrapeWidget)
        self.robertsCheckbox.setGeometry(QtCore.QRect(140, 120, 161, 17))
        self.robertsCheckbox.setTristate(False)
        self.robertsCheckbox.setObjectName("robertsCheckbox")
        self.progressBar = QtWidgets.QProgressBar(self.MangaScrapeWidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 190, 121, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.MangaScrapeWidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 150, 41, 31))
        icon = QtGui.QIcon.fromTheme("Play")
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        MangaScrapeGUI.setCentralWidget(self.MangaScrapeWidget)
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
        self.robertsCheckbox.setText(_translate("MangaScrapeGUI", "Roberts Anime Corner Store"))
        self.progressBar.setFormat(_translate("MangaScrapeGUI", "%p%"))
        self.pushButton.setText(_translate("MangaScrapeGUI", "Run"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MangaScrapeGUI = QtWidgets.QMainWindow()
    ui = Ui_MangaScrapeGUI()
    ui.setupUi(MangaScrapeGUI)
    MangaScrapeGUI.show()
    sys.exit(app.exec_())