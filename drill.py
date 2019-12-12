
import os


def getTxtFile():
    path = "c:\\test\\"
    files = os.listdir(path)
    for i in files:
        name, ext = os.path.splitext(i)
        if ext == ".txt":
            abspath = os.path.join(path, i)
            time = os.path.getmtime(abspath)
            print(i, time)





__name__ == "__main__"
getTxtFile()
        




