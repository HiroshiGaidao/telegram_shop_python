# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowlYPzEt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(720, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(720, 450))
        MainWindow.setMaximumSize(QSize(720, 450))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 10, 651, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.category_box = QComboBox(self.horizontalLayoutWidget_2)
        self.category_box.setObjectName(u"category_box")
        self.category_box.setMinimumSize(QSize(200, 0))
        self.category_box.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.category_box)

        self.del_cat = QToolButton(self.horizontalLayoutWidget_2)
        self.del_cat.setObjectName(u"del_cat")
        icon = QIcon()
        icon.addFile(u"../telegram_shop_python/SVG/trash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.del_cat.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.del_cat)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.category_name = QLineEdit(self.horizontalLayoutWidget_2)
        self.category_name.setObjectName(u"category_name")
        self.category_name.setMaximumSize(QSize(999, 16777215))

        self.horizontalLayout.addWidget(self.category_name)

        self.add_category = QPushButton(self.horizontalLayoutWidget_2)
        self.add_category.setObjectName(u"add_category")
        self.add_category.setMinimumSize(QSize(160, 0))
        self.add_category.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout.addWidget(self.add_category)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 60, 651, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.subcategory_box = QComboBox(self.horizontalLayoutWidget_3)
        self.subcategory_box.setObjectName(u"subcategory_box")
        self.subcategory_box.setMinimumSize(QSize(200, 0))
        self.subcategory_box.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_3.addWidget(self.subcategory_box)

        self.del_subcat = QToolButton(self.horizontalLayoutWidget_3)
        self.del_subcat.setObjectName(u"del_subcat")
        self.del_subcat.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.del_subcat)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.subcategory_name = QLineEdit(self.horizontalLayoutWidget_3)
        self.subcategory_name.setObjectName(u"subcategory_name")
        self.subcategory_name.setMaximumSize(QSize(999, 16777215))

        self.horizontalLayout_4.addWidget(self.subcategory_name)

        self.add_subcategory = QPushButton(self.horizontalLayoutWidget_3)
        self.add_subcategory.setObjectName(u"add_subcategory")
        self.add_subcategory.setMinimumSize(QSize(160, 0))
        self.add_subcategory.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout_4.addWidget(self.add_subcategory)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 110, 331, 241))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pName = QLineEdit(self.formLayoutWidget)
        self.pName.setObjectName(u"pName")

        self.horizontalLayout_7.addWidget(self.pName)

        self.product_Box = QComboBox(self.formLayoutWidget)
        self.product_Box.setObjectName(u"product_Box")
        self.product_Box.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_7.addWidget(self.product_Box)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.pCost = QLineEdit(self.formLayoutWidget)
        self.pCost.setObjectName(u"pCost")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pCost)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.pCount = QLineEdit(self.formLayoutWidget)
        self.pCount.setObjectName(u"pCount")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pCount)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.pByu = QLineEdit(self.formLayoutWidget)
        self.pByu.setObjectName(u"pByu")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pByu)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.pPlace = QLineEdit(self.formLayoutWidget)
        self.pPlace.setObjectName(u"pPlace")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.pPlace)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.pBar = QLineEdit(self.formLayoutWidget)
        self.pBar.setObjectName(u"pBar")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.pBar)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.select_id = QLineEdit(self.formLayoutWidget)
        self.select_id.setObjectName(u"select_id")
        self.select_id.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.select_id)

        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(350, 110, 351, 241))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.pDiscripton = QPlainTextEdit(self.formLayoutWidget_2)
        self.pDiscripton.setObjectName(u"pDiscripton")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.pDiscripton)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(360, 360, 341, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.del_product = QPushButton(self.horizontalLayoutWidget_4)
        self.del_product.setObjectName(u"del_product")

        self.horizontalLayout_6.addWidget(self.del_product)

        self.add_product = QPushButton(self.horizontalLayoutWidget_4)
        self.add_product.setObjectName(u"add_product")

        self.horizontalLayout_6.addWidget(self.add_product)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 350, 331, 43))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.image_place = QLineEdit(self.horizontalLayoutWidget)
        self.image_place.setObjectName(u"image_place")
        self.image_place.setEnabled(True)
        self.image_place.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.image_place)

        self.pImage = QPushButton(self.horizontalLayoutWidget)
        self.pImage.setObjectName(u"pImage")

        self.horizontalLayout_5.addWidget(self.pImage)

        self.upd_btn = QToolButton(self.centralwidget)
        self.upd_btn.setObjectName(u"upd_btn")
        self.upd_btn.setGeometry(QRect(670, 20, 28, 28))
        icon1 = QIcon()
        icon1.addFile(u"../telegram_shop_python/SVG/reload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.upd_btn.setIcon(icon1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 720, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.del_cat.setText("")
        self.add_category.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.del_subcat.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.add_subcategory.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0443\u043f\u043a\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"BAR code", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d ID", None))
        self.select_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.pDiscripton.setPlainText("")
        self.del_product.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.add_product.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
        self.pImage.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0444\u043e\u0442\u043e", None))
        self.upd_btn.setText("")
    # retranslateUi

