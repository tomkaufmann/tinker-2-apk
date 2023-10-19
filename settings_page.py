from tkinter import *
from constants import *


class SettingsPage:
    def __init__(self, window):
        self.window = window
        self.identifyPage = None
        self.selectPage = None
        self.numberPage = None
        self.namePage = None
        self.workPage = None
        self.summaryPage = None
        self.settingsPage = None
        self.appData = None
        self.topFrame = None
        self.bottomFrame = None
        self.label1 = None
        self.entry1 = None
        self.label2 = None
        self.entry2 = None
        self.label3 = None
        self.entry3 = None
        self.label4 = None
        self.entry4 = None
        self.label5 = None
        self.entry5 = None
        self.button1 = None
        self.button2 = None

    def show(self, identify_page, select_page, number_page, name_page, work_page, summary_page, settings_page, app_data):
        self.identifyPage = identify_page
        self.selectPage = select_page
        self.numberPage = number_page
        self.namePage = name_page
        self.workPage = work_page
        self.summaryPage = summary_page
        self.settingsPage = settings_page
        self.appData = app_data
        # Frames
        self.topFrame = Frame(self.window, bg='white')
        self.topFrame.grid(column=0, row=0)
        self.bottomFrame = Frame(self.window, bg='white')
        self.bottomFrame.grid(column=0, row=1, pady=20)
        # Top frame
        self.label1 = Label(self.topFrame, text="Client name", font=("Arial Bold", TEXT), bg="white")
        self.label1.grid(column=0, row=0)
        self.entry1 = Entry(self.topFrame, font=("Arial", TEXT), width=50, bd=3)
        self.entry1.insert(END, string=self.appData.mClientName)
        self.entry1.grid(column=1, row=0)
        self.label2 = Label(self.topFrame, text="Server", font=("Arial Bold", TEXT), bg="white")
        self.label2.grid(column=0, row=1)
        self.entry2 = Entry(self.topFrame, font=("Arial", TEXT), width=50, bd=3)
        self.entry2.insert(END, string=self.appData.mServer)
        self.entry2.grid(column=1, row=1)
        self.label3 = Label(self.topFrame, text="Database", font=("Arial Bold", TEXT), bg="white")
        self.label3.grid(column=0, row=2)
        self.entry3 = Entry(self.topFrame, font=("Arial", TEXT), width=50, bd=3)
        self.entry3.insert(END, string=self.appData.mDatabase)
        self.entry3.grid(column=1, row=2)
        self.label4 = Label(self.topFrame, text="User", font=("Arial Bold", TEXT), bg="white")
        self.label4.grid(column=0, row=3)
        self.entry4 = Entry(self.topFrame, font=("Arial", TEXT), width=50, bd=3)
        self.entry4.insert(END, string=self.appData.mUser)
        self.entry4.grid(column=1, row=3)
        self.label5 = Label(self.topFrame, text="Password", font=("Arial Bold", TEXT), bg="white")
        self.label5.grid(column=0, row=4)
        self.entry5 = Entry(self.topFrame, font=("Arial", TEXT), width=50, bd=3)
        self.entry5.insert(END, string=self.appData.mPassword)
        self.entry5.grid(column=1, row=4)
        # Bottom  frame
        self.button1 = Button(self.bottomFrame, text="Abbrechen", height=BUTTON_SMALL_HEIGHT, width=BUTTON_SMALL_WIDTH, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_cancel)
        self.button1.grid(column=0, row=0, padx=5)
        self.button2 = Button(self.bottomFrame, text="Speichern", height=BUTTON_SMALL_HEIGHT, width=BUTTON_SMALL_WIDTH, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_save)
        self.button2.grid(column=1, row=0, padx=5)

    def hide(self):
        self.topFrame.grid_forget()
        self.bottomFrame.grid_forget()

    def click_cancel(self):
        self.hide()
        self.identifyPage.show(self.identifyPage, self.selectPage, self.numberPage, self.namePage, self.workPage, self.summaryPage, self.settingsPage, self.appData)

    def click_save(self):
        with open("./tr.hiq", mode="w") as file:
            self.appData.mServer = self.entry2.get()
            self.appData.mDatabase = self.entry3.get()
            self.appData.mUser = self.entry4.get()
            self.appData.mPassword = self.entry5.get()
            file.write(self.appData.mServer + "\n")
            file.write(self.appData.mDatabase + "\n")
            file.write(self.appData.mUser + "\n")
            file.write(self.appData.mPassword + "\n")
