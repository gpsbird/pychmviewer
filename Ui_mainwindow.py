# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri Dec 17 14:59:07 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(873, 591)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pychmviewer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.widget = QtGui.QWidget(MainWindow)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        #self.WebViewsWidget = PyChmTabs(self.widget)
        #self.WebViewsWidget.setObjectName(_fromUtf8("WebViewsWidget"))
        #self.horizontalLayout.addWidget(self.WebViewsWidget)
        MainWindow.setCentralWidget(self.widget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuPanels = QtGui.QMenu(self.menubar)
        self.menuPanels.setObjectName(_fromUtf8("menuPanels"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuTabs = QtGui.QMenu(self.menubar)
        self.menuTabs.setObjectName(_fromUtf8("menuTabs"))
        self.menuBookmarks = QtGui.QMenu(self.menubar)
        self.menuBookmarks.setObjectName(_fromUtf8("menuBookmarks"))
        MainWindow.setMenuBar(self.menubar)
        self.mainToolbar = QtGui.QToolBar(MainWindow)
        self.mainToolbar.setOrientation(QtCore.Qt.Horizontal)
        self.mainToolbar.setObjectName(_fromUtf8("mainToolbar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolbar)
        self.navToolbar = QtGui.QToolBar(MainWindow)
        self.navToolbar.setOrientation(QtCore.Qt.Horizontal)
        self.navToolbar.setObjectName(_fromUtf8("navToolbar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.navToolbar)
        self.viewToolbar = QtGui.QToolBar(MainWindow)
        self.viewToolbar.setOrientation(QtCore.Qt.Horizontal)
        self.viewToolbar.setObjectName(_fromUtf8("viewToolbar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.viewToolbar)
        self.mainStatusBar = QtGui.QStatusBar(MainWindow)
        self.mainStatusBar.setObjectName(_fromUtf8("mainStatusBar"))
        MainWindow.setStatusBar(self.mainStatusBar)
        self.dockTopics = QtGui.QDockWidget(MainWindow)
        self.dockTopics.setAcceptDrops(False)
        self.dockTopics.setAccessibleDescription(_fromUtf8(""))
        self.dockTopics.setObjectName(_fromUtf8("dockTopics"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.dockTopics.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockTopics)
        self.dockIndex = QtGui.QDockWidget(MainWindow)
        self.dockIndex.setObjectName(_fromUtf8("dockIndex"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.dockIndex.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockIndex)
        self.dockSearch = QtGui.QDockWidget(MainWindow)
        self.dockSearch.setObjectName(_fromUtf8("dockSearch"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.dockSearch.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockSearch)
        self.dockBookmark = QtGui.QDockWidget(MainWindow)
        self.dockBookmark.setAccessibleName(_fromUtf8(""))
        self.dockBookmark.setObjectName(_fromUtf8("dockBookmark"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.dockBookmark.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockBookmark)
        self.actionPrintPage = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon_print.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrintPage.setIcon(icon1)
        self.actionPrintPage.setObjectName(_fromUtf8("actionPrintPage"))
        self.actionOpenSettings = QtGui.QAction(MainWindow)
        self.actionOpenSettings.setObjectName(_fromUtf8("actionOpenSettings"))
        self.actionAddBookmark = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon_add_bookmark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddBookmark.setIcon(icon2)
        self.actionAddBookmark.setObjectName(_fromUtf8("actionAddBookmark"))
        self.actionZoomIn = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon_font_increase.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomIn.setIcon(icon3)
        self.actionZoomIn.setObjectName(_fromUtf8("actionZoomIn"))
        self.actionZoomOut = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon_font_decrease.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomOut.setIcon(icon4)
        self.actionZoomOut.setObjectName(_fromUtf8("actionZoomOut"))
        self.actionZoomOff = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon_font_norm.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoomOff.setIcon(icon5)
        self.actionZoomOff.setObjectName(_fromUtf8("actionZoomOff"))
        self.actionViewHtmlSource = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon_view_source.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionViewHtmlSource.setIcon(icon6)
        self.actionViewHtmlSource.setObjectName(_fromUtf8("actionViewHtmlSource"))
        self.actionLocate = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon_locate_in_content.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLocate.setIcon(icon7)
        self.actionLocate.setObjectName(_fromUtf8("actionLocate"))
        self.actionChangeEncoding = QtGui.QAction(MainWindow)
        self.actionChangeEncoding.setObjectName(_fromUtf8("actionChangeEncoding"))
        self.actionOpenFile = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon_open_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenFile.setIcon(icon8)
        self.actionOpenFile.setObjectName(_fromUtf8("actionOpenFile"))
        self.actionGoBack = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon_back.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoBack.setIcon(icon9)
        self.actionGoBack.setObjectName(_fromUtf8("actionGoBack"))
        self.actionGoForward = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon_forward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoForward.setIcon(icon10)
        self.actionGoForward.setObjectName(_fromUtf8("actionGoForward"))
        self.actionGoHome = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon_home.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGoHome.setIcon(icon11)
        self.actionGoHome.setObjectName(_fromUtf8("actionGoHome"))
        self.actionAboutApp = QtGui.QAction(MainWindow)
        self.actionAboutApp.setObjectName(_fromUtf8("actionAboutApp"))
        self.actionExtractFile = QtGui.QAction(MainWindow)
        self.actionExtractFile.setObjectName(_fromUtf8("actionExtractFile"))
        self.actionQuitApp = QtGui.QAction(MainWindow)
        self.actionQuitApp.setObjectName(_fromUtf8("actionQuitApp"))
        self.actionTogglePanels = QtGui.QAction(MainWindow)
        self.actionTogglePanels.setObjectName(_fromUtf8("actionTogglePanels"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionSelectAll = QtGui.QAction(MainWindow)
        self.actionSelectAll.setObjectName(_fromUtf8("actionSelectAll"))
        self.actionFind = QtGui.QAction(MainWindow)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.actionFindNext = QtGui.QAction(MainWindow)
        self.actionFindNext.setObjectName(_fromUtf8("actionFindNext"))
        self.actionFindPrevious = QtGui.QAction(MainWindow)
        self.actionFindPrevious.setObjectName(_fromUtf8("actionFindPrevious"))
        self.actionOpenNewTab = QtGui.QAction(MainWindow)
        self.actionOpenNewTab.setObjectName(_fromUtf8("actionOpenNewTab"))
        self.actionCloseCurrentTab = QtGui.QAction(MainWindow)
        self.actionCloseCurrentTab.setObjectName(_fromUtf8("actionCloseCurrentTab"))
        self.actionAboutQt = QtGui.QAction(MainWindow)
        self.actionAboutQt.setObjectName(_fromUtf8("actionAboutQt"))
        self.actionOpenRecents = QtGui.QAction(MainWindow)
        self.actionOpenRecents.setObjectName(_fromUtf8("actionOpenRecents"))
        self.actionEditBookmark = QtGui.QAction(MainWindow)
        self.actionEditBookmark.setObjectName(_fromUtf8("actionEditBookmark"))
        self.actionDeleteBookmark = QtGui.QAction(MainWindow)
        self.actionDeleteBookmark.setObjectName(_fromUtf8("actionDeleteBookmark"))
        self.menuSettings.addAction(self.actionOpenSettings)
        self.menuFile.addAction(self.actionOpenFile)
        self.menuFile.addAction(self.actionOpenRecents)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrintPage)
        self.menuFile.addAction(self.actionExtractFile)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuitApp)
        self.menuView.addAction(self.actionZoomIn)
        self.menuView.addAction(self.actionZoomOut)
        self.menuView.addAction(self.actionZoomOff)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionChangeEncoding)
        self.menuView.addAction(self.actionViewHtmlSource)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionLocate)
        self.menuView.addSeparator()
        self.menuPanels.addAction(self.actionTogglePanels)
        self.menuPanels.addSeparator()
        self.menuHelp.addAction(self.actionAboutApp)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionSelectAll)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFindNext)
        self.menuEdit.addAction(self.actionFindPrevious)
        self.menuTabs.addAction(self.actionOpenNewTab)
        self.menuTabs.addAction(self.actionCloseCurrentTab)
        self.menuTabs.addSeparator()
        self.menuBookmarks.addAction(self.actionAddBookmark)
        self.menuBookmarks.addAction(self.actionEditBookmark)
        self.menuBookmarks.addAction(self.actionDeleteBookmark)
        self.menuBookmarks.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuPanels.menuAction())
        self.menubar.addAction(self.menuBookmarks.menuAction())
        self.menubar.addAction(self.menuTabs.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.mainToolbar.addAction(self.actionOpenFile)
        self.mainToolbar.addAction(self.actionPrintPage)
        self.navToolbar.addAction(self.actionGoHome)
        self.navToolbar.addAction(self.actionGoBack)
        self.navToolbar.addAction(self.actionGoForward)
        self.viewToolbar.addAction(self.actionLocate)
        self.viewToolbar.addAction(self.actionZoomIn)
        self.viewToolbar.addAction(self.actionZoomOut)
        self.viewToolbar.addAction(self.actionZoomOff)
        self.viewToolbar.addAction(self.actionViewHtmlSource)
        self.viewToolbar.addAction(self.actionAddBookmark)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "pychmviewer", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSettings.setTitle(QtGui.QApplication.translate("MainWindow", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "&View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPanels.setTitle(QtGui.QApplication.translate("MainWindow", "&Panels", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTabs.setTitle(QtGui.QApplication.translate("MainWindow", "&Tabs", None, QtGui.QApplication.UnicodeUTF8))
        self.menuBookmarks.setTitle(QtGui.QApplication.translate("MainWindow", "&Bookmarks", None, QtGui.QApplication.UnicodeUTF8))
        self.mainToolbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "general toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.navToolbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "navigation toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.viewToolbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "action toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.dockTopics.setStatusTip(QtGui.QApplication.translate("MainWindow", "Topics", None, QtGui.QApplication.UnicodeUTF8))
        self.dockTopics.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Topics", None, QtGui.QApplication.UnicodeUTF8))
        self.dockIndex.setStatusTip(QtGui.QApplication.translate("MainWindow", "Index", None, QtGui.QApplication.UnicodeUTF8))
        self.dockIndex.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Index", None, QtGui.QApplication.UnicodeUTF8))
        self.dockSearch.setStatusTip(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.dockSearch.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.dockBookmark.setStatusTip(QtGui.QApplication.translate("MainWindow", "Bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.dockBookmark.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrintPage.setText(QtGui.QApplication.translate("MainWindow", "&Print...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrintPage.setIconText(QtGui.QApplication.translate("MainWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrintPage.setToolTip(QtGui.QApplication.translate("MainWindow", "Print current page", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrintPage.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Prints currently opened page.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrintPage.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenSettings.setText(QtGui.QApplication.translate("MainWindow", "&Application settings...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenSettings.setToolTip(QtGui.QApplication.translate("MainWindow", "Change the application settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenSettings.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Change the application settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddBookmark.setText(QtGui.QApplication.translate("MainWindow", "&Add bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddBookmark.setToolTip(QtGui.QApplication.translate("MainWindow", "Adds a bookmark for currently opened page", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddBookmark.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Adds a bookmark for currently opened page. Remembers the opened page, and scroll position. Bookmarks are accessible through Bookmarks menu or tab.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAddBookmark.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+B", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom &in", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomIn.setToolTip(QtGui.QApplication.translate("MainWindow", "Increase the font size", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomIn.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Increases the document font size.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomIn.setShortcut(QtGui.QApplication.translate("MainWindow", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom &out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOut.setToolTip(QtGui.QApplication.translate("MainWindow", "Decrease the font size", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOut.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Decreases the document font size.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOut.setShortcut(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOff.setText(QtGui.QApplication.translate("MainWindow", "Zoom &off", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOff.setToolTip(QtGui.QApplication.translate("MainWindow", "restore normal font size", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOff.setWhatsThis(QtGui.QApplication.translate("MainWindow", "set the document font size normal.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionZoomOff.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewHtmlSource.setText(QtGui.QApplication.translate("MainWindow", "&HTML Source", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewHtmlSource.setIconText(QtGui.QApplication.translate("MainWindow", "HTML source", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewHtmlSource.setToolTip(QtGui.QApplication.translate("MainWindow", "View HTML source of current page", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewHtmlSource.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Shows the HTML source of currently opened page", None, QtGui.QApplication.UnicodeUTF8))
        self.actionViewHtmlSource.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+U", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLocate.setText(QtGui.QApplication.translate("MainWindow", "&Locate ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLocate.setToolTip(QtGui.QApplication.translate("MainWindow", "Locate the current page in side panel", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLocate.setWhatsThis(QtGui.QApplication.translate("MainWindow", "If the current page is present in the Table of Contents, locate it there. ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLocate.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChangeEncoding.setText(QtGui.QApplication.translate("MainWindow", "&Encoding", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChangeEncoding.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Changes the current document encoding. ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenFile.setText(QtGui.QApplication.translate("MainWindow", "&Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenFile.setToolTip(QtGui.QApplication.translate("MainWindow", "Open a CHM file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenFile.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Opens a new CHM file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenFile.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoBack.setText(QtGui.QApplication.translate("MainWindow", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoBack.setToolTip(QtGui.QApplication.translate("MainWindow", "Navigate back", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoBack.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Navigate back in navigation history", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoForward.setText(QtGui.QApplication.translate("MainWindow", "Forward", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoForward.setToolTip(QtGui.QApplication.translate("MainWindow", "Navigate forward", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoForward.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Navigate forward in navigation history", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoHome.setText(QtGui.QApplication.translate("MainWindow", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoHome.setToolTip(QtGui.QApplication.translate("MainWindow", "Navigate home", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGoHome.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Navigate to the document Home page, as specified in the document.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutApp.setText(QtGui.QApplication.translate("MainWindow", "&About PyChmViewer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutApp.setShortcut(QtGui.QApplication.translate("MainWindow", "F1", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExtractFile.setText(QtGui.QApplication.translate("MainWindow", "&Extract", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExtractFile.setIconText(QtGui.QApplication.translate("MainWindow", "Extract", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExtractFile.setToolTip(QtGui.QApplication.translate("MainWindow", "Extract current CHM file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExtractFile.setWhatsThis(QtGui.QApplication.translate("MainWindow", "Extract current CHM ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExtractFile.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuitApp.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuitApp.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTogglePanels.setText(QtGui.QApplication.translate("MainWindow", "&Hide Panels", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTogglePanels.setShortcut(QtGui.QApplication.translate("MainWindow", "F2", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "&Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectAll.setText(QtGui.QApplication.translate("MainWindow", "&Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelectAll.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setText(QtGui.QApplication.translate("MainWindow", "&Find", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFind.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindNext.setText(QtGui.QApplication.translate("MainWindow", "Find &Next", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindNext.setShortcut(QtGui.QApplication.translate("MainWindow", "F3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindPrevious.setText(QtGui.QApplication.translate("MainWindow", "Find &Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFindPrevious.setShortcut(QtGui.QApplication.translate("MainWindow", "Shift+F3", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenNewTab.setText(QtGui.QApplication.translate("MainWindow", "&Open Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenNewTab.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+T", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCloseCurrentTab.setText(QtGui.QApplication.translate("MainWindow", "&Close Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCloseCurrentTab.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAboutQt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpenRecents.setText(QtGui.QApplication.translate("MainWindow", "Open &Recents", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditBookmark.setText(QtGui.QApplication.translate("MainWindow", "&Edit bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteBookmark.setText(QtGui.QApplication.translate("MainWindow", "&Delete bookmark", None, QtGui.QApplication.UnicodeUTF8))

from pychmtabs import PyChmTabs
import images_rc
