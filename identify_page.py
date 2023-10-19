from tkinter import *
from constants import *
import pymssql
import time
import serial


class IdentifyPage:
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
        self.labelTime = None
        self.label1 = None
        self.buttonConnection = None
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
        self.m_time = None
        self.m_rfid = None

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
        self.labelTime = Label(self.leftFrame, font=("Arial Bold", SMALL_TEXT), bg="white")
        self.labelTime.grid(column=0, row=0)
        self.label1 = Label(self.leftFrame, text="Mit RFID Token oder Tokennummer anmelden", font=("Arial Bold", TEXT), bg="white")
        self.label1.grid(column=0, row=1, padx=100, pady=100)
        # self.buttonConnection = Button(self.leftFrame, text="Verbindung", height=BUTTON_SMALL_HEIGHT, width=BUTTON_SMALL_WIDTH, font=("Arial Bold", SMALL_TEXT), bg="white", command=self.click_connection)
        # self.buttonConnection.grid(column=0, row=2)
        # Right frame
        self.label2 = Label(self.rightFrame, text="Tokennummer", font=("Arial Bold", TEXT), bg="white")
        self.label2.grid(column=0, row=0, columnspan=3)
        self.label3 = Label(self.rightFrame, text=str(self.id).zfill(4), font=("Arial Bold", TEXT), bg="white")
        self.label3.grid(column=0, row=1, columnspan=3)
        self.button1 = Button(self.rightFrame, text="1", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click1)
        self.button1.grid(column=0, row=2)
        self.button2 = Button(self.rightFrame, text="2", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click2)
        self.button2.grid(column=1, row=2)
        self.button3 = Button(self.rightFrame, text="3", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click3)
        self.button3.grid(column=2, row=2)
        self.button4 = Button(self.rightFrame, text="4", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click4)
        self.button4.grid(column=0, row=3)
        self.button5 = Button(self.rightFrame, text="5", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click5)
        self.button5.grid(column=1, row=3)
        self.button6 = Button(self.rightFrame, text="6", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click6)
        self.button6.grid(column=2, row=3)
        self.button7 = Button(self.rightFrame, text="7", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click7)
        self.button7.grid(column=0, row=4)
        self.button8 = Button(self.rightFrame, text="8", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click8)
        self.button8.grid(column=1, row=4)
        self.button9 = Button(self.rightFrame, text="9", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click9)
        self.button9.grid(column=2, row=4)
        self.buttonC = Button(self.rightFrame, text="C", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click_clear)
        self.buttonC.grid(column=0, row=5)
        self.button0 = Button(self.rightFrame, text="0", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click0)
        self.button0.grid(column=1, row=5)
        self.buttonOK = Button(self.rightFrame, text="OK", height=BUTTON_HEIGHT, width=BUTTON_WIDTH, font=("Arial Bold", TEXT), bg="white", command=self.click_ok)
        self.buttonOK.grid(column=2, row=5)
        self.tick()
        self.rfid_handler()

    def hide(self):
        if self.m_rfid is not None:
            self.window.after_cancel(self.m_rfid)
            self.m_rfid = None
        if self.m_time is not None:
            self.window.after_cancel(self.m_time)
            self.m_time = None
        self.leftFrame.grid_forget()
        self.rightFrame.grid_forget()

    def click_connection(self):
        self.hide()
        self.settingsPage.show(self.identifyPage, self.selectPage, self.numberPage, self.namePage, self.workPage, self.summaryPage, self.settingsPage, self.appData)

    def tick(self):
        now = time.strftime('%d.%m.%Y %H:%M:%S')
        self.labelTime.config(text=now)
        self.m_time = self.window.after(500, self.tick)

    def rfid_handler(self):
        try:
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            # ser = serial.Serial('COM7', 9600, timeout=1)
            ser.close()
            ser.open()
            if ser.isOpen() is True:
                ser.flushInput()
                ser.write(b'050020\r')
                res = ser.read(5)
                if res != b'0000\r':
                    res = ser.read(22)
                    ser.close()
                    if len(res) == 22 and res[21] == 13:
                        res = res[5:21]
                        uid = res.decode()
                        if len(uid) == 16:
                            self.appData.mConnection = pymssql.connect(server=self.appData.mServer, user=self.appData.mUser, password=self.appData.mPassword, database=self.appData.mDatabase)
                            cursor = self.appData.mConnection.cursor()
                            cursor.execute(f"SELECT * FROM empl_data WHERE TokenUID = '{uid}'")
                            row = cursor.fetchone()
                            if row is not None:
                                self.appData.mCurrentID = row[0]                    # empl_data(ID)                 => 33
                                self.appData.mCurrentHiquelNumber = row[1]          # empl_data(EmplIdentNumber)    => 1054
                                self.appData.mCurrentChipdriveNumber = row[2]       # empl_data(ChipdrIdNumber)     => 1136
                                self.appData.mCurrentName = row[4] + " " + row[5]   # empl_data(FirstName LastName) => Thomas Kaufmann
                                self.appData.mConnection.close()
                                self.handle_employee()
                            else:
                                self.label1.config(text="Nummer existiert nicht!\nMit RFID Token oder Tokennummer anmelden")
                                self.appData.mConnection.close()
                                self.m_rfid = self.window.after(200, self.rfid_handler)
                        else:
                            self.m_rfid = self.window.after(200, self.rfid_handler)
                    else:
                        self.m_rfid = self.window.after(200, self.rfid_handler)
                else:
                    ser.close()
                    self.m_rfid = self.window.after(200, self.rfid_handler)
            else:
                self.m_rfid = self.window.after(200, self.rfid_handler)
        except:
            self.m_rfid = self.window.after(200, self.rfid_handler)

    @staticmethod
    def get_numeric_input(i, c):
        if c == 0:
            r = i
        elif c < 10:
            r = c * 10 + i
        elif c < 100:
            r = c * 10 + i
        elif c < 1000:
            r = c * 10 + i
        else:
            r = 0
        return r

    def click0(self):
        self.id = self.get_numeric_input(0, self.id)
        self.label3.config(text=str(self.id).zfill(4))

    def click1(self):
        self.id = self.get_numeric_input(1, self.id)
        self.label3.config(text=str(self.id).zfill(4))

    def click2(self):
        self.id = self.get_numeric_input(2, self.id)
        self.label3.config(text=str(self.id).zfill(4))

    def click3(self):
        self.id = self.get_numeric_input(3, self.id)
        self.label3.config(text=str(self.id).zfill(4))

    def click4(self):
        self.id = self.get_numeric_input(4, self.id)
        self.label3.config(text=str(self.id).zfill(4))

    def click5(self):
        self.id = self.get_numeric_input(5, self.id)
        self.label3.config(text=str(self.id).zfill(4))

    def click6(self):
        self.id = self.get_numeric_input(6, self.id)
        self.label3.config(text=str(self.id).zfill(4))

    def click7(self):
        self.id = self.get_numeric_input(7, self.id)
        self.label3.config(text=str(self.id).zfill(4))

    def click8(self):
        self.id = self.get_numeric_input(8, self.id)
        self.label3.config(text=str(self.id).zfill(4))

    def click9(self):
        self.id = self.get_numeric_input(9, self.id)
        self.label3.config(text=str(self.id).zfill(4))

    def click_clear(self):
        self.id = 0
        self.label3.config(text=str(self.id).zfill(4))

    def click_ok(self):
        self.appData.mConnection = pymssql.connect(server=self.appData.mServer, user=self.appData.mUser, password=self.appData.mPassword, database=self.appData.mDatabase)
        cursor = self.appData.mConnection.cursor()
        cursor.execute(f"SELECT * FROM empl_data WHERE HiqTokenDescript = '{str(self.id).zfill(4)}'")
        row = cursor.fetchone()
        if row is not None:
            self.appData.mCurrentID = row[0]                    # empl_data(ID)                 => 33
            self.appData.mCurrentHiquelNumber = row[1]          # empl_data(EmplIdentNumber)    => 1054
            self.appData.mCurrentChipdriveNumber = row[2]       # empl_data(ChipdrIdNumber)     => 1136
            self.appData.mCurrentName = row[4] + " " + row[5]   # empl_data(FirstName LastName) => Thomas Kaufmann
            self.appData.mConnection.close()
            self.handle_employee()
        else:
            self.label1.config(text="Nummer existiert nicht!\nMit RFID Token oder Tokennummer anmelden")
            self.appData.mConnection.close()

    def handle_employee(self):
        self.appData.mConnection = pymssql.connect(server=self.appData.mServer, user=self.appData.mUser, password=self.appData.mPassword, database=self.appData.mDatabase)
        cursor = self.appData.mConnection.cursor()
        cursor.execute(f"SELECT * FROM empl_curstatus WHERE EmplIdentNumber = '{self.appData.mCurrentHiquelNumber}'")
        row = cursor.fetchone()
        if row is not None and row[1] is not None:
            self.appData.mCurrentWorkState = row[1]     # empl_curstatus(CurWorkState)  => 1: in, 0: out
        else:
            self.appData.mCurrentWorkState = ""
        if row is not None and row[2] is not None:
            self.appData.mCurrentRefId = row[2]         # empl_curstatus(CurRefId)      => PAxxxxxxxx/AUxxxxxxxx
        else:
            self.appData.mCurrentRefId = ""
        if row is not None and row[3] is not None:
            self.appData.mCurrentSubRefId = row[3]      # empl_curstatus(CurSubRefId)   => 6543/RAH113357 2.A
        else:
            self.appData.mCurrentSubRefId = ""
        if row is not None and row[4] is not None:
            self.appData.mCurrentTaskId = row[4]        # empl_curstatus(CurTask)       => 70: coding
        else:
            self.appData.mCurrentTaskId = ""
        if self.appData.mCurrentTaskId != "":
            cursor.execute(f"SELECT * FROM action_data WHERE ActionId = '{self.appData.mCurrentTaskId}'")
            row = cursor.fetchone()
            if row is not None and row[4] is not None:
                self.appData.mCurrentTask = row[4]
            else:
                self.appData.mCurrentTask = ""
        if 'PA' in self.appData.mCurrentRefId or 'AU' in self.appData.mCurrentRefId:
            cursor.execute(f"SELECT * FROM reference_data WHERE RefId = '{self.appData.mCurrentRefId}'")
            row = cursor.fetchone()
            if row is not None and row[3] is not None:
                self.appData.mCurrentRefIdName = row[3]
            else:
                self.appData.mCurrentRefIdName = ""
            if row is not None and row[4] is not None:
                self.appData.mCurrentSubRefId = row[4]
            else:
                self.appData.mCurrentSubRefId = ""
        else:
            self.appData.mCurrentRefIdName = ""
            # Don't change mCurrentSubRefId if no mCurrentRefId
        self.appData.mConnection.close()
        self.hide()
        self.selectPage.show(self.identifyPage, self.selectPage, self.numberPage, self.namePage, self.workPage, self.summaryPage, self.settingsPage, self.appData)
