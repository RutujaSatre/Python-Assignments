# Design automation script which accept two directory names. Copy all files from first directory into second directory should be created at run time.
# Accept input through command line.


import os 
import sys
import shutil

def DirectoryCopy(sou_directory,Den_directory):
    flag = os.path.exists(sou_directory)

    if(flag == False):
        print("The path is invalid")
        exit()


    sou_directory = os.path.abspath(sou_directory)
    Den_directory = os.path.abspath(Den_directory)

    if not os.path.exists(Den_directory):
        os.makedirs(Den_directory)

    else:
        print("Folder already exists")

    for directory in os.listdir(sou_directory):
        sourcepath = os.path.join(sou_directory,directory)
        dest_path = os.path.join(Den_directory,directory)

        if os.path.isfile(sourcepath):
            shutil.copy(sourcepath,dest_path)


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
        DirectoryCopy(sys.argv[1], sys.argv[2])

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