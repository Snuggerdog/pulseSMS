from PyQt6.QtWidgets import QWidget, QApplication, QPushButton
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import pyqtSignal
from pulsesmsreboot.view.settings import Ui_Settings
from pulsesmsreboot.controllers.settings_pages.general import General
from pulsesmsreboot.controllers.settings_pages.account import Account
from pulsesmsreboot.controllers.settings_pages.notifications import Notifications
from pulsesmsreboot.controllers.settings_pages.personalization import Personalization
from pulsesmsreboot.controllers.settings_pages.advanced import Advanced
from pulsesmsreboot.controllers.settings_pages.about import About
from pulsesmsreboot.controllers.settings_pages.network import Network
from pulsesmsreboot.model.user import User
from gettext import gettext as _
import pulsesmsreboot


class Settings(QWidget, Ui_Settings):

    pages_id = {}

    # account
    emitDisableUser = pyqtSignal(User)
    emitDeleteUser = pyqtSignal(User)
    emitEditUser = pyqtSignal(User)
    emitNewtUser = pyqtSignal(User)

    # personalization
    emitUpdateTheme = pyqtSignal(str)
    emitDisableTrayIcon = pyqtSignal(bool)
    emitNotifications = pyqtSignal()

    # avanced
    emitHideSettingsBar = pyqtSignal()
    emiHideNotificationCounter = pyqtSignal()

    # Quit
    emitQuit = pyqtSignal()
    emitCloseSettings = pyqtSignal()

    # PulseSMS Settings
    emitOpenSettingsPulseSMS = pyqtSignal()

    # Set Proxy
    emitUpdateProxyPage = pyqtSignal()

    def __init__(self, parent=None):
        super(Settings, self).__init__()
        self.setupUi(self)
        self.setParent(parent)

        self.setDefaultEventButtonInMenu()
        self.setPages()

        self.btn_close.clicked.connect(self.emitCloseSettings.emit)

        self.btn_general.setStyleSheet(
            self.selectMenu(self.btn_general.styleSheet()))

    def setPages(self):
        # General
        self.generalPage = General()
        self.generalPage.emitOpenSettingsPulseSMS = self.emitOpenSettingsPulseSMS
        self.pages_id['btn_general'] = self.settings_stacked.addWidget(
            self.generalPage)

        # Account
        self.accountPage = Account()
        self.accountPage.emitDisableUser = self.emitDisableUser
        self.accountPage.emitDeleteUser = self.emitDeleteUser
        self.accountPage.emitEditUser = self.emitEditUser
        self.accountPage.emitNewtUser = self.emitNewtUser
        self.pages_id['btn_account'] = self.settings_stacked.addWidget(
            self.accountPage)

        # Notifications
        self.pages_id['btn_notifications'] = self.settings_stacked.addWidget(
            Notifications())

        # Personalization
        self.persoPage = Personalization()
        self.persoPage.emitUpdateTheme = self.emitUpdateTheme
        self.persoPage.emitDisableTrayIcon = self.emitDisableTrayIcon
        self.persoPage.emitNotifications = self.emitNotifications
        self.pages_id['btn_personalization'] = self.settings_stacked.addWidget(
            self.persoPage)

        # Avanced mode
        self.avanced_page = Advanced()
        self.avanced_page.emitHideSettingsBar = self.emitHideSettingsBar
        self.avanced_page.emiHideNotificationCounter = self.emiHideNotificationCounter
        self.pages_id['btn_advanced'] = self.settings_stacked.addWidget(
            self.avanced_page)


        # About
        self.aboutPage = About()
        self.aboutPage.emitCloseSettings = self.emitCloseSettings
        self.pages_id['btn_about'] = self.settings_stacked.addWidget(
            self.aboutPage)

        # Network
        self.networkPage = Network()
        self.networkPage.emitUpdateProxyPage = self.emitUpdateProxyPage
        self.pages_id['btn_network'] = self.settings_stacked.addWidget(
            self.networkPage)

    def setDefaultEventButtonInMenu(self):
        for item in self.menu.findChildren(QPushButton):
            item.clicked.connect(self.buttonClick)

    def buttonClick(self):
        btn = self.sender()  # returns a pointer to the object that sent the signal
        btnName = btn.objectName()
        self.resetStyle(btnName)
        try:
            self.settings_stacked.setCurrentIndex(self.pages_id[btnName])

            btn.setStyleSheet(self.selectMenu(btn.styleSheet()))

        except Exception as e:
            self.emitQuit.emit()


    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    # MENU SELECTED STYLESHEET
    MENU_SELECTED_STYLESHEET = """
    font-weight: bold;
    """

    def selectMenu(self, getStyle):
        select = getStyle + self.MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(self, getStyle):
        deselect = getStyle.replace(self.MENU_SELECTED_STYLESHEET, "")
        return deselect

    # RESET SELECTION
    def resetStyle(self, widget):
        for w in self.menu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(self.deselectMenu(w.styleSheet()))
