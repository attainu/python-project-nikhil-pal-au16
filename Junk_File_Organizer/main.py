from checking_path import main
from file_organizer import Dictionary


class DriverCode:
    def __init__(self, path, y):
        self.DIR_PATH = path
        self.SRC_PATH = path
        self.choice = y
        if y >= 5:
            print("Enter the Valid Choice")
            return
        main(self.SRC_PATH, self.DIR_PATH)

    def Run(self):
        if self.choice >= 4:
            return
        Dictionary(self.DIR_PATH, self.choice)


if __name__ == "__main__":
    while True:
        print("\nPress 1 to Sort By Extension\n")
        print("Press 2 to Sort By Day\n")
        print("Press 3 to Sort By Size\n")
        print("Press 'Q' or 'q' to exit\n")
        pathh = input("ENTER PATH\n")
        pathh = r''+pathh+'\\'
        if len(pathh) == 2:
            break
        choice = int(input("Enter Your Choice\n"))
        obj = DriverCode(pathh, choice)
        obj.Run()
