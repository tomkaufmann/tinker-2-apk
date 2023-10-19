from os import path
from platform import uname


class AppData:
    def __init__(self):
        self.mPAOnAUOff = True
        # Current employee
        self.mCurrentID = 0                 # empl_data[0](ID)                      => 35
        self.mCurrentHiquelNumber = ""      # empl_data[1](EmplIdentNumber)         => 1054
        self.mCurrentChipdriveNumber = ""   # empl_data[2](ChipdrIdNumber)          => 1136
        self.mCurrentName = ""              # empl_data[4][5](FirstName)(LastName)  => Thomas Kaufmann
        self.mCurrentWorkState = ""         # empl_curstatus[10](CurWorkState)      => 1: in, 0: out
        self.mCurrentRefId = ""             # empl_curstatus[11](CurRefId)          => PAxxxxxxxx/AUxxxxxxxx
        self.mCurrentSubRefId = ""          # empl_curstatus[4](CurSubRefId)        => 6543/RAH113357 2.A                   reference_data[4](subRefId)
        self.mCurrentTaskId = ""            # empl_curstatus[12](CurTask)           => 70
        self.mCurrentTask = ""              # action_data[4](RefIdName)             => Programmieren
        self.mCurrentAction = ""            # trans_data[4](Typ)                    => K, G or PW
        self.mCurrentRefIdName = ""         # reference_data[3](RefIdName)          => SLS-EXT-KLIMA_0401_THT.../KNAPP  AG
        # Database
        self.mClientName = uname()[1]
        self.mServer = ""
        self.mDatabase = ""
        self.mUser = ""
        self.mPassword = ""
        # Name page parameter
        self.mNamePageParameter = False
        if path.exists("./tr.hiq"):
            with open("./tr.hiq") as file:
                self.mServer = file.readline().strip()
                self.mDatabase = file.readline().strip()
                self.mUser = file.readline().strip()
                self.mPassword = file.readline().strip()
        else:
            with open("./tr.hiq", mode="w") as file:
                self.mServer = "bk-axd-01\\Axprod"
                self.mDatabase = "timedata"
                self.mUser = "TimedataUserRw"
                self.mPassword = "TimedataUserRw%#$"
                file.write(self.mServer + "\n")
                file.write(self.mDatabase + "\n")
                file.write(self.mUser + "\n")
                file.write(self.mPassword + "\n")
        self.mConnection = None
