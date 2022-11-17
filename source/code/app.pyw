# This is the main file which imports all modules and
# after executing displays an App window
import sys
import os

from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

from utils.ui_commands import UI_Commands
from utils.ENV_VARS import PATH
from modules import *


class MainWindow:

    def __init__(self):
        """
        Setup the window, set the default screen 
        to index, track home button clicks
        and initialize modules.
        """

        self.ui = uic.loadUi(os.path.join(PATH, 'source', 'code', 'main.ui'))

        self.commands = UI_Commands(self.ui)
        self.commands.change_screen(self.ui.index)

        # Initialize modul portal and statistika
        self.portal = modul_portal.Portal(self.ui)
        self.databaza = modul_databaza.Databaza(self.ui)
        self.statistika = modul_statistika.Statistika(self.ui)
        # Track button clicks for index screen (module buttons)
        self.commands.button_click(self.ui.cenotvorbaButton, self.price)
        self.commands.button_click(self.ui.skladButton, self.storage)

        # Track all home button clicks
        self.home_buttons = [
            self.ui.homeArrow,
            self.ui.homeArrow2,
            self.ui.homeArrow3,
            self.ui.homeArrow4,
            self.ui.homeArrow5,
        ]
        self.commands.buttons_click(self.home_buttons, self.index)

    def show(self):
        """Show the main App UI window."""
        self.ui.show()

    def price(self):
        self.commands.change_screen(self.ui.cenotvorba)

    def storage(self):
        self.commands.change_screen(self.ui.sklad)

    def database(self):
        self.commands.change_screen(self.ui.databaza)

    def index(self):
        self.commands.change_screen(self.ui.index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
