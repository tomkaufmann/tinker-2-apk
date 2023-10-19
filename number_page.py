from tkinter import *
from constants import *
import pymssql


class NumberPage:
    def __init__(self, window):
        self.window = window
        self.id = 0
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
        self.buttonNumber1 = None
        self.buttonNumber2 = None
        self.buttonNumber3 = None
        self.buttonNumber4 = None
        self.buttonNumber5 = None
        self.buttonNumber6 = None
        self.buttonNumber7 = None
        self.buttonNumber8 = None
        self.buttonNumber9 = None
        self.buttonNumber10 = None
        self.buttonNumber11 = None
        self.buttonNumber12 = None
        self.buttonNumber13 = None
        self.buttonNumber14 = None
        self.buttonNumber15 = None
        self.buttonNumber16 = None
        self.buttonNumber17 = None
        self.buttonNumber18 = None
        self.buttonNumber19 = None
        self.buttonNumber20 = None
        self.buttonNumber21 = None
        self.buttonNumber22 = None
        self.buttonNumber23 = None
        self.buttonNumber24 = None
        self.buttonNumber25 = None
        self.buttonNumber26 = None
        self.buttonCancel = None
        self.label2 = None
        self.label3 = None
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.button4 = None
        self.button5 = None
        self.button6 = None
        self.button7 = None
        self.button8 = None
        self.button9 = None
        self.buttonC = None
        self.button0 = None
        self.buttonOK = None
        self.buttonPA = None
        self.buttonAU = None

    def show(self, identify_page, select_page, number_page, name_page, work_page, summary_page, settings_page, app_data):
        self.id = 0
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
        self.label1 = Label(self.leftFrame, text="Projektnummer wählen", font=("Arial Bold", TEXT), bg="white")
        self.label1.grid(column=0, row=0, columnspan=4, pady=20)
        self.buttonNumber1 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number1)
        self.buttonNumber1.grid(column=0, row=1)
        self.buttonNumber2 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number2)
        self.buttonNumber2.grid(column=1, row=1)
        self.buttonNumber3 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number3)
        self.buttonNumber3.grid(column=2, row=1)
        self.buttonNumber4 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number4)
        self.buttonNumber4.grid(column=3, row=1)
        self.buttonNumber5 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number5)
        self.buttonNumber5.grid(column=0, row=2)
        self.buttonNumber6 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number6)
        self.buttonNumber6.grid(column=1, row=2)
        self.buttonNumber7 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number7)
        self.buttonNumber7.grid(column=2, row=2)
        self.buttonNumber8 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number8)
        self.buttonNumber8.grid(column=3, row=2)
        self.buttonNumber9 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number9)
        self.buttonNumber9.grid(column=0, row=3)
        self.buttonNumber10 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number10)
        self.buttonNumber10.grid(column=1, row=3)
        self.buttonNumber11 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number11)
        self.buttonNumber11.grid(column=2, row=3)
        self.buttonNumber12 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number12)
        self.buttonNumber12.grid(column=3, row=3)
        self.buttonNumber13 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number13)
        self.buttonNumber13.grid(column=0, row=4)
        self.buttonNumber14 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number14)
        self.buttonNumber14.grid(column=1, row=4)
        self.buttonNumber15 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number15)
        self.buttonNumber15.grid(column=2, row=4)
        self.buttonNumber16 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number16)
        self.buttonNumber16.grid(column=3, row=4)
        self.buttonNumber17 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number17)
        self.buttonNumber17.grid(column=0, row=5)
        self.buttonNumber18 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number18)
        self.buttonNumber18.grid(column=1, row=5)
        self.buttonNumber19 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number19)
        self.buttonNumber19.grid(column=2, row=5)
        self.buttonNumber20 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number20)
        self.buttonNumber20.grid(column=3, row=5)
        self.buttonNumber21 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number21)
        self.buttonNumber21.grid(column=0, row=6)
        self.buttonNumber22 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number22)
        self.buttonNumber22.grid(column=1, row=6)
        self.buttonNumber23 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number23)
        self.buttonNumber23.grid(column=2, row=6)
        self.buttonNumber24 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number24)
        self.buttonNumber24.grid(column=3, row=6)
        self.buttonNumber25 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number25)
        self.buttonNumber25.grid(column=0, row=7)
        self.buttonNumber26 = Button(self.leftFrame, height=BUTTON_SMALL_HEIGHT, width=16, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_number26)
        self.buttonNumber26.grid(column=1, row=7)
        self.buttonCancel = Button(self.leftFrame, text="Abbrechen", height=BUTTON_SMALL_HEIGHT, width=BUTTON_SMALL_WIDTH, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_cancel)
        self.buttonCancel.grid(column=0, row=10, pady=20)
        # Right frame
        self.label2 = Label(self.rightFrame, text="Projektnummer", font=("Arial Bold", TEXT), bg="white")
        self.label2.grid(column=0, row=0, columnspan=3)
        self.label3 = Label(self.rightFrame, text=str(self.id).zfill(4), font=("Arial Bold", TEXT), bg="white")
        self.label3.grid(column=0, row=1, columnspan=3)
        self.button1 = Button(self.rightFrame, text="1", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click1)
        self.button1.grid(column=0, row=2, rowspan=2)
        self.button2 = Button(self.rightFrame, text="2", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click2)
        self.button2.grid(column=1, row=2, rowspan=2)
        self.button3 = Button(self.rightFrame, text="3", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click3)
        self.button3.grid(column=2, row=2, rowspan=2)
        self.button4 = Button(self.rightFrame, text="4", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click4)
        self.button4.grid(column=0, row=4, rowspan=2)
        self.button5 = Button(self.rightFrame, text="5", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click5)
        self.button5.grid(column=1, row=4, rowspan=2)
        self.button6 = Button(self.rightFrame, text="6", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click6)
        self.button6.grid(column=2, row=4, rowspan=2)
        self.button7 = Button(self.rightFrame, text="7", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click7)
        self.button7.grid(column=0, row=6, rowspan=2)
        self.button8 = Button(self.rightFrame, text="8", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click8)
        self.button8.grid(column=1, row=6, rowspan=2)
        self.button9 = Button(self.rightFrame, text="9", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click9)
        self.button9.grid(column=2, row=6, rowspan=2)
        self.buttonC = Button(self.rightFrame, text="C", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click_clear)
        self.buttonC.grid(column=0, row=8, rowspan=2)
        self.button0 = Button(self.rightFrame, text="0", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click0)
        self.button0.grid(column=1, row=8, rowspan=2)
        self.buttonOK = Button(self.rightFrame, text="OK", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click_ok)
        self.buttonOK.grid(column=2, row=8, rowspan=2)
        self.buttonPA = Button(self.rightFrame, text="PA", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click_pa)
        self.buttonPA.grid(column=0, row=10, rowspan=2)
        self.buttonAU = Button(self.rightFrame, text="AU", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click_au)
        self.buttonAU.grid(column=1, row=10, rowspan=2)

    def hide(self):
        self.leftFrame.grid_forget()
        self.rightFrame.grid_forget()

    def handle_number(self, w):
        if w != "":
            self.appData.mCurrentSubRefId = w
            self.appData.mNamePageParameter = True
            self.hide()
            self.namePage.show(self.identifyPage, self.selectPage, self.numberPage, self.namePage, self.workPage, self.summaryPage, self.settingsPage, self.appData)

    def click_number1(self):
        w = self.buttonNumber1["text"]
        self.handle_number(w)

    def click_number2(self):
        w = self.buttonNumber2["text"]
        self.handle_number(w)

    def click_number3(self):
        w = self.buttonNumber3["text"]
        self.handle_number(w)

    def click_number4(self):
        w = self.buttonNumber4["text"]
        self.handle_number(w)

    def click_number5(self):
        w = self.buttonNumber5["text"]
        self.handle_number(w)

    def click_number6(self):
        w = self.buttonNumber6["text"]
        self.handle_number(w)

    def click_number7(self):
        w = self.buttonNumber7["text"]
        self.handle_number(w)

    def click_number8(self):
        w = self.buttonNumber8["text"]
        self.handle_number(w)

    def click_number9(self):
        w = self.buttonNumber9["text"]
        self.handle_number(w)

    def click_number10(self):
        w = self.buttonNumber10["text"]
        self.handle_number(w)

    def click_number11(self):
        w = self.buttonNumber11["text"]
        self.handle_number(w)

    def click_number12(self):
        w = self.buttonNumber12["text"]
        self.handle_number(w)

    def click_number13(self):
        w = self.buttonNumber13["text"]
        self.handle_number(w)

    def click_number14(self):
        w = self.buttonNumber14["text"]
        self.handle_number(w)

    def click_number15(self):
        w = self.buttonNumber15["text"]
        self.handle_number(w)

    def click_number16(self):
        w = self.buttonNumber16["text"]
        self.handle_number(w)

    def click_number17(self):
        w = self.buttonNumber17["text"]
        self.handle_number(w)

    def click_number18(self):
        w = self.buttonNumber18["text"]
        self.handle_number(w)

    def click_number19(self):
        w = self.buttonNumber19["text"]
        self.handle_number(w)

    def click_number20(self):
        w = self.buttonNumber20["text"]
        self.handle_number(w)

    def click_number21(self):
        w = self.buttonNumber21["text"]
        self.handle_number(w)

    def click_number22(self):
        w = self.buttonNumber22["text"]
        self.handle_number(w)

    def click_number23(self):
        w = self.buttonNumber23["text"]
        self.handle_number(w)

    def click_number24(self):
        w = self.buttonNumber24["text"]
        self.handle_number(w)

    def click_number25(self):
        w = self.buttonNumber25["text"]
        self.handle_number(w)

    def click_number26(self):
        w = self.buttonNumber26["text"]
        self.handle_number(w)

    def click_cancel(self):
        self.hide()
        self.identifyPage.show(self.identifyPage, self.selectPage, self.numberPage, self.namePage, self.workPage, self.summaryPage, self.settingsPage, self.appData)

    def handle_numeric(self, i):
        if self.appData.mPAOnAUOff is True:
            self.id = self.get_numeric_input(i, self.id, 4)
            self.label3.config(text=str(self.id).zfill(4))
        else:
            self.id = self.get_numeric_input(i, self.id, 8)
            self.label3.config(text="AU"+str(self.id).zfill(8))

    @staticmethod
    def get_numeric_input(i, c, length):
        if c == 0 and length > 0:
            r = i
        elif c < 10 and length > 1:
            r = c * 10 + i
        elif c < 100 and length > 2:
            r = c * 10 + i
        elif c < 1000 and length > 3:
            r = c * 10 + i
        elif c < 10000 and length > 4:
            r = c * 10 + i
        elif c < 100000 and length > 5:
            r = c * 10 + i
        elif c < 1000000 and length > 6:
            r = c * 10 + i
        elif c < 10000000 and length > 7:
            r = c * 10 + i
        else:
            r = 0
        return r

    def click0(self):
        self.handle_numeric(0)

    def click1(self):
        self.handle_numeric(1)

    def click2(self):
        self.handle_numeric(2)

    def click3(self):
        self.handle_numeric(3)

    def click4(self):
        self.handle_numeric(4)

    def click5(self):
        self.handle_numeric(5)

    def click6(self):
        self.handle_numeric(6)

    def click7(self):
        self.handle_numeric(7)

    def click8(self):
        self.handle_numeric(8)

    def click9(self):
        self.handle_numeric(9)

    def click_clear(self):
        self.id = 0
        if self.appData.mPAOnAUOff is True:
            self.label3.config(text=str(self.id).zfill(4))
        else:
            self.label3.config(text="AU"+str(self.id).zfill(8))

    def write_number_button(self, i, t):
        if i == 0:
            self.buttonNumber1.config(text=t)
        elif i == 1:
            self.buttonNumber2.config(text=t)
        elif i == 2:
            self.buttonNumber3.config(text=t)
        elif i == 3:
            self.buttonNumber4.config(text=t)
        elif i == 4:
            self.buttonNumber5.config(text=t)
        elif i == 5:
            self.buttonNumber6.config(text=t)
        elif i == 6:
            self.buttonNumber7.config(text=t)
        elif i == 7:
            self.buttonNumber8.config(text=t)
        elif i == 8:
            self.buttonNumber9.config(text=t)
        elif i == 9:
            self.buttonNumber10.config(text=t)
        elif i == 10:
            self.buttonNumber11.config(text=t)
        elif i == 11:
            self.buttonNumber12.config(text=t)
        elif i == 12:
            self.buttonNumber13.config(text=t)
        elif i == 13:
            self.buttonNumber14.config(text=t)
        elif i == 14:
            self.buttonNumber15.config(text=t)
        elif i == 15:
            self.buttonNumber16.config(text=t)
        elif i == 16:
            self.buttonNumber17.config(text=t)
        elif i == 17:
            self.buttonNumber18.config(text=t)
        elif i == 18:
            self.buttonNumber19.config(text=t)
        elif i == 19:
            self.buttonNumber20.config(text=t)
        elif i == 20:
            self.buttonNumber21.config(text=t)
        elif i == 21:
            self.buttonNumber22.config(text=t)
        elif i == 22:
            self.buttonNumber23.config(text=t)
        elif i == 23:
            self.buttonNumber24.config(text=t)
        elif i == 24:
            self.buttonNumber25.config(text=t)
        elif i == 25:
            self.buttonNumber26.config(text=t)

    def click_ok(self):
        if self.appData.mPAOnAUOff is False:
            # Search AU
            self.appData.mConnection = pymssql.connect(server=self.appData.mServer, user=self.appData.mUser, password=self.appData.mPassword, database=self.appData.mDatabase)
            cursor = self.appData.mConnection.cursor()
            cursor.execute(f"SELECT * FROM reference_data WHERE RefId = '{self.label3['text']}'")
            row = cursor.fetchone()
            if row is not None:
                if row[2] == self.label3['text']:
                    self.appData.mCurrentRefId = row[2]
                    if row[3] is not None:
                        self.appData.mCurrentRefIdName = row[3]
                    else:
                        self.appData.mCurrentRefIdName = ""
                    if row[4] is not None:
                        self.appData.mCurrentSubRefId = row[4]
                    else:
                        self.appData.mCurrentSubRefId = ""
                    self.appData.mConnection.close()
                    self.hide()
                    self.workPage.show(self.identifyPage, self.selectPage, self.numberPage, self.namePage, self.workPage, self.summaryPage, self.settingsPage, self.appData)
                else:
                    self.appData.mConnection.close()
            else:
                self.appData.mConnection.close()
        else:
            # Search PA
            for i in range(26):
                self.write_number_button(i, "")
            i = 0
            number = []
            self.appData.mConnection = pymssql.connect(server=self.appData.mServer, user=self.appData.mUser, password=self.appData.mPassword, database=self.appData.mDatabase)
            cursor = self.appData.mConnection.cursor()
            cursor.execute(f"SELECT * FROM reference_data WHERE Typ = 'PA' AND subRefId LIKE '%{self.label3['text']}%'")
            row = cursor.fetchone()
            while row:
                found = False
                for s in number:
                    if s == row[4]:
                        found = True
                if not found:
                    number.append(row[4])
                    self.write_number_button(i, row[4])
                    i = i + 1
                row = cursor.fetchone()
            self.appData.mConnection.close()
            # PA not found
            if i == 0:
                self.appData.mCurrentRefId = ""
                self.appData.mCurrentRefIdName = ""
                self.appData.mCurrentSubRefId = self.label3['text']
                self.appData.mNamePageParameter = False
                self.hide()
                self.namePage.show(self.identifyPage, self.selectPage, self.numberPage, self.namePage, self.workPage, self.summaryPage, self.settingsPage, self.appData)

    def click_pa(self):
        self.id = 0
        self.appData.mPAOnAUOff = True
        self.label1.config(text="Projektnummer wählen")
        self.label2.config(text="Projektnummer")
        self.label3.config(text="0000")

    def click_au(self):
        self.id = 0
        self.appData.mPAOnAUOff = False
        self.label1.config(text="Auftragsnummer wählen")
        self.label2.config(text="Auftragsnummer")
        self.label3.config(text="AU00000000")
