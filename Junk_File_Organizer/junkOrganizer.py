from exten import EXT
from Timeandate import DATESANDTIMES
from size import SIZEORG
import os


class junkOrganizer:
    def __init__(self):
        self.DIR_PATH = 'E:\\NIKHIL'+'\\'
        self.SRC_PATH = r'E:\\NIKHIL'+'\\'

    def exten(self, v):
        EXT(v)

    def DATES(self, v):
        DATESANDTIMES(v)

    def SIZE(self, v):
        SIZEORG(v)


def Dictionary(A, B):
    d = {1: "ORGANISE BY Extension\n",
         2: "ORGANISE BY DATE\n",
         3: "ORGANISE BY SIZE\n"}
    if len(A) == 1 or len(A) == 0:
        return
    if not os.path.exists(A):
        return
    inputChoice(A, B)
    print(d[B])


def inputChoice(A, B):
    obj = junkOrganizer()
    if B == 1:
        obj.exten(A)
    if B == 2:
        obj.DATES(A)
    if B == 3:
        obj.SIZE(A)
    if B > 3:
        print("your selection is not valid")
