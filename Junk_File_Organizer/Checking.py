import os


class Checking:
    def file_check(self, SRC_PATH, DIR_PATH):
        for path, _, files in os.walk(SRC_PATH):
            if files:
                for Files in files:
                    if not os.path.isfile(DIR_PATH+Files):
                        os.rename(path+'\\'+Files, DIR_PATH+Files)

    def folder_remove(self, DIR_PATH):
        folders = list(os.walk(DIR_PATH))[1:]
        for folder in folders:
            if not folder[2]:
                os.rmdir(folder[0])


def main(SRC_PATH, DIR_PATH):
    if len(SRC_PATH) == 1:
        print("Enter a valid Path")
        return
    if not os.path.exists(SRC_PATH):
        print("Enter a valid path")
        return
    obj = Checking()
    obj.file_check(SRC_PATH, DIR_PATH)
    obj.folder_remove(DIR_PATH)