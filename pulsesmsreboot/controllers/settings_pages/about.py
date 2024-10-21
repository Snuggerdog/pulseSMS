from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QUrl, pyqtSignal
from PyQt6.QtGui import QDesktopServices
from pulsesmsreboot.view.about_page import Ui_About
from gettext import gettext as _
import pulsesmsreboot
from pulsesmsreboot.theme.builder_icon import getImageQPixmap


class About(QWidget, Ui_About):

    emitCloseSettings = pyqtSignal()

    def __init__(self):
        super(About, self).__init__()
        self.setupUi(self)

        self.version_app.setText(
            _(self.version_app.text()).format(id=pulsesmsreboot.__version__))
        # actions

        def leanMore():
            QDesktopServices.openUrl(QUrl(pulsesmsreboot.__website__))
            self.emitCloseSettings.emit()
        self.btnLeanMore.clicked.connect(leanMore)

        #def reportIssue():
        #    QDesktopServices.openUrl(QUrl(pulsesmsreboot.__bugreport__))
        #    self.emitCloseSettings.emit()
       # self.btnReportIssue.clicked.connect(reportIssue)
