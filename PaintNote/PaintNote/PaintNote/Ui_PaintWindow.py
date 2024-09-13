# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PaintWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QStatusBar,
    QToolBar, QVBoxLayout, QWidget)

from PaintNote.PaintNote.PaintNote.PaintingArea import PaintingArea

class Ui_PaintWindow(object):
    def setupUi(self, PaintWindow):
        if not PaintWindow.objectName():
            PaintWindow.setObjectName(u"PaintWindow")
        PaintWindow.resize(1036, 680)
        self.centralwidget = QWidget(PaintWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.canvas = PaintingArea(self.centralwidget)
        self.canvas.setObjectName(u"canvas")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setMinimumSize(QSize(200, 200))

        self.verticalLayout.addWidget(self.canvas)

        PaintWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(PaintWindow)
        self.statusbar.setObjectName(u"statusbar")
        PaintWindow.setStatusBar(self.statusbar)
        self.toolbar = QToolBar(PaintWindow)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMovable(False)
        self.toolbar.setIconSize(QSize(32, 32))
        self.toolbar.setFloatable(False)
        PaintWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)

        self.retranslateUi(PaintWindow)

        QMetaObject.connectSlotsByName(PaintWindow)
    # setupUi

    def retranslateUi(self, PaintWindow):
        PaintWindow.setWindowTitle(QCoreApplication.translate("PaintWindow", u"MainWindow", None))
        self.toolbar.setWindowTitle(QCoreApplication.translate("PaintWindow", u"toolBar", None))
    # retranslateUi

