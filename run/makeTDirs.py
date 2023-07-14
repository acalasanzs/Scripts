import os
import warnings
from sys import argv
from utils import get_immediate_subdirectories, sure
workdir = False
homedir = workdir
def main():
    dirNames = get_immediate_subdirectories(workdir)
    #Create Dirs
    os.chdir(homedir)
    if(os.listdir(os.getcwd())):
        warnings.warn("Already with content in it!")
        sure()
    all = False
    for x in dirNames:
        try:
            os.mkdir(x)
        except:
            if(not all):
                warnings.warn(f"{x} already exists!")
                all = sure(True)
                print("Skiping...")
            continue
    print("SUCCESS!")
if __name__ == "__main__":
    if(len(argv) < 2):
        workdir = input("From dir: ")
        homedir = input("To dir: ")
    else:
        workdir = argv[1]
        homedir = argv[2]
    main()