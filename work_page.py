from tkinter import *
from constants import *
import pymssql


class WorkPage:
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
        self.buttonWork1 = None
        self.buttonWork2 = None
        self.buttonWork3 = None
        self.buttonWork4 = None
        self.buttonWork5 = None
        self.buttonWork6 = None
        self.buttonWork7 = None
        self.buttonWork8 = None
        self.buttonWork9 = None
        self.buttonWork10 = None
        self.buttonWork11 = None
        self.buttonWork12 = None
        self.buttonWork13 = None
        self.buttonWork14 = None
        self.buttonWork15 = None
        self.buttonWork16 = None
        self.buttonWork17 = None
        self.buttonWork18 = None
        self.buttonWork19 = None
        self.buttonWork20 = None
        self.buttonWork21 = None
        self.buttonWork22 = None
        self.buttonWork23 = None
        self.buttonWork24 = None
        self.buttonWork25 = None
        self.buttonWork26 = None
        self.buttonWork27 = None
        self.buttonWork28 = None
        self.buttonWork29 = None
        self.buttonWork30 = None
        self.buttonWork31 = None
        self.buttonWork32 = None
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
        self.label1 = Label(self.leftFrame, text="Tätigkeit wählen", font=("Arial Bold", TEXT), bg="white")
        self.label1.grid(column=0, row=0, columnspan=4, pady=20)
        self.buttonWork1 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work1)
        self.buttonWork1.grid(column=0, row=1)
        self.buttonWork2 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work2)
        self.buttonWork2.grid(column=1, row=1)
        self.buttonWork3 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work3)
        self.buttonWork3.grid(column=2, row=1)
        self.buttonWork4 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work4)
        self.buttonWork4.grid(column=3, row=1)
        self.buttonWork5 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work5)
        self.buttonWork5.grid(column=0, row=2)
        self.buttonWork6 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work6)
        self.buttonWork6.grid(column=1, row=2)
        self.buttonWork7 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work7)
        self.buttonWork7.grid(column=2, row=2)
        self.buttonWork8 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work8)
        self.buttonWork8.grid(column=3, row=2)
        self.buttonWork9 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work9)
        self.buttonWork9.grid(column=0, row=3)
        self.buttonWork10 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work10)
        self.buttonWork10.grid(column=1, row=3)
        self.buttonWork11 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work11)
        self.buttonWork11.grid(column=2, row=3)
        self.buttonWork12 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work12)
        self.buttonWork12.grid(column=3, row=3)
        self.buttonWork13 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work13)
        self.buttonWork13.grid(column=0, row=4)
        self.buttonWork14 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work14)
        self.buttonWork14.grid(column=1, row=4)
        self.buttonWork15 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work15)
        self.buttonWork15.grid(column=2, row=4)
        self.buttonWork16 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work16)
        self.buttonWork16.grid(column=3, row=4)
        self.buttonWork17 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work17)
        self.buttonWork17.grid(column=0, row=5)
        self.buttonWork18 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work18)
        self.buttonWork18.grid(column=1, row=5)
        self.buttonWork19 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work19)
        self.buttonWork19.grid(column=2, row=5)
        self.buttonWork20 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work20)
        self.buttonWork20.grid(column=3, row=5)
        self.buttonWork21 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work21)
        self.buttonWork21.grid(column=0, row=6)
        self.buttonWork22 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work22)
        self.buttonWork22.grid(column=1, row=6)
        self.buttonWork23 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work23)
        self.buttonWork23.grid(column=2, row=6)
        self.buttonWork24 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work24)
        self.buttonWork24.grid(column=3, row=6)
        self.buttonWork25 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work25)
        self.buttonWork25.grid(column=0, row=7)
        self.buttonWork26 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work26)
        self.buttonWork26.grid(column=1, row=7)
        self.buttonWork27 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work27)
        self.buttonWork27.grid(column=2, row=7)
        self.buttonWork28 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work28)
        self.buttonWork28.grid(column=3, row=7)
        self.buttonWork29 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work29)
        self.buttonWork29.grid(column=0, row=8)
        self.buttonWork30 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work30)
        self.buttonWork30.grid(column=1, row=8)
        self.buttonWork31 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work31)
        self.buttonWork31.grid(column=2, row=8)
        self.buttonWork32 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=25, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_work32)
        self.buttonWork32.grid(column=3, row=8)
        self.buttonCancel = Button(self.leftFrame, text="Abbrechen", height=BUTTON_SMALL_HEIGHT, width=BUTTON_SMALL_WIDTH, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_cancel)
        self.buttonCancel.grid(column=0, row=11, pady=20)
        # Get work
        i = 0
        self.appData.mConnection = pymssql.connect(server=self.appData.mServer, user=self.appData.mUser, password=self.appData.mPassword, database=self.appData.mDatabase)
        cursor = self.appData.mConnection.cursor()
        cursor.execute("SELECT * FROM action_data ORDER BY RefIdName")
        row = cursor.fetchone()
        while row:
            if i == 0:
                self.buttonWork1.config(text=row[4])
            elif i == 1:
                self.buttonWork2.config(text=row[4])
            elif i == 2:
                self.buttonWork3.config(text=row[4])
            elif i == 3:
                self.buttonWork4.config(text=row[4])
            elif i == 4:
                self.buttonWork5.config(text=row[4])
            elif i == 5:
                self.buttonWork6.config(text=row[4])
            elif i == 6:
                self.buttonWork7.config(text=row[4])
            elif i == 7:
                self.buttonWork8.config(text=row[4])
            elif i == 8:
                self.buttonWork9.config(text=row[4])
            elif i == 9:
                self.buttonWork10.config(text=row[4])
            elif i == 10:
                self.buttonWork11.config(text=row[4])
            elif i == 11:
                self.buttonWork12.config(text=row[4])
            elif i == 12:
                self.buttonWork13.config(text=row[4])
            elif i == 13:
                self.buttonWork14.config(text=row[4])
            elif i == 14:
                self.buttonWork15.config(text=row[4])
            elif i == 15:
                self.buttonWork16.config(text=row[4])
            elif i == 16:
                self.buttonWork17.config(text=row[4])
            elif i == 17:
                self.buttonWork18.config(text=row[4])
            elif i == 18:
                self.buttonWork19.config(text=row[4])
            elif i == 19:
                self.buttonWork20.config(text=row[4])
            elif i == 20:
                self.buttonWork21.config(text=row[4])
            elif i == 21:
                self.buttonWork22.config(text=row[4])
            elif i == 22:
                self.buttonWork23.config(text=row[4])
            elif i == 23:
                self.buttonWork24.config(text=row[4])
            elif i == 24:
                self.buttonWork25.config(text=row[4])
            elif i == 25:
                self.buttonWork26.config(text=row[4])
            elif i == 26:
                self.buttonWork27.config(text=row[4])
            elif i == 27:
                self.buttonWork28.config(text=row[4])
            elif i == 28:
                self.buttonWork29.config(text=row[4])
            elif i == 29:
                self.buttonWork30.config(text=row[4])
            elif i == 30:
                self.buttonWork31.config(text=row[4])
            elif i == 31:
                self.buttonWork32.config(text=row[4])
            else:
                break
            row = cursor.fetchone()
            i = i + 1
        self.appData.mConnection.close()

    def hide(self):
        self.leftFrame.grid_forget()

    def handle_work(self, w):
        if w != "":
            self.appData.mCurrentTask = w
            self.appData.mConnection = pymssql.connect(server=self.appData.mServer, user=self.appData.mUser, password=self.appData.mPassword, database=self.appData.mDatabase)
            cursor = self.appData.mConnection.cursor()
            cursor.execute(f"SELECT * FROM action_data WHERE RefIdName = '{w}'")
            row = cursor.fetchone()
            if row is not None and row[4] == w and row[2] is not None:
                self.appData.mCurrentTaskId = str(row[2])
            else:
                self.appData.mCurrentTaskId = ""
            self.appData.mConnection.close()
            self.hide()
            self.summaryPage.show(self.identifyPage, self.selectPage, self.numberPage, self.namePage, self.workPage, self.summaryPage, self.settingsPage, self.appData)

    def click_work1(self):
        w = self.buttonWork1["text"]
        self.handle_work(w)

    def click_work2(self):
        w = self.buttonWork2["text"]
        self.handle_work(w)

    def click_work3(self):
        w = self.buttonWork3["text"]
        self.handle_work(w)

    def click_work4(self):
        w = self.buttonWork4["text"]
        self.handle_work(w)

    def click_work5(self):
        w = self.buttonWork5["text"]
        self.handle_work(w)

    def click_work6(self):
        w = self.buttonWork6["text"]
        self.handle_work(w)

    def click_work7(self):
        w = self.buttonWork7["text"]
        self.handle_work(w)

    def click_work8(self):
        w = self.buttonWork8["text"]
        self.handle_work(w)

    def click_work9(self):
        w = self.buttonWork9["text"]
        self.handle_work(w)

    def click_work10(self):
        w = self.buttonWork10["text"]
        self.handle_work(w)

    def click_work11(self):
        w = self.buttonWork11["text"]
        self.handle_work(w)

    def click_work12(self):
        w = self.buttonWork12["text"]
        self.handle_work(w)

    def click_work13(self):
        w = self.buttonWork13["text"]
        self.handle_work(w)

    def click_work14(self):
        w = self.buttonWork14["text"]
        self.handle_work(w)

    def click_work15(self):
        w = self.buttonWork15["text"]
        self.handle_work(w)

    def click_work16(self):
        w = self.buttonWork16["text"]
        self.handle_work(w)

    def click_work17(self):
        w = self.buttonWork17["text"]
        self.handle_work(w)

    def click_work18(self):
        w = self.buttonWork18["text"]
        self.handle_work(w)

    def click_work19(self):
        w = self.buttonWork19["text"]
        self.handle_work(w)

    def click_work20(self):
        w = self.buttonWork20["text"]
        self.handle_work(w)

    def click_work21(self):
        w = self.buttonWork21["text"]
        self.handle_work(w)

    def click_work22(self):
        w = self.buttonWork22["text"]
        self.handle_work(w)

    def click_work23(self):
        w = self.buttonWork23["text"]
        self.handle_work(w)

    def click_work24(self):
        w = self.buttonWork24["text"]
        self.handle_work(w)

    def click_work25(self):
        w = self.buttonWork25["text"]
        self.handle_work(w)

    def click_work26(self):
        w = self.buttonWork26["text"]
        self.handle_work(w)

    def click_work27(self):
        w = self.buttonWork27["text"]
        self.handle_work(w)

    def click_work28(self):
        w = self.buttonWork28["text"]
        self.handle_work(w)

    def click_work29(self):
        w = self.buttonWork29["text"]
        self.handle_work(w)

    def click_work30(self):
        w = self.buttonWork30["text"]
        self.handle_work(w)

    def click_work31(self):
        w = self.buttonWork31["text"]
        self.handle_work(w)

    def click_work32(self):
        w = self.buttonWork32["text"]
        self.handle_work(w)

    def click_cancel(self):
        self.hide()
        self.identifyPage.show(self.identifyPage, self.selectPage, self.numberPage, self.namePage, self.workPage, self.summaryPage, self.settingsPage, self.appData)
