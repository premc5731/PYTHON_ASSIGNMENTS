# 3.Design python application which creates two threads as evenlist and oddlist. Both
# the threads accept list of integers as parameter. Evenlist thread add all even 
# elements from input list and display the addition. Oddlist thread add all odd elements 
# from input list and display the addition. 

import threading

def EvenList(e_list):
    sum = 0
    for i in e_list:
        if i % 2 == 0:
            sum = sum + i

    print("Evenlist sum : ",sum)

def OddList(o_list):
    sum = 0
    for i in o_list:
        if i % 2 != 0:
            sum = sum + i

    print("Oddlist sum : ",sum)



def main():
    Data = []
    print("Enter a number : ",end="")
    value = int(input())

    for i in range(value):
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