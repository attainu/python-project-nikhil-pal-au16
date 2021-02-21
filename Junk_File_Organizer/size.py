import os
from pathlib import Path


class Size:
    def create_directory(self, size, DIR_PATH):
        for D in size:
            if D == 0:
                FOLDER_NAME = 'Files lessthan 1MB'
            elif D == 1048576:
                FOLDER_NAME = 'Files Between 1MB_to _10MB'
            elif D == 10485760:
                FOLDER_NAME = 'Files Between 10MB_to_100MB'
            elif D == 104857600:
                FOLDER_NAME = 'Files Between 100MB_to_500MB'
            elif D == 524288000:
                FOLDER_NAME = 'Files Between 500_to_1GB'
            elif D == 1073741274:
                FOLDER_NAME = 'Files larger than 1GB'
            directories_path = os.path.join(DIR_PATH, FOLDER_NAME)
            directories_path = Path(directories_path)
            directories_path.mkdir(exist_ok=True)

    def size_calculation(self, ALL_FILES, DIR_PATH, sizer):
        for FILES in ALL_FILES:
            file_path = Path(FILES)
            PATH = (os.path.join(DIR_PATH, FILES))
            SIZE_OF_CURRENT_FILE = (os.path.getsize(PATH))
            old_path = os.path.join(DIR_PATH, file_path)
            sizer.append([SIZE_OF_CURRENT_FILE, old_path, FILES])

    def transfer(self, sizer, DIR_PATH):
        for SIZE_OF_FILE, OLD_PATH_CURRENT_FILE, FILES_NAME in sizer:
            isFile = os.path.isdir(OLD_PATH_CURRENT_FILE)
            if isFile:
                continue
            if SIZE_OF_FILE >= 0 and SIZE_OF_FILE < 1048576:
                FOLDER_NAME = 'Files lessthan 1MB'
                x = os.path.join(DIR_PATH, FOLDER_NAME, FILES_NAME)
                new_path = x
                os.rename(OLD_PATH_CURRENT_FILE, new_path)
            elif SIZE_OF_FILE >= 1048576 and SIZE_OF_FILE < 10485760:
                FOLDER_NAME = 'Files Between 1MB_to _10MB'
                x = os.path.join(DIR_PATH, FOLDER_NAME, FILES_NAME)
                new_path = x
                os.rename(OLD_PATH_CURRENT_FILE, new_path)

            elif SIZE_OF_FILE >= 10485760 and SIZE_OF_FILE < 104857600:
                FOLDER_NAME = 'Files Between 10MB_to_100MB'
                x = os.path.join(DIR_PATH, FOLDER_NAME, FILES_NAME)
                new_path = x
                os.rename(OLD_PATH_CURRENT_FILE, new_path)

            elif SIZE_OF_FILE >= 104857600 and SIZE_OF_FILE < 524288000:
                FOLDER_NAME = 'Files Between 100MB_to_500MB'
                x = os.path.join(DIR_PATH, FOLDER_NAME, FILES_NAME)
                new_path = x
                os.rename(OLD_PATH_CURRENT_FILE, new_path)

            elif SIZE_OF_FILE >= 524288000 and SIZE_OF_FILE < 1073741274:
                FOLDER_NAME = 'Files Between 500_to_1GB'
                x = os.path.join(DIR_PATH, FOLDER_NAME, FILES_NAME)
                new_path = x
                os.rename(OLD_PATH_CURRENT_FILE, new_path)

            else:
                FOLDER_NAME = 'Files larger than 1GB'
                x = os.path.join(DIR_PATH, FOLDER_NAME, FILES_NAME)
                new_path = x
                os.rename(OLD_PATH_CURRENT_FILE, new_path)

    def extrafolder(self, DIR_PATH):
        folders = list(os.walk(DIR_PATH))[1:]
        for folder in folders:
            if not folder[2]:
                os.rmdir(folder[0])


def SIZEORG(DIR_PATH):
    ALL_FILES = os.listdir(DIR_PATH)
    sizer = []
    size = [0, 1048576, 10485760, 104857600, 524288000, 1073741274]

    obj = Size()
    obj.create_directory(size, DIR_PATH)
    obj.size_calculation(ALL_FILES, DIR_PATH, sizer)
    obj.transfer(sizer, DIR_PATH)
    obj.extrafolder(DIR_PATH)
