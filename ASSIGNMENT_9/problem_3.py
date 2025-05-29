# 3. Create a Python program that uses multiprocessing.Pool to compute
# factorial of numbers in a list.

import multiprocessing
import time


def factorial(No):
        Fact = 1
        for i in range(No,0,-1):
            Fact = Fact * i 

        return Fact


        
def main():
    start_time = time.time()
    print("Enter the size : ",end = "")
    size = int(input())

    Data = []
    Result = []

    for i in range(size):
        Data.append(int(input()))

    P = multiprocessing.Pool()
    Result = P.map(factorial,Data)

    P.close()
    P.join()

    end_time = time.time()

    print("factorial is : ",Result)
    print("time taken : ",(end_time - start_time))

    print("End of main")

if __name__ == "__main__":
    main()