from sort_by_extension import ext
from sort_by_day import date_and_time
from sort_by_size import size_org
import os


class FileOrganizer:
    def __init__(self):
        self.dir_path = 'E:\\NIKHIL'+'\\'
        self.src_path = r'E:\\NIKHIL'+'\\'

    def extension(self, v):
        ext(v)

    def day(self, v):
        date_and_time(v)

    def size(self, v):
        size_org(v)


def dictionary(A, B):
    d = {1: "Sort By Extension\n",
         2: "Sort By Day\n",
         3: "Sort By Size\n"}
    if len(A) == 1 or len(A) == 0:
        return
    if not os.path.exists(A):
        return
    input_choice(A, B)
    print(d[B])


def input_choice(A, B):
    obj = FileOrganizer()
    if B == 1:
        obj.extension(A)
    if B == 2:
        obj.day(A)
    if B == 3:
        obj.size(A)
    if B > 3:
        print("your selection is not valid")
