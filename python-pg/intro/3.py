import os

START_DIR = "."


def traversal():
    for currdir, subdirs, files in os.walk(START_DIR):
        for file in files:
            if file.endswith('.py'):
                fullpath = os.path.join(currdir, file)
                fsize = os.path.getsize(fullpath)
                print("{:8d} {:s}".format(fsize, fullpath))


if __name__ == '__main__':
    traversal()