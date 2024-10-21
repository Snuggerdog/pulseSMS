from pulsesmsreboot import __version__, __appname__, __comment__, isFlatpak
from PyQt6.QtCore import QStandardPaths
import os
import dbus

path_data = QStandardPaths.writableLocation(
    QStandardPaths.StandardLocation.ConfigLocation)+'/autostart/com.snuggerdog.pulsesmsreboot.desktop'


def createDesktopFile(typeAction):

    if isFlatpak:
        generateFlatpak(typeAction)
    else:
        generateLocal(typeAction)


def generateFlatpak(typeAction):
    try:
        bus = dbus.SessionBus()
        obj = bus.get_object("org.freedesktop.portal.Desktop",
                             "/org/freedesktop/portal/desktop")
        inter = dbus.Interface(obj, "org.freedesktop.portal.Background")

        res = inter.RequestBackground('', {'reason': 'PulseSMSReboot autostart', 'autostart': typeAction,
                                           'background': typeAction, 'commandline': dbus.Array(['pulsesmsreboot', '--hideStart'])})

    except Exception as e:
        print(e)


def generateLocal(typeAction):
    if typeAction:  # create
        createDesktopLocal()
    else:
        removeDesktopLocal()


def createDesktopLocal():

    conteudo = f"""[Desktop Entry]
Version=1.0
Name=PulseSMSReboot
Comment=PulseSMS Desktop app for Linux
Exec=pulsesmsreboot %u --hideStart
Icon=com.snuggerdog.pulsesmsreboot
Type=Application
Categories=Chat;Network;InstantMessaging;Qt;
Keywords=PulseSMS;Chat;Pulse;
StartupWMClass=pulsesms
MimeType=x-scheme-handler/pulsesms
Terminal=false
SingleMainWindow=true
X-GNOME-UsesNotifications=true
X-GNOME-SingleWindow=true"""

    with open(path_data, 'w') as arquivo:
        arquivo.write(conteudo)


def removeDesktopLocal():
    if os.path.exists(path_data):
        os.remove(path_data)
