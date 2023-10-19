from tkinter import *
from constants import *
import pymssql


class NamePage:
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
        self.leftFrame = None
        self.label1 = None
        self.buttonName1 = None
        self.buttonName2 = None
        self.buttonName3 = None
        self.buttonName4 = None
        self.buttonName5 = None
        self.buttonName6 = None
        self.buttonName7 = None
        self.buttonName8 = None
        self.buttonName9 = None
        self.buttonName10 = None
        self.buttonCancel = None

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
        self.leftFrame = Frame(self.window, bg='white')
        self.leftFrame.grid(column=0, row=0)
        # Left frame
        self.label1 = Label(self.leftFrame, text="Projektnamen wählen", font=("Arial Bold", TEXT), bg="white")
        self.label1.grid(column=0, row=0, pady=20)
        self.buttonName1 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=100, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_name1)
        self.buttonName1.grid(column=0, row=1)
        self.buttonName2 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=100, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_name2)
        self.buttonName2.grid(column=0, row=2)
        self.buttonName3 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=100, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_name3)
        self.buttonName3.grid(column=0, row=3)
        self.buttonName4 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=100, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_name4)
        self.buttonName4.grid(column=0, row=4)
        self.buttonName5 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=100, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_name5)
        self.buttonName5.grid(column=0, row=5)
        self.buttonName6 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=100, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_name6)
        self.buttonName6.grid(column=0, row=6)
        self.buttonName7 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=100, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_name7)
        self.buttonName7.grid(column=0, row=7)
        self.buttonName8 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=100, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_name8)
        self.buttonName8.grid(column=0, row=8)
        self.buttonName9 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=100, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_name9)
        self.buttonName9.grid(column=0, row=9)
        self.buttonName10 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=100, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_name10)
        self.buttonName10.grid(column=0, row=10)
        self.buttonCancel = Button(self.leftFrame, text="Abbrechen", height=BUTTON_SMALL_HEIGHT, width=BUTTON_SMALL_WIDTH, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_cancel)
        self.buttonCancel.grid(column=0, row=11, pady=20)
        # Handle widgets
        if self.appData.mNamePageParameter is False:
            self.buttonName1.config(text="Projekt nicht in Datenbank!")
        else:
            i = 0
            self.appData.mConnection = pymssql.connect(server=self.appData.mServer, user=self.appData.mUser, password=self.appData.mPassword, database=self.appData.mDatabase)
            cursor = self.appData.mConnection.cursor()
            cursor.execute(f"SELECT * FROM reference_data WHERE subRefId = '{self.appData.mCurrentSubRefId}'")
            row = cursor.fetchone()
            while row:
                if i == 0:
                    self.buttonName1.config(text=row[3])
                elif i == 1:
                    self.buttonName2.config(text=row[3])
                elif i == 2:
                    self.buttonName3.config(text=row[3])
                elif i == 3:
                    self.buttonName4.config(text=row[3])
                elif i == 4:
                    self.buttonName5.config(text=row[3])
                elif i == 5:
                    self.buttonName6.config(text=row[3])
                elif i == 6:
                    self.buttonName7.config(text=row[3])
                elif i == 7:
                    self.buttonName8.config(text=row[3])
                elif i == 8:
                    self.buttonName9.config(text=row[3])
                elif i == 9:
                    self.buttonName10.config(text=row[3])
                else:
                    break
                row = cursor.fetchone()
                i = i + 1
            self.appData.mConnection.close()

    def hide(self):
        self.leftFrame.grid_forget()

    def handle_name(self, w):
        if w != "":
            self.appData.mCurrentRefIdName = w
            self.appData.mConnection = pymssql.connect(server=self.appData.mServer, user=self.appData.mUser, password=self.appData.mPassword, database=self.appData.mDatabase)
            cursor = self.appData.mConnection.cursor()
            cursor.execute(f"SELECT * FROM reference_data WHERE subRefId = '{self.appData.mCurrentSubRefId}' AND RefIdName = '{self.appData.mCurrentRefIdName}'")
            row = cursor.fetchone()
            if row is not None and row[2] is not None:
                self.appData.mCurrentRefId = row[2]
            else:
                self.appData.mCurrentRefId = ""
            self.hide()
            self.workPage.show(self.identifyPage, self.selectPage, self.numberPage, self.namePage, self.workPage, self.summaryPage, self.settingsPage, self.appData)

    def click_name1(self):
        w = self.buttonName1["text"]
        self.handle_name(w)

    def click_name2(self):
        w = self.buttonName2["text"]
        self.handle_name(w)

    def click_name3(self):
        w = self.buttonName3["text"]
        self.handle_name(w)

    def click_name4(self):
        w = self.buttonName4["text"]
        self.handle_name(w)

    def click_name5(self):
        w = self.buttonName5["text"]
        self.handle_name(w)

    def click_name6(self):
        w = self.buttonName6["text"]
        self.handle_name(w)

    def click_name7(self):
        w = self.buttonName7["text"]
        self.handle_name(w)

    def click_name8(self):
        w = self.buttonName8["text"]
        self.handle_name(w)

    def click_name9(self):
        w = self.buttonName9["text"]
        self.handle_name(w)

    def click_name10(self):
        w = self.buttonName10["text"]
        self.handle_name(w)

    def click_cancel(self):
        self.hide()
        self.identifyPage.show(self.identifyPage, self.selectPage, self.numberPage, self.namePage, self.workPage, self.summaryPage, self.settingsPage, self.appData)
