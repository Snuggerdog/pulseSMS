from PyQt6.QtWidgets import QWidget, QCheckBox
from PyQt6.QtCore import pyqtSignal, QSettings
from pulsesmsreboot.view.advanced_page import Ui_Advanced
from gettext import gettext as _
from .tools import updateTextCheckBox
import pulsesmsreboot


class Advanced(QWidget, Ui_Advanced):

    emitHideSettingsBar = pyqtSignal()
    emiHideNotificationCounter = pyqtSignal()

    def __init__(self):
        super(Advanced, self).__init__()
        self.setupUi(self)

        self.settings = QSettings(pulsesmsreboot.__appname__, pulsesmsreboot.__appname__)
        self.load()
        self.setActionCheckBox()

    def load(self):
        self.hideBarUsers.setChecked(self.settings.value(
            "system/hide_bar_users", False, bool))
        self.donationMessage.setChecked(self.settings.value(
            "system/donation_message", True, bool))
        self.backgroundMessage.setChecked(self.settings.value(
            "system/background_message", True, bool))
        self.folderDownloads.setChecked(self.settings.value(
            "system/folderDownloads", False, bool))
        self.notificationCounter.setChecked(self.settings.value(
            "system/notificationCounter", True, bool))

    def setLabelFolderDownloads(self):
        if (self.settings.value(
                "system/folderDownloads", False, bool)):
            self.labelFolderDownloads.setText(_("Standard folder ~/Downloads"))
        else:
            self.labelFolderDownloads.setText(
                _("Standard folder ~/Downloads/PulseSMSReboot Downloads"))

    def save(self):
        self.settings.setValue("system/hide_bar_users",
                               self.hideBarUsers.isChecked())
        self.settings.setValue("system/donation_message",
                               self.donationMessage.isChecked())
        self.settings.setValue("system/background_message",
                               self.backgroundMessage.isChecked())
        self.settings.setValue("system/folderDownloads",
                               self.folderDownloads.isChecked())
        self.settings.setValue("system/notificationCounter",
                               self.notificationCounter.isChecked())
        
        self.setLabelFolderDownloads()

    def setActionCheckBox(self):
        for children in self.findChildren(QCheckBox):
            children.clicked.connect(self.checkClick)
            updateTextCheckBox(children)

    def checkClick(self):
        children = self.sender()

        updateTextCheckBox(children)
        self.save()

        childrenName = children.objectName()
        if childrenName == 'hideBarUsers':
            self.emitHideSettingsBar.emit()
        elif childrenName =='notificationCounter':
            self.emiHideNotificationCounter.emit()
