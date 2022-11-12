# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 489)
        MainWindow.setMinimumSize(QtCore.QSize(800, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../assets/icons/camel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralContainer = QtWidgets.QWidget(MainWindow)
        self.centralContainer.setObjectName("centralContainer")
        self.screens = QtWidgets.QStackedWidget(self.centralContainer)
        self.screens.setGeometry(QtCore.QRect(0, 0, 801, 452))
        self.screens.setObjectName("screens")
        self.portal = QtWidgets.QWidget()
        self.portal.setObjectName("portal")
        self.homeArrow = QtWidgets.QCommandLinkButton(self.portal)
        self.homeArrow.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.homeArrow.setStyleSheet(":hover {\n"
"    border: none;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../assets/icons/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeArrow.setIcon(icon1)
        self.homeArrow.setObjectName("homeArrow")
        self.portalHeading = QtWidgets.QLabel(self.portal)
        self.portalHeading.setGeometry(QtCore.QRect(320, 10, 161, 31))
        self.portalHeading.setStyleSheet("font-family: \"Myanmar Text\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"")
        self.portalHeading.setAlignment(QtCore.Qt.AlignCenter)
        self.portalHeading.setObjectName("portalHeading")
        self.portalScrollArea = QtWidgets.QScrollArea(self.portal)
        self.portalScrollArea.setGeometry(QtCore.QRect(80, 100, 391, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portalScrollArea.sizePolicy().hasHeightForWidth())
        self.portalScrollArea.setSizePolicy(sizePolicy)
        self.portalScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.portalScrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.portalScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.portalScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.portalScrollArea.setObjectName("portalScrollArea")
        self.portalScrollContents = QtWidgets.QWidget()
        self.portalScrollContents.setGeometry(QtCore.QRect(0, 0, 374, 1042))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(90)
        sizePolicy.setHeightForWidth(self.portalScrollContents.sizePolicy().hasHeightForWidth())
        self.portalScrollContents.setSizePolicy(sizePolicy)
        self.portalScrollContents.setObjectName("portalScrollContents")
        self.gridLayout = QtWidgets.QGridLayout(self.portalScrollContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label_12 = QtWidgets.QLabel(self.portalScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(0, 200))
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.portalScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(0, 200))
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.portalScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(0, 200))
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.portalScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QtCore.QSize(0, 200))
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 3, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.portalScrollContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(0, 200))
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 4, 0, 1, 1)
        self.portalScrollArea.setWidget(self.portalScrollContents)
        self.lineEdit = QtWidgets.QLineEdit(self.portal)
        self.lineEdit.setGeometry(QtCore.QRect(80, 59, 391, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.testGraph = QtWidgets.QGraphicsView(self.portal)
        self.testGraph.setGeometry(QtCore.QRect(490, 60, 256, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.testGraph.sizePolicy().hasHeightForWidth())
        self.testGraph.setSizePolicy(sizePolicy)
        self.testGraph.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.testGraph.setToolTipDuration(0)
        self.testGraph.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.testGraph.setFrameShadow(QtWidgets.QFrame.Plain)
        self.testGraph.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.testGraph.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.testGraph.setObjectName("testGraph")
        self.screens.addWidget(self.portal)
        self.databaza = QtWidgets.QWidget()
        self.databaza.setObjectName("databaza")
        self.homeArrow5 = QtWidgets.QCommandLinkButton(self.databaza)
        self.homeArrow5.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.homeArrow5.setStyleSheet(":hover {\n"
"    border: none;\n"
"}")
        self.homeArrow5.setIcon(icon1)
        self.homeArrow5.setObjectName("homeArrow5")
        self.databazaHeading = QtWidgets.QLabel(self.databaza)
        self.databazaHeading.setGeometry(QtCore.QRect(320, 10, 161, 31))
        self.databazaHeading.setStyleSheet("font-family: \"Myanmar Text\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"")
        self.databazaHeading.setAlignment(QtCore.Qt.AlignCenter)
        self.databazaHeading.setObjectName("databazaHeading")
        self.screens.addWidget(self.databaza)
        self.cenotvorba = QtWidgets.QWidget()
        self.cenotvorba.setObjectName("cenotvorba")
        self.homeArrow3 = QtWidgets.QCommandLinkButton(self.cenotvorba)
        self.homeArrow3.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.homeArrow3.setStyleSheet(":hover {\n"
"    border: none;\n"
"}")
        self.homeArrow3.setIcon(icon1)
        self.homeArrow3.setObjectName("homeArrow3")
        self.cenotvorbaHeading = QtWidgets.QLabel(self.cenotvorba)
        self.cenotvorbaHeading.setGeometry(QtCore.QRect(320, 10, 161, 31))
        self.cenotvorbaHeading.setStyleSheet("font-family: \"Myanmar Text\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"")
        self.cenotvorbaHeading.setAlignment(QtCore.Qt.AlignCenter)
        self.cenotvorbaHeading.setObjectName("cenotvorbaHeading")
        self.screens.addWidget(self.cenotvorba)
        self.sklad = QtWidgets.QWidget()
        self.sklad.setObjectName("sklad")
        self.homeArrow4 = QtWidgets.QCommandLinkButton(self.sklad)
        self.homeArrow4.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.homeArrow4.setStyleSheet(":hover {\n"
"    border: none;\n"
"}")
        self.homeArrow4.setIcon(icon1)
        self.homeArrow4.setObjectName("homeArrow4")
        self.skladHeading = QtWidgets.QLabel(self.sklad)
        self.skladHeading.setGeometry(QtCore.QRect(320, 10, 161, 31))
        self.skladHeading.setStyleSheet("font-family: \"Myanmar Text\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"")
        self.skladHeading.setAlignment(QtCore.Qt.AlignCenter)
        self.skladHeading.setObjectName("skladHeading")
        self.screens.addWidget(self.sklad)
        self.statistika = QtWidgets.QWidget()
        self.statistika.setObjectName("statistika")
        self.homeArrow2 = QtWidgets.QCommandLinkButton(self.statistika)
        self.homeArrow2.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.homeArrow2.setStyleSheet(":hover {\n"
"    border: none;\n"
"}")
        self.homeArrow2.setIcon(icon1)
        self.homeArrow2.setObjectName("homeArrow2")
        self.statistikaHeading = QtWidgets.QLabel(self.statistika)
        self.statistikaHeading.setGeometry(QtCore.QRect(320, 10, 161, 31))
        self.statistikaHeading.setStyleSheet("font-family: \"Myanmar Text\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"")
        self.statistikaHeading.setAlignment(QtCore.Qt.AlignCenter)
        self.statistikaHeading.setObjectName("statistikaHeading")
        self.statistikaTestGraf = QtWidgets.QGraphicsView(self.statistika)
        self.statistikaTestGraf.setGeometry(QtCore.QRect(170, 120, 461, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statistikaTestGraf.sizePolicy().hasHeightForWidth())
        self.statistikaTestGraf.setSizePolicy(sizePolicy)
        self.statistikaTestGraf.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.statistikaTestGraf.setToolTipDuration(0)
        self.statistikaTestGraf.setFrameShape(QtWidgets.QFrame.HLine)
        self.statistikaTestGraf.setFrameShadow(QtWidgets.QFrame.Plain)
        self.statistikaTestGraf.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.statistikaTestGraf.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.statistikaTestGraf.setObjectName("statistikaTestGraf")
        self.screens.addWidget(self.statistika)
        self.index = QtWidgets.QWidget()
        self.index.setObjectName("index")
        self.statistikaLabel = QtWidgets.QLabel(self.index)
        self.statistikaLabel.setGeometry(QtCore.QRect(220, 270, 121, 31))
        self.statistikaLabel.setStyleSheet("font-family: \"Myanmar Text\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"")
        self.statistikaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statistikaLabel.setObjectName("statistikaLabel")
        self.cenotvorbaLabel = QtWidgets.QLabel(self.index)
        self.cenotvorbaLabel.setGeometry(QtCore.QRect(100, 270, 121, 31))
        self.cenotvorbaLabel.setStyleSheet("font-family: \"Myanmar Text\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"")
        self.cenotvorbaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.cenotvorbaLabel.setObjectName("cenotvorbaLabel")
        self.skladLabel = QtWidgets.QLabel(self.index)
        self.skladLabel.setGeometry(QtCore.QRect(340, 270, 121, 31))
        self.skladLabel.setStyleSheet("font-family: \"Myanmar Text\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"")
        self.skladLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.skladLabel.setObjectName("skladLabel")
        self.cenotvorbaButton = QtWidgets.QPushButton(self.index)
        self.cenotvorbaButton.setGeometry(QtCore.QRect(120, 180, 80, 80))
        self.cenotvorbaButton.setStyleSheet("QPushButton {\n"
"    background: rgb(0, 170, 255);\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(10, 174, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:rgb(0, 142, 213);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 4px;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../assets/icons/price-tag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cenotvorbaButton.setIcon(icon2)
        self.cenotvorbaButton.setIconSize(QtCore.QSize(40, 40))
        self.cenotvorbaButton.setObjectName("cenotvorbaButton")
        self.statistikaButton = QtWidgets.QPushButton(self.index)
        self.statistikaButton.setGeometry(QtCore.QRect(240, 180, 80, 80))
        self.statistikaButton.setStyleSheet("QPushButton {\n"
"    background: rgb(0, 170, 255);\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(10, 174, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:rgb(0, 142, 213);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 4px;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../assets/icons/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statistikaButton.setIcon(icon3)
        self.statistikaButton.setIconSize(QtCore.QSize(40, 40))
        self.statistikaButton.setObjectName("statistikaButton")
        self.skladButton = QtWidgets.QPushButton(self.index)
        self.skladButton.setGeometry(QtCore.QRect(360, 180, 80, 80))
        self.skladButton.setStyleSheet("QPushButton {\n"
"    background: rgb(0, 170, 255);\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(10, 174, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:rgb(0, 142, 213);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 4px;\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../assets/icons/locker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.skladButton.setIcon(icon4)
        self.skladButton.setIconSize(QtCore.QSize(40, 40))
        self.skladButton.setObjectName("skladButton")
        self.databazaLabel = QtWidgets.QLabel(self.index)
        self.databazaLabel.setGeometry(QtCore.QRect(580, 270, 121, 31))
        self.databazaLabel.setStyleSheet("font-family: \"Myanmar Text\";\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"")
        self.databazaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.databazaLabel.setObjectName("databazaLabel")
        self.camelLogo = QtWidgets.QLabel(self.index)
        self.camelLogo.setGeometry(QtCore.QRect(360, 20, 81, 80))
        self.camelLogo.setPixmap(QtGui.QPixmap("../../assets/icons/camel.png"))
        self.camelLogo.setScaledContents(True)
        self.camelLogo.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.camelLogo.setObjectName("camelLogo")
        self.databazaButton = QtWidgets.QPushButton(self.index)
        self.databazaButton.setGeometry(QtCore.QRect(600, 180, 80, 80))
        self.databazaButton.setStyleSheet("QPushButton {\n"
"    background: rgb(0, 170, 255);\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(10, 174, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:rgb(0, 142, 213);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 4px;\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../assets/icons/online-shop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.databazaButton.setIcon(icon5)
        self.databazaButton.setIconSize(QtCore.QSize(40, 40))
        self.databazaButton.setObjectName("databazaButton")
        self.portalButton = QtWidgets.QPushButton(self.index)
        self.portalButton.setGeometry(QtCore.QRect(480, 180, 80, 80))
        self.portalButton.setStyleSheet("QPushButton {\n"
"    background: rgb(0, 170, 255);\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(10, 174, 255);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background:rgb(0, 142, 213);\n"
"    border: 2px solid rgb(0, 170, 255);\n"
"    border-radius: 4px;\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../assets/icons/shopping-bag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.portalButton.setIcon(icon6)
        self.portalButton.setIconSize(QtCore.QSize(40, 40))
        self.portalButton.setObjectName("portalButton")
        self.portalLabel = QtWidgets.QLabel(self.index)
        self.portalLabel.setGeometry(QtCore.QRect(460, 270, 121, 51))
        self.portalLabel.setStyleSheet("QLabel {\n"
"    font-family: \"Myanmar Text\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    line-height: 80;\n"
"}\n"
"")
        self.portalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.portalLabel.setWordWrap(True)
        self.portalLabel.setObjectName("portalLabel")
        self.screens.addWidget(self.index)
        MainWindow.setCentralWidget(self.centralContainer)

        self.retranslateUi(MainWindow)
        self.screens.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Camels Infornation System"))
        self.portalHeading.setText(_translate("MainWindow", "PREDAJNÝ PORTÁL"))
        self.label_12.setText(_translate("MainWindow", "ITEM NAME"))
        self.label_13.setText(_translate("MainWindow", "ITEM NAME"))
        self.label_14.setText(_translate("MainWindow", "ITEM NAME"))
        self.label_15.setText(_translate("MainWindow", "ITEM NAME"))
        self.label_16.setText(_translate("MainWindow", "ITEM NAME"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Vyhľadať produkt"))
        self.databazaHeading.setText(_translate("MainWindow", "INTERNÁ DATABÁZA"))
        self.cenotvorbaHeading.setText(_translate("MainWindow", "CENOTVORBA"))
        self.skladHeading.setText(_translate("MainWindow", "SKLAD"))
        self.statistikaHeading.setText(_translate("MainWindow", "ŠTATISTIKA"))
        self.statistikaLabel.setText(_translate("MainWindow", "ŠTATISTIKA"))
        self.cenotvorbaLabel.setText(_translate("MainWindow", "CENOTVORBA"))
        self.skladLabel.setText(_translate("MainWindow", "SKLAD"))
        self.cenotvorbaButton.setToolTip(_translate("MainWindow", "Otvoriť cenotvorbu"))
        self.databazaLabel.setText(_translate("MainWindow", "DATABÁZA"))
        self.camelLogo.setToolTip(_translate("MainWindow", "Camels"))
        self.databazaButton.setToolTip(_translate("MainWindow", "Otvoriť databázu"))
        self.portalLabel.setText(_translate("MainWindow", "PREDAJNÝ PORTÁL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
