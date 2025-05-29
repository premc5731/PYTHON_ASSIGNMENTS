# 3.Design python application which creates two threads as evenlist and oddlist. Both
# the threads accept list of integers as parameter. Evenlist thread add all even 
# elements from input list and display the addition. Oddlist thread add all odd elements 
# from input list and display the addition. 

import threading

def EvenList(Elist):
    Sum = 0
    for i in Elist:
        if i % 2 == 0:
            Sum = Sum + i

    print("Evenlist Sum : ",Sum)

def OddList(Olist):
    Sum = 0
    for i in Olist:
        if i % 2 != 0:
            Sum = Sum + i

    print("Oddlist Sum : ",Sum)



def main():
    Data = []
    print("Enter a number : ",end="")
    Value = int(input())

    for i in range(Value):
        Data.append(int(input()))

    T1 = threading.Thread(target = EvenList,args = (Data,))
    T2 = threading.Thread(target = OddList,args = (Data,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("end of main")

if __name__ == "__main__":
    main()