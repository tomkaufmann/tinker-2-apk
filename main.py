from identify_page import *
from select_page import *
from number_page import *
from name_page import *
from work_page import *
from summary_page import *
from settings_page import *
from app_data import *


class RPiTRClient:
    def __init__(self):
        self.fullScreenState = True
        self.appData = AppData()
        self.window = Tk()
        self.window.title("rpiTRclient")
        self.window.configure(background="white", padx=50, pady=50)
        self.window.attributes("-fullscreen", self.fullScreenState)
        self.window.bind("<F11>", self.toggle_full_screen)
        self.window.bind("<Escape>", self.quit_full_screen)
        self.identifyPage = IdentifyPage(self.window)
        self.selectPage = SelectPage(self.window)
        self.numberPage = NumberPage(self.window)
        self.namePage = NamePage(self.window)
        self.workPage = WorkPage(self.window)
        self.summaryPage = SummaryPage(self.window)
        self.settingsPage = SettingsPage(self.window)
        self.identifyPage.show(self.identifyPage, self.selectPage, self.numberPage, self.namePage, self.workPage, self.summaryPage, self.settingsPage, self.appData)
        self.window.mainloop()

    def toggle_full_screen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quit_full_screen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)


if __name__ == '__main__':
    app = RPiTRClient()
