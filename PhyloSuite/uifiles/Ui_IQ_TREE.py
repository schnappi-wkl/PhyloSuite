# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Work\python\bioinfo_excercise\PhyloSuite\PhyloSuite\PhyloSuite\uifiles\IQ_TREE.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IQTREE(object):
    def setupUi(self, IQTREE):
        IQTREE.setObjectName("IQTREE")
        IQTREE.resize(584, 674)
        self.verticalLayout = QtWidgets.QVBoxLayout(IQTREE)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(IQTREE)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 566, 656))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.comboBox_11 = ListQCombobox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_11.sizePolicy().hasHeightForWidth())
        self.comboBox_11.setSizePolicy(sizePolicy)
        self.comboBox_11.setAcceptDrops(True)
        self.comboBox_11.setEditable(True)
        self.comboBox_11.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_11.setObjectName("comboBox_11")
        self.gridLayout_2.addWidget(self.comboBox_11, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 26))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 26))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_2.addWidget(self.checkBox_8, 1, 0, 1, 1)
        self.lineEdit_3 = InputQLineEdit(self.groupBox_4)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_22.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setMinimumSize(QtCore.QSize(30, 26))
        self.pushButton_22.setMaximumSize(QtCore.QSize(30, 26))
        self.pushButton_22.setStyleSheet("")
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_2.addWidget(self.pushButton_22, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 3, 0, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_9.sizePolicy().hasHeightForWidth())
        self.comboBox_9.setSizePolicy(sizePolicy)
        self.comboBox_9.setMinimumSize(QtCore.QSize(114, 26))
        self.comboBox_9.setMaximumSize(QtCore.QSize(16777215, 26))
        self.comboBox_9.setStyleSheet("")
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_9, 3, 1, 1, 2)
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_9.setChecked(True)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_2.addWidget(self.checkBox_9, 4, 0, 1, 1)
        self.comboBox_10 = CheckableComboBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_10.sizePolicy().hasHeightForWidth())
        self.comboBox_10.setSizePolicy(sizePolicy)
        self.comboBox_10.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_10.setObjectName("comboBox_10")
        self.gridLayout_2.addWidget(self.comboBox_10, 4, 1, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setOpenExternalLinks(True)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.label = ClickedLableGif(self.groupBox_4)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 5, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_5)
        self.label_24 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_3.addWidget(self.label_24)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 1, 1, 2)
        self.gridLayout_5.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setToolTip("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 0, 0, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy)
        self.comboBox_7.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_7.setObjectName("comboBox_7")
        self.gridLayout.addWidget(self.comboBox_7, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_29 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_4.addWidget(self.label_29)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_4.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_4.addWidget(self.checkBox_4)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setAutoRepeat(False)
        self.checkBox_2.setAutoExclusive(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 2, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy)
        self.comboBox_6.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout.addWidget(self.comboBox_6, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_2.addWidget(self.label_28)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(64)
        self.spinBox.setProperty("value", 4)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_30 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.gridLayout_4.addWidget(self.label_30, 0, 0, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_8.sizePolicy().hasHeightForWidth())
        self.comboBox_8.setSizePolicy(sizePolicy)
        self.comboBox_8.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_8, 0, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.gridLayout_4.addWidget(self.label_35, 0, 2, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy)
        self.spinBox_3.setMinimum(100)
        self.spinBox_3.setMaximum(1000000)
        self.spinBox_3.setSingleStep(10)
        self.spinBox_3.setProperty("value", 5000)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_4.addWidget(self.spinBox_3, 0, 3, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.gridLayout_4.addWidget(self.label_36, 1, 0, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_4.sizePolicy().hasHeightForWidth())
        self.spinBox_4.setSizePolicy(sizePolicy)
        self.spinBox_4.setMinimum(1000)
        self.spinBox_4.setMaximum(100000000)
        self.spinBox_4.setSingleStep(100)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_4.addWidget(self.spinBox_4, 1, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.gridLayout_4.addWidget(self.label_37, 1, 2, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy)
        self.doubleSpinBox.setMinimum(0.9)
        self.doubleSpinBox.setMaximum(0.99)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_4.addWidget(self.doubleSpinBox, 1, 3, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_4.addWidget(self.checkBox_6, 2, 0, 1, 2)
        self.label_38 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_38.setFont(font)
        self.label_38.setToolTip("")
        self.label_38.setObjectName("label_38")
        self.gridLayout_4.addWidget(self.label_38, 2, 2, 1, 1)
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_5.sizePolicy().hasHeightForWidth())
        self.spinBox_5.setSizePolicy(sizePolicy)
        self.spinBox_5.setToolTip("")
        self.spinBox_5.setMinimum(1000)
        self.spinBox_5.setMaximum(100000000)
        self.spinBox_5.setSingleStep(100)
        self.spinBox_5.setObjectName("spinBox_5")
        self.gridLayout_4.addWidget(self.spinBox_5, 2, 3, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_4.addWidget(self.checkBox_7, 3, 0, 1, 2)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_4.addWidget(self.checkBox_5, 3, 2, 1, 2)
        self.gridLayout_5.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/resourses/if_Delete_1493279.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton = ArrowPushButton(self.groupBox_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/picture/resourses/if_start_60207.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 3, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_6)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/picture/resourses/Eye_Care_Services-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_7.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_6)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_7.addWidget(self.progressBar, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_6, 4, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.label_24.setBuddy(self.comboBox_3)

        self.retranslateUi(IQTREE)
        self.checkBox_2.toggled['bool'].connect(self.checkBox_3.setDisabled)
        self.checkBox_2.toggled['bool'].connect(self.checkBox_4.setDisabled)
        self.checkBox_6.toggled['bool'].connect(self.spinBox_5.setEnabled)
        self.checkBox_6.toggled['bool'].connect(self.label_38.setEnabled)
        self.checkBox_2.toggled['bool'].connect(self.label_29.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(IQTREE)
        IQTREE.setTabOrder(self.pushButton_3, self.lineEdit_3)
        IQTREE.setTabOrder(self.lineEdit_3, self.pushButton_9)
        IQTREE.setTabOrder(self.pushButton_9, self.pushButton_22)
        IQTREE.setTabOrder(self.pushButton_22, self.pushButton_2)
        IQTREE.setTabOrder(self.pushButton_2, self.pushButton)

    def retranslateUi(self, IQTREE):
        _translate = QtCore.QCoreApplication.translate
        IQTREE.setWindowTitle(_translate("IQTREE", "IQ-TREE"))
        self.groupBox_4.setTitle(_translate("IQTREE", "Input"))
        self.label_5.setText(_translate("IQTREE", "Alignment File:"))
        self.checkBox_8.setText(_translate("IQTREE", "Partition Mode:"))
        self.lineEdit_3.setPlaceholderText(_translate("IQTREE", "Optional!"))
        self.label_8.setText(_translate("IQTREE", "Partition Style:"))
        self.label_22.setText(_translate("IQTREE", "Code Table:"))
        self.comboBox_9.setItemText(0, _translate("IQTREE", "1 The standard code"))
        self.comboBox_9.setItemText(1, _translate("IQTREE", "2 Vertebrate mitochondrial code"))
        self.comboBox_9.setItemText(2, _translate("IQTREE", "3 The Yeast Mitochondrial Code"))
        self.comboBox_9.setItemText(3, _translate("IQTREE", "4 Mold, Protozoan, and Coelenterate Mitochondrial code and Mycoplasma/Spiroplasma code"))
        self.comboBox_9.setItemText(4, _translate("IQTREE", "5 Invertebrate mitochondrial"))
        self.comboBox_9.setItemText(5, _translate("IQTREE", "6 The Ciliate, Dasycladacean and Hexamita Nuclear Code"))
        self.comboBox_9.setItemText(6, _translate("IQTREE", "9 Echinoderm and Flatworm mitochondrial code"))
        self.comboBox_9.setItemText(7, _translate("IQTREE", "10 The Euplotid Nuclear Code"))
        self.comboBox_9.setItemText(8, _translate("IQTREE", "11 The Bacterial, Archaeal and Plant Plastid Code"))
        self.comboBox_9.setItemText(9, _translate("IQTREE", "12 The Alternative Yeast Nuclear Code"))
        self.comboBox_9.setItemText(10, _translate("IQTREE", "13 Ascidian mitochondrial code"))
        self.comboBox_9.setItemText(11, _translate("IQTREE", "14 Alternative flatworm mitochondrial code"))
        self.comboBox_9.setItemText(12, _translate("IQTREE", "16 Chlorophycean Mitochondrial Code"))
        self.comboBox_9.setItemText(13, _translate("IQTREE", "21 Trematode Mitochondrial Code"))
        self.comboBox_9.setItemText(14, _translate("IQTREE", "22 Scenedesmus obliquus Mitochondrial Code"))
        self.comboBox_9.setItemText(15, _translate("IQTREE", "23 Thraustochytrium Mitochondrial Code"))
        self.comboBox_9.setItemText(16, _translate("IQTREE", "24 Pterobranchia Mitochondrial Code"))
        self.comboBox_9.setItemText(17, _translate("IQTREE", "25 Candidate Division SR1 and Gracilibacteria Code"))
        self.checkBox_9.setText(_translate("IQTREE", "Outgroup (s):"))
        self.label_14.setText(_translate("IQTREE", "<html><head/><body><p>Click <a href=\"http://www.iqtree.org/doc/\"><span style=\" text-decoration: underline; color:#0000ff;\">here</span></a> to learn more about <span style=\" font-weight:600; color:#ff0000;\">IQ-TREE</span></p></body></html>"))
        self.label.setToolTip(_translate("IQTREE", "Brief example"))
        self.comboBox_5.setItemText(0, _translate("IQTREE", "Edge-linked"))
        self.comboBox_5.setItemText(1, _translate("IQTREE", "Edge-unlinked"))
        self.label_24.setText(_translate("IQTREE", "Seq. Type:"))
        self.comboBox_3.setItemText(0, _translate("IQTREE", "Auto detect"))
        self.comboBox_3.setItemText(1, _translate("IQTREE", "DNA"))
        self.comboBox_3.setItemText(2, _translate("IQTREE", "Protein"))
        self.comboBox_3.setItemText(3, _translate("IQTREE", "Codon"))
        self.comboBox_3.setItemText(4, _translate("IQTREE", "Binary"))
        self.comboBox_3.setItemText(5, _translate("IQTREE", "Morphology"))
        self.comboBox_3.setItemText(6, _translate("IQTREE", "DNA-->AA"))
        self.groupBox.setTitle(_translate("IQTREE", "Substitution Model Options"))
        self.label_25.setText(_translate("IQTREE", "Models:"))
        self.label_29.setText(_translate("IQTREE", "Rate heterogeneity:"))
        self.checkBox_3.setToolTip(_translate("IQTREE", "Discrete Gamma model"))
        self.checkBox_3.setText(_translate("IQTREE", "[+G]"))
        self.checkBox_4.setToolTip(_translate("IQTREE", "Allowing for a proportion of invariable sites"))
        self.checkBox_4.setText(_translate("IQTREE", "[+I]"))
        self.label_26.setText(_translate("IQTREE", "State freq:"))
        self.comboBox_4.setItemText(0, _translate("IQTREE", "Empirical (from data)"))
        self.comboBox_4.setItemText(1, _translate("IQTREE", "AA model (from matrix)"))
        self.comboBox_4.setItemText(2, _translate("IQTREE", "ML-optimized"))
        self.comboBox_4.setItemText(3, _translate("IQTREE", "Codon F1X4"))
        self.comboBox_4.setItemText(4, _translate("IQTREE", "Codon F3X4"))
        self.checkBox_2.setText(_translate("IQTREE", "FreeRate heterogeneity [+R]"))
        self.checkBox.setToolTip(_translate("IQTREE", "Ascertainment bias correction"))
        self.checkBox.setText(_translate("IQTREE", "[+ASC]"))
        self.label_27.setText(_translate("IQTREE", "Threads:"))
        self.label_28.setText(_translate("IQTREE", "#rate categories:"))
        self.groupBox_2.setTitle(_translate("IQTREE", "Branch Support Analysis"))
        self.label_30.setToolTip(_translate("IQTREE", "Bootstrap analysis"))
        self.label_30.setText(_translate("IQTREE", "Bootstrap:"))
        self.comboBox_8.setItemText(0, _translate("IQTREE", "Ultrafast"))
        self.comboBox_8.setItemText(1, _translate("IQTREE", "Standard"))
        self.comboBox_8.setItemText(2, _translate("IQTREE", "None"))
        self.label_35.setText(_translate("IQTREE", "Num of bootstrap:"))
        self.label_36.setToolTip(_translate("IQTREE", "Maximum iterations"))
        self.label_36.setText(_translate("IQTREE", "Max. iter.:"))
        self.spinBox_4.setToolTip(_translate("IQTREE", "Maximum iterations"))
        self.label_37.setToolTip(_translate("IQTREE", "Minimum correlation coefficient"))
        self.label_37.setText(_translate("IQTREE", "Minimum cor. coef.:"))
        self.doubleSpinBox.setToolTip(_translate("IQTREE", "Minimum correlation coefficient"))
        self.checkBox_6.setText(_translate("IQTREE", "SH-aLRT branch test"))
        self.label_38.setText(_translate("IQTREE", "#replicates:"))
        self.checkBox_7.setText(_translate("IQTREE", "Approximate Bayes test"))
        self.checkBox_5.setToolTip(_translate("IQTREE", "Write bootstrap trees to .ufboot file"))
        self.checkBox_5.setText(_translate("IQTREE", "Create .ufboot file"))
        self.groupBox_3.setTitle(_translate("IQTREE", "Run"))
        self.pushButton_2.setText(_translate("IQTREE", "Stop"))
        self.pushButton.setText(_translate("IQTREE", "Start"))
        self.groupBox_6.setTitle(_translate("IQTREE", "Progress"))
        self.pushButton_9.setText(_translate("IQTREE", "Show log"))

from src.CustomWidget import ArrowPushButton, CheckableComboBox, ClickedLableGif, InputQLineEdit, ListQCombobox
from uifiles import myRes_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IQTREE = QtWidgets.QDialog()
    ui = Ui_IQTREE()
    ui.setupUi(IQTREE)
    IQTREE.show()
    sys.exit(app.exec_())

