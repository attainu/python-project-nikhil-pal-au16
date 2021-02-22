import os
from pathlib import Path


class SortBySize:
    def create_directory(self, size, dir_path):
        for d in size:
            if d == 0:
                folder_name = 'Files lessthan 1MB'
            elif d == 1048576:
                folder_name = 'Files Between 1MB_to _10MB'
            elif d == 10485760:
                folder_name = 'Files Between 10MB_to_100MB'
            elif d == 104857600:
                folder_name = 'Files Between 100MB_to_500MB'
            elif d == 524288000:
                folder_name = 'Files Between 500_to_1GB'
            elif d == 1073741274:
                folder_name = 'Files larger than 1GB'
            directories_path = os.path.join(dir_path, folder_name)
            directories_path = Path(directories_path)
            directories_path.mkdir(exist_ok=True)

    def size_calculation(self, all_files, dir_path, sizer):
        for files in all_files:
            file_path = Path(files)
            PATH = (os.path.join(dir_path, files))
            size_of_current_file = (os.path.getsize(PATH))
            old_path = os.path.join(dir_path, file_path)
            sizer.append([size_of_current_file, old_path, files])

    def transfer(self, sizer, dir_path):
        for size_of_file, old_path_current_file, files_name in sizer:
            isFile = os.path.isdir(old_path_current_file)
            if isFile:
                continue
            if size_of_file >= 0 and size_of_file < 1048576:
                folder_name = 'Files lessthan 1MB'
                x = os.path.join(dir_path, folder_name, files_name)
                new_path = x
                os.rename(old_path_current_file, new_path)
            elif size_of_file >= 1048576 and size_of_file < 10485760:
                folder_name = 'Files Between 1MB_to _10MB'
                x = os.path.join(dir_path, folder_name, files_name)
                new_path = x
                os.rename(old_path_current_file, new_path)

            elif size_of_file >= 10485760 and size_of_file < 104857600:
                folder_name = 'Files Between 10MB_to_100MB'
                x = os.path.join(dir_path, folder_name, files_name)
                new_path = x
                os.rename(old_path_current_file, new_path)

            elif size_of_file >= 104857600 and size_of_file < 524288000:
                folder_name = 'Files Between 100MB_to_500MB'
                x = os.path.join(dir_path, folder_name, files_name)
                new_path = x
                os.rename(old_path_current_file, new_path)

            elif size_of_file >= 524288000 and size_of_file < 1073741274:
                folder_name = 'Files Between 500_to_1GB'
                x = os.path.join(dir_path, folder_name, files_name)
                new_path = x
                os.rename(old_path_current_file, new_path)

            else:
                folder_name = 'Files larger than 1GB'
                x = os.path.join(dir_path, folder_name, files_name)
                new_path = x
                os.rename(old_path_current_file, new_path)

    def extra_folder(self, dir_path):
        folders = list(os.walk(dir_path))[1:]
        for folder in folders:
            if not folder[2]:
                os.rmdir(folder[0])


def size_org(dir_path):
    all_files = os.listdir(dir_path)
    sizer = []
    size = [0, 1048576, 10485760, 104857600, 524288000, 1073741274]

    obj = SortBySize()
    obj.create_directory(size, dir_path)
    obj.size_calculation(all_files, dir_path, sizer)
    obj.transfer(sizer, dir_path)
    obj.extra_folder(dir_path)
