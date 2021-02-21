import os
import datetime
from pathlib import Path


class Timeandate:
    def folderCreation(self, date_folder, DIR_PATH):
        for dates in date_folder:
            if dates == 0:
                FOLDER_NAME = "Files created 10 days ago"
            elif dates == 10:
                FOLDER_NAME = "File created From day-10 to day-19"
            elif dates == 20:
                FOLDER_NAME = "Files created btwn 20days to 1month ago"
            elif dates == 30:
                FOLDER_NAME = "Files created btwn 30-60 days ago"
            elif dates == 40:
                FOLDER_NAME = "Files created btwn 60-90 days ago"
            elif dates == 60:
                FOLDER_NAME = "Files created btwn 3-6 months ago"
            else:
                FOLDER_NAME = "Files Older than 6 months"
            directories_path = os.path.join(DIR_PATH, FOLDER_NAME)
            directories_path = Path(directories_path)
            directories_path.mkdir(exist_ok=True)

    def onlyfile(self, files, DIR_PATH, only_files):
        for current_file in files:
            old_path = os.path.join(DIR_PATH, current_file)
            isFile = os.path.isdir(old_path)
            if isFile:
                continue
            only_files.append(current_file)

    def totaldays(self, only_files, DIR_PATH, mvr):
        for file in only_files:
            mtime = (os.stat(os.path.join(DIR_PATH, file)).st_mtime)
            x = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
            y = datetime.datetime.now().strftime('%Y-%m-%d')
            d1 = datetime.date(int(x[:4]), int(x[5:7]), int(x[8:]))
            d2 = datetime.date(int(y[:4]), int(y[5:7]), int(y[8:]))
            d3 = (d2-d1).days
            old_path = os.path.join(DIR_PATH, file)
            mvr.append([d3, old_path, file])

    def moves(self, mvr, DIR_PATH):
        for days, old_path, file in mvr:
            isFile = os.path.isdir(old_path)
            if(isFile):
                continue
            if days >= 0 and days <= 10:
                FOLDER_NAME = "Files created 10 days ago"
                new_path = os.path.join(DIR_PATH, FOLDER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 11 and days <= 20:
                FOLDER_NAME = "Files created btwn 10-20 days ago"
                new_path = os.path.join(DIR_PATH, FOLDER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 21 and days <= 30:
                FOLDER_NAME = "Files created btwn 20days to 1month ago"
                new_path = os.path.join(DIR_PATH, FOLDER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 31 and days <= 60:
                FOLDER_NAME = "Files created btwn 30-60 days ago"
                new_path = os.path.join(DIR_PATH, FOLDER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 61 and days <= 90:
                FOLDER_NAME = "Files created btwn 60-90 days ago"
                new_path = os.path.join(DIR_PATH, FOLDER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 91 and days <= 180:
                FOLDER_NAME = "Files created btwn 3-6 months ago"
                new_path = os.path.join(DIR_PATH, FOLDER_NAME, file)
                os.rename(old_path, new_path)
            else:
                FOLDER_NAME = "Files Older than 6 months"
                new_path = os.path.join(DIR_PATH, FOLDER_NAME, file)
                os.rename(old_path, new_path)

    def extrafolder(self, DIR_PATH):
        folders = list(os.walk(DIR_PATH))[1:]
        for folder in folders:
            if not folder[2]:
                os.rmdir(folder[0])


def DATESANDTIMES(DIR_PATH):
    files = os.listdir(DIR_PATH)
    only_files = []
    date_folder = [0, 10, 20, 30, 40, 60, 90]
    mvr = []
    obj = Timeandate()
    obj.folderCreation(date_folder, DIR_PATH)
    obj.onlyfile(files, DIR_PATH, only_files)
    obj.totaldays(only_files, DIR_PATH, mvr)
    obj.moves(mvr, DIR_PATH)
    obj.extrafolder(DIR_PATH)
