# 4. Create a Python program that Compare execution time of summing
# numbers from 1 to 10 million using normal function, threading, and
# multiprocessing.

import multiprocessing
import threading
import time


def Summation(no):
    sum = 0
    for i in range(no+1):
        sum = sum + i

    print("Summation is : ",sum)

def main():

    Value = 10000000

    start_time = time.time()
    Summation(Value)
    end_time = time.time()
    print("normal function execution time : ",(end_time - start_time))

    start_time = time.time()
    T1 = threading.Thread(target = Summation, args = (Value,))
    end_time = time.time()
    print("Threading function execution time : ",(end_time - start_time))

    start_time = time.time()
    T1 = multiprocessing.Process(target = Summation, args = (Value,))
    end_time = time.time()
    print("Multiprocessing function execution time : ",(end_time - start_time))

    print("End of main")

if __name__ == "__main__":
    main()