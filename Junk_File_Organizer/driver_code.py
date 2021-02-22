from checking_path import main
from file_organizer import dictionary


class DriverCode:
    def __init__(self, path, y):
        self.dir_path = path
        self.src_path = path
        self.choice = y
        if y >= 5:
            print("Enter the Valid Choice")
            return
        main(self.src_path, self.dir_path)

    def run(self):
        if self.choice >= 4:
            return
        dictionary(self.dir_path, self.choice)


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
        obj.run()
