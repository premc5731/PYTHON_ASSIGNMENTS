# 3. Create a Python program that uses multiprocessing.Pool to compute
# factorial of numbers in a list.

import multiprocessing
import time


def Factorial(No):
        fact = 1
        for i in range(No,0,-1):
            fact = fact * i 

        return fact


        
def main():
    start_time = time.time()
    print("Enter the size : ",end = "")
    size = int(input())

    data = []
    result = []

    for i in range(size):
        data.append(int(input()))

    P = multiprocessing.Pool()
    result = P.map(Factorial,data)

    P.close()
    P.join()

    end_time = time.time()

    print("factorial is : ",result)
    print("time taken : ",(end_time - start_time))

    print("End of main")

if __name__ == "__main__":
    main()