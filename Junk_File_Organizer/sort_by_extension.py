import os
from pathlib import Path


class SortByExtension:
    def extension(self, dir_path, file_extension, ALL_FILES):
        for FILES in ALL_FILES:
            file_path = Path(FILES)
            removind_dot = file_path.suffix.lower()
            removind_dot = removind_dot[1::]
            file_extension.append(removind_dot)

    def directory_creation(self, file_extension, dir_path):
        for D in file_extension:
            directories_path = os.path.join(dir_path, D)
            directories_path = Path(directories_path)
            directories_path.mkdir(exist_ok=True)

    def movables(self, all_files, dir_path):
        for FILES in all_files:
            file_path = Path(FILES)
            exten = file_path.suffix.lower()
            exten = exten[1::]
            old_path = os.path.join(dir_path, file_path)
            new_path = os.path.join(dir_path, exten, FILES)
            os.rename(old_path, new_path)

    def extra_folder(self, dir_path):
        folders = list(os.walk(dir_path))[1:]
        for folder in folders:
            if not folder[2]:
                os.rmdir(folder[0])


def ext(dir_path):
    ALL_FILES = os.listdir(dir_path)
    file_extension = []
    obj = SortByExtension()
    obj.extension(dir_path, file_extension, ALL_FILES)
    obj.directory_creation(file_extension, dir_path)
    obj.movables(ALL_FILES, dir_path)
    obj.extra_folder(dir_path)
