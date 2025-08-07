# Design automation script which accept directory name and file extension from user . Display all files with that extension. Show output in log file.
# Accept input through command line.
#  Display message in log file instead of console

import os 
import sys

def FindingFilewithExtension(Directory,Extension):
    flag = os.path.isabs(Directory)

    if(flag == False):
        DirectoryName = os.path.abspath(Directory)

    flag = os.path.exists(Directory)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but the target is not a directory")
        exit()
    
    fobj = "Marvellouslog.log"       
    file = open(fobj,'w')

    for FolderName , SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            if(fname.endswith(Extension)):
                file.write(fname+"\n")

def main():
    
    Border=51*'-'
    print(Border)
    print("--------------- Assignment of Automation ----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory Expected_Extention")
            print("Please provide valid absolute path")

    elif(len(sys.argv) == 3):
        FindingFilewithExtension(sys.argv[1], sys.argv[2])

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 

    print(Border)
    print("----------- Thank you for using script -----------")
    print(Border)




if __name__=="__main__":
    main()