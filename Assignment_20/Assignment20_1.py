# Design automation script which accept directory name and display checksum of all files.
# Accept input through command line or through file.
# Display any message in log file instead of console.

import time
import sys
import os
import hashlib  

def CalculateChecksum(path, BlockSize = 1024):
    fobj = open(path ,'rb')  

    hobj = hashlib.md5()       
    buffer = fobj.read(BlockSize)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName):

    flag = os.path.isabs(DirectoryName)

    if(flag==False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag==False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag==False):
        print("Path is valid but the target is not a directory")
        exit()
    File = 'Checksumlogfile.log'
    fobj = open(File,'w')

    for FolderName , SubFolderNames , FileNames in os.walk(DirectoryName):
        for fname in FileNames:
           fname = os.path.join(FolderName,fname)
           checksum = CalculateChecksum(fname)
           fobj.write("Filen name is : "+fname+'\n\n')
           fobj.write("Checksum is : "+checksum+'\n\n')
      


def main():
 
    Border = "-"*54
    print(Border)
    print("---------------Marvellous Automation--------------------")
    print(Border)

    if(len(sys.argv)==2):
        if((sys.argv[1] == "--h") or (sys.argv[1]=="--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1]=="--U")):
            print("Use the given script as ")
            print("ScriptName.py NameOfDirectory")
            print("Please provide valid absolute path")

        else:
            DirectoryWatcher(sys.argv[1])

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : used to display the usage")

    print(Border)
    print("--------------Thank you for using our script--------------")
    print("--------------Marvellous Infosystem---------------------")
    print(Border)

    

if __name__=="__main__":
    main()