import os
from pathlib import Path


class Exten:
    def extension(self, DIR_PATH, File_extension, ALL_FILES):
        for FILES in ALL_FILES:
            file_path = Path(FILES)
            REMOVIND_DOT = file_path.suffix.lower()
            REMOVIND_DOT = REMOVIND_DOT[1::]
            File_extension.append(REMOVIND_DOT)

    def directoryCreation(self, File_extension, DIR_PATH):
        for D in File_extension:
            directories_path = os.path.join(DIR_PATH, D)
            directories_path = Path(directories_path)
            directories_path.mkdir(exist_ok=True)

    def movables(self, ALL_FILES, DIR_PATH):
        for FILES in ALL_FILES:
            file_path = Path(FILES)
            EXTENSION = file_path.suffix.lower()
            EXTENSION = EXTENSION[1::]
            old_path = os.path.join(DIR_PATH, file_path)
            new_path = os.path.join(DIR_PATH, EXTENSION, FILES)
            os.rename(old_path, new_path)

    def extrafolder(self, DIR_PATH):
        folders = list(os.walk(DIR_PATH))[1:]
        for folder in folders:
            if not folder[2]:
                os.rmdir(folder[0])


def EXT(DIR_PATH):
    ALL_FILES = os.listdir(DIR_PATH)
    File_extension = []
    obj = Exten()
    obj.extension(DIR_PATH, File_extension, ALL_FILES)
    obj.directoryCreation(File_extension, DIR_PATH)
    obj.movables(ALL_FILES, DIR_PATH)
    obj.extrafolder(DIR_PATH)
