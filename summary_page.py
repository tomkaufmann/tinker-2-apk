import datetime
from tkinter import *
from constants import *
import pymssql


class SummaryPage:
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
        self.rightFrame = None
        self.label1 = None
        self.label2 = None
        self.label3 = None
        self.label4 = None
        self.label5 = None
        self.label6 = None
        self.label7 = None
        self.label8 = None
        self.label9 = None
        self.label10 = None
        self.label11 = None
        self.label12 = None
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
        self.leftFrame = Frame(self.window, bg='white')
        self.leftFrame.grid(column=0, row=0, padx=5)
        self.rightFrame = Frame(self.window, bg='white')
        self.rightFrame.grid(column=1, row=0, padx=5)
        # Left frame
        self.label1 = Label(self.leftFrame, text="Mitarbeiter: ", font=("Arial Bold", TEXT), bg="white", width=10, anchor=NW)
        self.label1.grid(column=0, row=0)
        self.label2 = Label(self.leftFrame, text=f"{self.appData.mCurrentName}", font=("Arial Bold", TEXT), bg="white", width=50, anchor=NW)
        self.label2.grid(column=1, row=0)
        self.label3 = Label(self.leftFrame, text="Projekt: ", font=("Arial Bold", TEXT), bg="white", width=10, anchor=NW)
        self.label3.grid(column=0, row=1)
        self.label4 = Label(self.leftFrame, text=f"{self.appData.mCurrentRefId}", font=("Arial Bold", TEXT), bg="white", width=50, anchor=NW)
        self.label4.grid(column=1, row=1)
        self.label5 = Label(self.leftFrame, text="Info: ", font=("Arial Bold", TEXT), bg="white", width=10, anchor=NW)
        self.label5.grid(column=0, row=2)
        self.label6 = Label(self.leftFrame, text=f"{self.appData.mCurrentRefIdName}", font=("Arial Bold", TEXT), bg="white", width=50, anchor=NW)
        self.label6.grid(column=1, row=2)
        self.label7 = Label(self.leftFrame, text="Nummer: ", font=("Arial Bold", TEXT), bg="white", width=10, anchor=NW)
        self.label7.grid(column=0, row=3)
        self.label8 = Label(self.leftFrame, text=f"{self.appData.mCurrentSubRefId}", font=("Arial Bold", TEXT), bg="white", width=50, anchor=NW)
        self.label8.grid(column=1, row=3)
        self.label9 = Label(self.leftFrame, text="Tätigkeit: ", font=("Arial Bold", TEXT), bg="white", width=10, anchor=NW)
        self.label9.grid(column=0, row=4)
        self.label10 = Label(self.leftFrame, text=f"{self.appData.mCurrentTask}", font=("Arial Bold", TEXT), bg="white", width=50, anchor=NW)
        self.label10.grid(column=1, row=4)
        self.label11 = Label(self.leftFrame, text="Status: ", font=("Arial Bold", TEXT), bg="white", width=10, anchor=NW)
        self.label11.grid(column=0, row=5)
        self.label12 = Label(self.leftFrame, font=("Arial Bold", TEXT), bg="white", width=50, anchor=NW)
        self.label12.grid(column=1, row=5)
        self.button1 = Button(self.leftFrame, text="Abbrechen", height=BUTTON_SMALL_HEIGHT, width=BUTTON_SMALL_WIDTH, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_cancel)
        self.button1.grid(column=0, row=6, pady=20)
        # Right frame
        self.button2 = Button(self.rightFrame, text="OK", height=6, width=BUTTON_BIG_WIDTH, font=("Arial Bold", BIG_TEXT), bg="white", command=self.click_ok)
        self.button2.grid(column=0, row=0)
        # Handle widgets
        if self.appData.mCurrentWorkState == "1":
            if self.appData.mCurrentAction == "PW":
                self.label12.config(text="Projekt wird gewechselt", fg="green")
            elif self.appData.mCurrentAction == "K":
                self.label12.config(text="Arbeit wird aufgenommen", fg="green")
        else:
            self.label12.config(text="Arbeit wird beendet", fg="red")

    def hide(self):
        self.leftFrame.grid_forget()
        self.rightFrame.grid_forget()

    def click_cancel(self):
        self.hide()
        self.identifyPage.show(self.identifyPage, self.selectPage, self.numberPage, self.namePage, self.workPage, self.summaryPage, self.settingsPage, self.appData)

    def click_ok(self):
        self.appData.mConnection = pymssql.connect(server=self.appData.mServer, user=self.appData.mUser, password=self.appData.mPassword, database=self.appData.mDatabase)
        cursor = self.appData.mConnection.cursor()
        cursor.execute(f"UPDATE empl_curstatus SET CurWorkState='{self.appData.mCurrentWorkState}',CurRefId='{self.appData.mCurrentRefId}',CurSubRefId='{self.appData.mCurrentSubRefId}',CurTask='{self.appData.mCurrentTaskId}' WHERE EmplIdentNumber = '{self.appData.mCurrentHiquelNumber}'")
        self.appData.mConnection.commit()
        request = "INSERT INTO trans_data (TimeStamp,EmplIdentNumber,ChipdrIdNumber,Typ,RefId,SubRefId,ActionId,DeviceId)VALUES('"
        request += datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        request += f"','{self.appData.mCurrentHiquelNumber}','{self.appData.mCurrentChipdriveNumber}','{self.appData.mCurrentAction}','{self.appData.mCurrentRefId}','{self.appData.mCurrentSubRefId}','{self.appData.mCurrentTaskId}','{self.appData.mClientName}')"
        cursor.execute(request)
        self.appData.mConnection.commit()
        self.appData.mConnection.close()
        self.hide()
        self.identifyPage.show(self.identifyPage, self.selectPage, self.numberPage, self.namePage, self.workPage, self.summaryPage, self.settingsPage, self.appData)
