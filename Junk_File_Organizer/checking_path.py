import os


class CheckingPath:
    def file_check(self, src_path, dir_path):
        for path, _, files in os.walk(src_path):
            if files:
                for Files in files:
                    if not os.path.isfile(dir_path+Files):
                        os.rename(path+'\\'+Files, dir_path+Files)

    def folder_remove(self, dir_path):
        folders = list(os.walk(dir_path))[1:]
        for folder in folders:
            if not folder[2]:
                os.rmdir(folder[0])


def main(src_path, dir_path):
    if len(src_path) == 1:
        print("Enter a valid Path")
        return
    if not os.path.exists(src_path):
        print("Enter a valid path")
        return
    obj = CheckingPath()
    obj.file_check(src_path, dir_path)
    obj.folder_remove(dir_path)
