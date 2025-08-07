# Design automation script which accept two directory names and one file extension. Copy all files with the specific extension from first directory into second directory.Second directory should be created at run time.


import os 
import sys
import shutil

def DirectoryCopy(sou_directory,Den_directory,Extension):
    flag = os.path.exists(sou_directory)

    if(flag == False):
        print("The path is invalid")
        exit()


    sou_directory = os.path.abspath(sou_directory)
    Den_directory = os.path.abspath(Den_directory)

    if not os.path.exists(Den_directory):
        os.makedirs(Den_directory)

    
    
    fobj = "Demolog.log"
    file = open(fobj,'w')

    for FolderName , SubFolderNames, FileNames in os.walk(sou_directory):
        for fname in FileNames:
            if(fname.endswith(Extension)):
                src_file = os.path.join(FolderName, fname)
                dst_file = os.path.join(Den_directory, fname)
                shutil.copy2(src_file,dst_file)
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

    elif(len(sys.argv) == 4):
        DirectoryCopy(sys.argv[1], sys.argv[2], sys.argv[3])

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