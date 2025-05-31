# Write a python program using multiprocessing. Process to square a list of numbers using multiple processes.

import multiprocessing

def Chksquare(no):
    return no * no

def main():
    num = [1,2,3,4,5]

    p=multiprocessing.Pool()
    result=p.map(Chksquare,num)

    p.close()
    p.join()

    print(result)

if __name__=="__main__":
    main()