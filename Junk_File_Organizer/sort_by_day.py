import os
import datetime
from pathlib import Path


class SortByDay:
    def folder_creation(self, date_folder, dir_path):
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
            directories_path = os.path.join(dir_path, FOLDER_NAME)
            directories_path = Path(directories_path)
            directories_path.mkdir(exist_ok=True)

    def only_file(self, files, dir_path, only_files):
        for current_file in files:
            old_path = os.path.join(dir_path, current_file)
            isFile = os.path.isdir(old_path)
            if isFile:
                continue
            only_files.append(current_file)

    def total_days(self, only_files, dir_path, mvr):
        for file in only_files:
            mtime = (os.stat(os.path.join(dir_path, file)).st_mtime)
            x = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
            y = datetime.datetime.now().strftime('%Y-%m-%d')
            d1 = datetime.date(int(x[:4]), int(x[5:7]), int(x[8:]))
            d2 = datetime.date(int(y[:4]), int(y[5:7]), int(y[8:]))
            d3 = (d2-d1).days
            old_path = os.path.join(dir_path, file)
            mvr.append([d3, old_path, file])

    def moves(self, mvr, dir_path):
        for days, old_path, file in mvr:
            isFile = os.path.isdir(old_path)
            if(isFile):
                continue
            if days >= 0 and days <= 10:
                FOLDER_NAME = "Files created 10 days ago"
                new_path = os.path.join(dir_path, FOLDER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 11 and days <= 20:
                FOLDER_NAME = "Files created btwn 10-20 days ago"
                new_path = os.path.join(dir_path, FOLDER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 21 and days <= 30:
                FOLDER_NAME = "Files created btwn 20days to 1month ago"
                new_path = os.path.join(dir_path, FOLDER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 31 and days <= 60:
                FOLDER_NAME = "Files created btwn 30-60 days ago"
                new_path = os.path.join(dir_path, FOLDER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 61 and days <= 90:
                FOLDER_NAME = "Files created btwn 60-90 days ago"
                new_path = os.path.join(dir_path, FOLDER_NAME, file)
                os.rename(old_path, new_path)
            elif days >= 91 and days <= 180:
                FOLDER_NAME = "Files created btwn 3-6 months ago"
                new_path = os.path.join(dir_path, FOLDER_NAME, file)
                os.rename(old_path, new_path)
            else:
                FOLDER_NAME = "Files Older than 6 months"
                new_path = os.path.join(dir_path, FOLDER_NAME, file)
                os.rename(old_path, new_path)

    def extra_folder(self, dir_path):
        folders = list(os.walk(dir_path))[1:]
        for folder in folders:
            if not folder[2]:
                os.rmdir(folder[0])


def date_and_time(dir_path):
    files = os.listdir(dir_path)
    only_files = []
    date_folder = [0, 10, 20, 30, 40, 60, 90]
    mvr = []
    obj = SortByDay()
    obj.folder_creation(date_folder, dir_path)
    obj.only_file(files, dir_path, only_files)
    obj.total_days(only_files, dir_path, mvr)
    obj.moves(mvr, dir_path)
    obj.extra_folder(dir_path)
