# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/osman/OneDrive/Masaüstü/PostFilterAppInterFace.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 550)
        MainWindow.setMinimumSize(QtCore.QSize(900, 550))
        MainWindow.setMaximumSize(QtCore.QSize(900, 550))
        MainWindow.setStyleSheet("background-color: #070F2B;\n"
"color: rgb(255, 255, 255);\n"
"padding: 0;")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.ArticlesPage = QtWidgets.QWidget()
        self.ArticlesPage.setObjectName("ArticlesPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ArticlesPage)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PostTitle = QtWidgets.QLabel(self.ArticlesPage)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PostTitle.setFont(font)
        self.PostTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.PostTitle.setObjectName("PostTitle")
        self.verticalLayout_2.addWidget(self.PostTitle)
        self.PostContent = QtWidgets.QPlainTextEdit(self.ArticlesPage)
        self.PostContent.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PostContent.setFont(font)
        self.PostContent.setStyleSheet("border: none;\n"
"padding: 15px;")
        self.PostContent.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.PostContent.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PostContent.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PostContent.setUndoRedoEnabled(True)
        self.PostContent.setPlainText("")
        self.PostContent.setObjectName("PostContent")
        self.verticalLayout_2.addWidget(self.PostContent)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BackPostBtn = QtWidgets.QPushButton(self.ArticlesPage)
        self.BackPostBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.BackPostBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.BackPostBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BackPostBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/media/media/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackPostBtn.setIcon(icon)
        self.BackPostBtn.setObjectName("BackPostBtn")
        self.horizontalLayout_2.addWidget(self.BackPostBtn)
        self.ConfirmBtn = QtWidgets.QPushButton(self.ArticlesPage)
        self.ConfirmBtn.setMinimumSize(QtCore.QSize(100, 30))
        self.ConfirmBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ConfirmBtn.setStyleSheet("QPushButton {\n"
"                border: 1px solid white;\n"
"                color: white;\n"
"                background-color: #070F2B;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0A1A3B;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #11264D;\n"
"                border-color: #CCCCCC;\n"
"            }")
        self.ConfirmBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/media/media/confirm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ConfirmBtn.setIcon(icon1)
        self.ConfirmBtn.setObjectName("ConfirmBtn")
        self.horizontalLayout_2.addWidget(self.ConfirmBtn)
        self.DenyBtn = QtWidgets.QPushButton(self.ArticlesPage)
        self.DenyBtn.setMinimumSize(QtCore.QSize(100, 30))
        self.DenyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DenyBtn.setStyleSheet("QPushButton {\n"
"                border: 1px solid white;\n"
"                color: white;\n"
"                background-color: #070F2B;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0A1A3B;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #11264D;\n"
"                border-color: #CCCCCC;\n"
"            }")
        self.DenyBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/media/media/deny.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DenyBtn.setIcon(icon2)
        self.DenyBtn.setObjectName("DenyBtn")
        self.horizontalLayout_2.addWidget(self.DenyBtn)
        self.SuspectBtn = QtWidgets.QPushButton(self.ArticlesPage)
        self.SuspectBtn.setMinimumSize(QtCore.QSize(100, 30))
        self.SuspectBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SuspectBtn.setStyleSheet("QPushButton {\n"
"                border: 1px solid white;\n"
"                color: white;\n"
"                background-color: #070F2B;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0A1A3B;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #11264D;\n"
"                border-color: #CCCCCC;\n"
"            }")
        self.SuspectBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/media/media/unlem.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SuspectBtn.setIcon(icon3)
        self.SuspectBtn.setObjectName("SuspectBtn")
        self.horizontalLayout_2.addWidget(self.SuspectBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.BriefBtn = QtWidgets.QPushButton(self.ArticlesPage)
        self.BriefBtn.setMinimumSize(QtCore.QSize(150, 30))
        self.BriefBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BriefBtn.setStyleSheet("QPushButton {\n"
"                border: 1px solid white;\n"
"                color: white;\n"
"                background-color: #070F2B;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0A1A3B;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #11264D;\n"
"                border-color: #CCCCCC;\n"
"            }")
        self.BriefBtn.setObjectName("BriefBtn")
        self.horizontalLayout_2.addWidget(self.BriefBtn)
        self.FilterBtn = QtWidgets.QPushButton(self.ArticlesPage)
        self.FilterBtn.setMinimumSize(QtCore.QSize(150, 30))
        self.FilterBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FilterBtn.setStyleSheet("QPushButton {\n"
"                border: 1px solid white;\n"
"                color: white;\n"
"                background-color: #070F2B;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0A1A3B;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #11264D;\n"
"                border-color: #CCCCCC;\n"
"            }")
        self.FilterBtn.setObjectName("FilterBtn")
        self.horizontalLayout_2.addWidget(self.FilterBtn)
        self.NextPostBtn = QtWidgets.QPushButton(self.ArticlesPage)
        self.NextPostBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.NextPostBtn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.NextPostBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NextPostBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/media/media/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NextPostBtn.setIcon(icon4)
        self.NextPostBtn.setObjectName("NextPostBtn")
        self.horizontalLayout_2.addWidget(self.NextPostBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.HorizontalSlider = QtWidgets.QSlider(self.ArticlesPage)
        self.HorizontalSlider.setStatusTip("")
        self.HorizontalSlider.setStyleSheet("margin-bottom: -100;")
        self.HorizontalSlider.setInputMethodHints(QtCore.Qt.ImhNone)
        self.HorizontalSlider.setMaximum(4)
        self.HorizontalSlider.setPageStep(1)
        self.HorizontalSlider.setProperty("value", 0)
        self.HorizontalSlider.setTracking(True)
        self.HorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.HorizontalSlider.setInvertedAppearance(False)
        self.HorizontalSlider.setInvertedControls(False)
        self.HorizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.HorizontalSlider.setObjectName("HorizontalSlider")
        self.verticalLayout_3.addWidget(self.HorizontalSlider)
        self.stackedWidget.addWidget(self.ArticlesPage)
        self.SettingsPage = QtWidgets.QWidget()
        self.SettingsPage.setObjectName("SettingsPage")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.SettingsPage)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(243, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem7)
        self.EmailInput = QtWidgets.QLineEdit(self.SettingsPage)
        self.EmailInput.setMinimumSize(QtCore.QSize(0, 30))
        self.EmailInput.setStyleSheet("border: 1px solid white;\n"
"padding-right: 10px;\n"
"padding-left: 10px;")
        self.EmailInput.setAlignment(QtCore.Qt.AlignCenter)
        self.EmailInput.setObjectName("EmailInput")
        self.verticalLayout_4.addWidget(self.EmailInput)
        self.PasswordInput = QtWidgets.QLineEdit(self.SettingsPage)
        self.PasswordInput.setMinimumSize(QtCore.QSize(0, 30))
        self.PasswordInput.setStyleSheet("border: 1px solid white;\n"
"padding-right: 10px;\n"
"padding-left: 10px;")
        self.PasswordInput.setAlignment(QtCore.Qt.AlignCenter)
        self.PasswordInput.setObjectName("PasswordInput")
        self.verticalLayout_4.addWidget(self.PasswordInput)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.MongoInput = QtWidgets.QLineEdit(self.SettingsPage)
        self.MongoInput.setMinimumSize(QtCore.QSize(0, 30))
        self.MongoInput.setStyleSheet("border: 1px solid white;\n"
"padding-right: 10px;\n"
"padding-left: 10px;")
        self.MongoInput.setAlignment(QtCore.Qt.AlignCenter)
        self.MongoInput.setObjectName("MongoInput")
        self.verticalLayout_4.addWidget(self.MongoInput)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.SettingsPage)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.SettingsPage)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Table1Combo = QtWidgets.QComboBox(self.SettingsPage)
        self.Table1Combo.setEnabled(True)
        self.Table1Combo.setMinimumSize(QtCore.QSize(150, 30))
        self.Table1Combo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Table1Combo.setStyleSheet("border: 1px solid white;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.Table1Combo.setEditable(False)
        self.Table1Combo.setObjectName("Table1Combo")
        self.horizontalLayout_3.addWidget(self.Table1Combo)
        self.Table2Combo = QtWidgets.QComboBox(self.SettingsPage)
        self.Table2Combo.setEnabled(True)
        self.Table2Combo.setMinimumSize(QtCore.QSize(150, 30))
        self.Table2Combo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Table2Combo.setStyleSheet("border: 1px solid white;\n"
"padding-left:5px;\n"
"padding-right:5px;")
        self.Table2Combo.setObjectName("Table2Combo")
        self.horizontalLayout_3.addWidget(self.Table2Combo)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem10)
        self.SaveBtn = QtWidgets.QPushButton(self.SettingsPage)
        self.SaveBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.SaveBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveBtn.setStyleSheet("QPushButton {\n"
"                border: 1px solid white;\n"
"                color: white;\n"
"                background-color: #070F2B;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #0A1A3B;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #11264D;\n"
"                border-color: #CCCCCC;\n"
"            }")
        self.SaveBtn.setObjectName("SaveBtn")
        self.verticalLayout_4.addWidget(self.SaveBtn)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem15)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem16)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem17)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem18 = QtWidgets.QSpacerItem(242, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem18)
        self.stackedWidget.addWidget(self.SettingsPage)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setStyleSheet("QMenuBar::item:selected {\n"
"    background: transparent;\n"
"}")
        self.menubar.setObjectName("menubar")
        self.menuMen_ler = QtWidgets.QMenu(self.menubar)
        self.menuMen_ler.setObjectName("menuMen_ler")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAyarlar = QtWidgets.QAction(MainWindow)
        self.actionAyarlar.setObjectName("actionAyarlar")
        self.actionArticles = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/media/media/makale.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionArticles.setIcon(icon5)
        self.actionArticles.setObjectName("actionArticles")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/media/media/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon6)
        self.actionSettings.setObjectName("actionSettings")
        self.menuMen_ler.addAction(self.actionArticles)
        self.menuMen_ler.addSeparator()
        self.menuMen_ler.addAction(self.actionSettings)
        self.menubar.addAction(self.menuMen_ler.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Formül Forum"))
        self.PostTitle.setText(_translate("MainWindow", "Başlık"))
        self.BriefBtn.setText(_translate("MainWindow", "Özet"))
        self.FilterBtn.setText(_translate("MainWindow", "Süzgeç"))
        self.EmailInput.setPlaceholderText(_translate("MainWindow", "E-posta Adresi"))
        self.PasswordInput.setPlaceholderText(_translate("MainWindow", "E-posta Parolası"))
        self.MongoInput.setPlaceholderText(_translate("MainWindow", "Mongo Bağlantı Url si"))
        self.label_2.setText(_translate("MainWindow", "Tablo 1"))
        self.label_3.setText(_translate("MainWindow", "Tablo 2"))
        self.SaveBtn.setText(_translate("MainWindow", "Kaydet"))
        self.menuMen_ler.setTitle(_translate("MainWindow", "Sayfalar"))
        self.actionAyarlar.setText(_translate("MainWindow", "Anasayfa"))
        self.actionArticles.setText(_translate("MainWindow", "Makaleler"))
        self.actionSettings.setText(_translate("MainWindow", "Ayarlar"))

import ui.media_rc
