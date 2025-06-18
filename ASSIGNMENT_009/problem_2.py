# 2. Write a Python program using multiprocessing.Process to square a list of numbers 
# using multiple processes.

import multiprocessing
import os


def Square(RData):
    print("process id :",os.getpid())
    for i in RData:
        s_no = i*i
        print("square of {} is {}".format(i,s_no))



def main():
    Data = []
    print("Enter size of list : ",end = "")
    size = int(input())

    for i in range(size):
        Data.append(int(input()))


    P1 = multiprocessing.Process(target = Square,args = (Data,))
    P2 = multiprocessing.Process(target = Square,args = (Data,))
    

    P1.start()
    P2.start()
    

    P1.join()
    P2.join()

if __name__ == "__main__":
    main()