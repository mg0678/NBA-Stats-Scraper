# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainuixMkEmP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(948, 878)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tmBtn = QRadioButton(self.centralwidget)
        self.tmPlyrGrp = QButtonGroup(MainWindow)
        self.tmPlyrGrp.setObjectName(u"tmPlyrGrp")
        self.tmPlyrGrp.addButton(self.tmBtn)
        self.tmBtn.setObjectName(u"tmBtn")
        self.tmBtn.setGeometry(QRect(10, 20, 82, 17))
        self.leagueBtn = QRadioButton(self.centralwidget)
        self.tmPlyrGrp.addButton(self.leagueBtn)
        self.leagueBtn.setObjectName(u"leagueBtn")
        self.leagueBtn.setGeometry(QRect(10, 50, 111, 17))
        self.perGmBtn = QRadioButton(self.centralwidget)
        self.gmSeasonGrp = QButtonGroup(MainWindow)
        self.gmSeasonGrp.setObjectName(u"gmSeasonGrp")
        self.gmSeasonGrp.addButton(self.perGmBtn)
        self.perGmBtn.setObjectName(u"perGmBtn")
        self.perGmBtn.setGeometry(QRect(170, 20, 82, 17))
        self.seasonBtn = QRadioButton(self.centralwidget)
        self.gmSeasonGrp.addButton(self.seasonBtn)
        self.seasonBtn.setObjectName(u"seasonBtn")
        self.seasonBtn.setGeometry(QRect(170, 50, 91, 17))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(21, 141, 476, 352))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(48)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.atlBox = QCheckBox(self.layoutWidget)
        self.atlBox.setObjectName(u"atlBox")

        self.gridLayout.addWidget(self.atlBox, 0, 0, 1, 1)

        self.bosBox = QCheckBox(self.layoutWidget)
        self.bosBox.setObjectName(u"bosBox")

        self.gridLayout.addWidget(self.bosBox, 0, 1, 1, 1)

        self.brkBox = QCheckBox(self.layoutWidget)
        self.brkBox.setObjectName(u"brkBox")

        self.gridLayout.addWidget(self.brkBox, 0, 2, 1, 1)

        self.choBox = QCheckBox(self.layoutWidget)
        self.choBox.setObjectName(u"choBox")

        self.gridLayout.addWidget(self.choBox, 1, 0, 1, 1)

        self.chiBox = QCheckBox(self.layoutWidget)
        self.chiBox.setObjectName(u"chiBox")

        self.gridLayout.addWidget(self.chiBox, 1, 1, 1, 1)

        self.cleBox = QCheckBox(self.layoutWidget)
        self.cleBox.setObjectName(u"cleBox")

        self.gridLayout.addWidget(self.cleBox, 1, 2, 1, 1)

        self.dalBox = QCheckBox(self.layoutWidget)
        self.dalBox.setObjectName(u"dalBox")

        self.gridLayout.addWidget(self.dalBox, 2, 0, 1, 1)

        self.denBox = QCheckBox(self.layoutWidget)
        self.denBox.setObjectName(u"denBox")

        self.gridLayout.addWidget(self.denBox, 2, 1, 1, 1)

        self.detBox = QCheckBox(self.layoutWidget)
        self.detBox.setObjectName(u"detBox")

        self.gridLayout.addWidget(self.detBox, 2, 2, 1, 1)

        self.gdwBox = QCheckBox(self.layoutWidget)
        self.gdwBox.setObjectName(u"gdwBox")

        self.gridLayout.addWidget(self.gdwBox, 3, 0, 1, 1)

        self.houBox = QCheckBox(self.layoutWidget)
        self.houBox.setObjectName(u"houBox")

        self.gridLayout.addWidget(self.houBox, 3, 1, 1, 1)

        self.indBox = QCheckBox(self.layoutWidget)
        self.indBox.setObjectName(u"indBox")

        self.gridLayout.addWidget(self.indBox, 3, 2, 1, 1)

        self.lacBox = QCheckBox(self.layoutWidget)
        self.lacBox.setObjectName(u"lacBox")

        self.gridLayout.addWidget(self.lacBox, 4, 0, 1, 1)

        self.lalBox = QCheckBox(self.layoutWidget)
        self.lalBox.setObjectName(u"lalBox")

        self.gridLayout.addWidget(self.lalBox, 4, 1, 1, 1)

        self.memBox = QCheckBox(self.layoutWidget)
        self.memBox.setObjectName(u"memBox")

        self.gridLayout.addWidget(self.memBox, 4, 2, 1, 1)

        self.miaBox = QCheckBox(self.layoutWidget)
        self.miaBox.setObjectName(u"miaBox")

        self.gridLayout.addWidget(self.miaBox, 5, 0, 1, 1)

        self.milBox = QCheckBox(self.layoutWidget)
        self.milBox.setObjectName(u"milBox")

        self.gridLayout.addWidget(self.milBox, 5, 1, 1, 1)

        self.minBox = QCheckBox(self.layoutWidget)
        self.minBox.setObjectName(u"minBox")

        self.gridLayout.addWidget(self.minBox, 5, 2, 1, 1)

        self.nopBox = QCheckBox(self.layoutWidget)
        self.nopBox.setObjectName(u"nopBox")

        self.gridLayout.addWidget(self.nopBox, 6, 0, 1, 1)

        self.nykBox = QCheckBox(self.layoutWidget)
        self.nykBox.setObjectName(u"nykBox")

        self.gridLayout.addWidget(self.nykBox, 6, 1, 1, 1)

        self.okcBox = QCheckBox(self.layoutWidget)
        self.okcBox.setObjectName(u"okcBox")

        self.gridLayout.addWidget(self.okcBox, 6, 2, 1, 1)

        self.orlBox = QCheckBox(self.layoutWidget)
        self.orlBox.setObjectName(u"orlBox")

        self.gridLayout.addWidget(self.orlBox, 7, 0, 1, 1)

        self.phiBox = QCheckBox(self.layoutWidget)
        self.phiBox.setObjectName(u"phiBox")

        self.gridLayout.addWidget(self.phiBox, 7, 1, 1, 1)

        self.phoBox = QCheckBox(self.layoutWidget)
        self.phoBox.setObjectName(u"phoBox")

        self.gridLayout.addWidget(self.phoBox, 7, 2, 1, 1)

        self.porBox = QCheckBox(self.layoutWidget)
        self.porBox.setObjectName(u"porBox")

        self.gridLayout.addWidget(self.porBox, 8, 0, 1, 1)

        self.sacBox = QCheckBox(self.layoutWidget)
        self.sacBox.setObjectName(u"sacBox")

        self.gridLayout.addWidget(self.sacBox, 8, 1, 1, 1)

        self.sasBox = QCheckBox(self.layoutWidget)
        self.sasBox.setObjectName(u"sasBox")

        self.gridLayout.addWidget(self.sasBox, 8, 2, 1, 1)

        self.torBox = QCheckBox(self.layoutWidget)
        self.torBox.setObjectName(u"torBox")

        self.gridLayout.addWidget(self.torBox, 9, 0, 1, 1)

        self.utaBox = QCheckBox(self.layoutWidget)
        self.utaBox.setObjectName(u"utaBox")

        self.gridLayout.addWidget(self.utaBox, 9, 1, 1, 1)

        self.wasBox = QCheckBox(self.layoutWidget)
        self.wasBox.setObjectName(u"wasBox")

        self.gridLayout.addWidget(self.wasBox, 9, 2, 1, 1)

        self.submitBtn = QPushButton(self.centralwidget)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setGeometry(QRect(20, 510, 75, 23))
        self.submitBtn.clicked.connect(self.checkButton)
        self.exitBtn = QPushButton(self.centralwidget)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setGeometry(QRect(110, 510, 75, 23))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(520, 20, 391, 791))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 948, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tmBtn.setText(QCoreApplication.translate("MainWindow", u"By Team", None))
        self.leagueBtn.setText(QCoreApplication.translate("MainWindow", u"League Leaders", None))
        self.perGmBtn.setText(QCoreApplication.translate("MainWindow", u"Per Game", None))
        self.seasonBtn.setText(QCoreApplication.translate("MainWindow", u"Season Totals", None))
        self.atlBox.setText(QCoreApplication.translate("MainWindow", u"Atlanta Hawks", None))
        self.bosBox.setText(QCoreApplication.translate("MainWindow", u"Boston Celtics", None))
        self.brkBox.setText(QCoreApplication.translate("MainWindow", u"Brooklyn Nets", None))
        self.choBox.setText(QCoreApplication.translate("MainWindow", u"Charlotte Hornets", None))
        self.chiBox.setText(QCoreApplication.translate("MainWindow", u"Chicago Bulls", None))
        self.cleBox.setText(QCoreApplication.translate("MainWindow", u"Cleveland Cavaliers", None))
        self.dalBox.setText(QCoreApplication.translate("MainWindow", u"Dallas Mavericks", None))
        self.denBox.setText(QCoreApplication.translate("MainWindow", u"Denver Nuggets", None))
        self.detBox.setText(QCoreApplication.translate("MainWindow", u"Detroit Pistons", None))
        self.gdwBox.setText(QCoreApplication.translate("MainWindow", u"Golden State Warriors", None))
        self.houBox.setText(QCoreApplication.translate("MainWindow", u"Houston Rockets", None))
        self.indBox.setText(QCoreApplication.translate("MainWindow", u"Indiana Pacers", None))
        self.lacBox.setText(QCoreApplication.translate("MainWindow", u"LA Clippers", None))
        self.lalBox.setText(QCoreApplication.translate("MainWindow", u"LA Lakers", None))
        self.memBox.setText(QCoreApplication.translate("MainWindow", u"Memphis Grizzlies", None))
        self.miaBox.setText(QCoreApplication.translate("MainWindow", u"Miami Heat", None))
        self.milBox.setText(QCoreApplication.translate("MainWindow", u"Milwaukee Bucks", None))
        self.minBox.setText(QCoreApplication.translate("MainWindow", u"Minnesota Timberwolves", None))
        self.nopBox.setText(QCoreApplication.translate("MainWindow", u"New Orleans Pelicans", None))
        self.nykBox.setText(QCoreApplication.translate("MainWindow", u"New York Knicks", None))
        self.okcBox.setText(QCoreApplication.translate("MainWindow", u"Oklahoma City Thunder", None))
        self.orlBox.setText(QCoreApplication.translate("MainWindow", u"Orlando Magic", None))
        self.phiBox.setText(QCoreApplication.translate("MainWindow", u"Philadelphia 76ers", None))
        self.phoBox.setText(QCoreApplication.translate("MainWindow", u"Phoenix Suns", None))
        self.porBox.setText(QCoreApplication.translate("MainWindow", u"Portland Trailblazers", None))
        self.sacBox.setText(QCoreApplication.translate("MainWindow", u"Sacramento Kings", None))
        self.sasBox.setText(QCoreApplication.translate("MainWindow", u"San Antonio Spurs", None))
        self.torBox.setText(QCoreApplication.translate("MainWindow", u"Toronto Raptors", None))
        self.utaBox.setText(QCoreApplication.translate("MainWindow", u"Utah Jazz", None))
        self.wasBox.setText(QCoreApplication.translate("MainWindow", u"Washington Wizards", None))
        self.submitBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.exitBtn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    
    def checkButton(self):
        self.plainTextEdit.clear()
        if self.tmBtn.isChecked():
            self.plainTextEdit.insertPlainText("Team Selected")
        else:
            self.plainTextEdit.insertPlainText("League Selected")
        if self.perGmBtn.isChecked():
            self.plainTextEdit.insertPlainText("Stats Per Game") 
        else:
            self.plainTextEdit.insertPlainText("Season Stats")
    

    # retranslateUi

app = QApplication(sys.argv)
main_window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(main_window)
main_window.show()
sys.exit(app.exec_())

