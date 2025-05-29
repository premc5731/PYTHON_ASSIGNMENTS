# 2.Design python application which creates two threads as evenfactor and  oddfactor. 
# Both the thread accept one parameter as integer. Evenfactor thread will display 
# addition of even factors of given number and oddfactor will display addition of odd 
# factors of given number. After execution of both the thread gets completed main thread should display message as “exit from main”.
import threading

def EvenFact(No):
    Sum = 0
    for i in range(1,(No//2)+1):
        if((No % i == 0) and (i % 2 == 0)):
            Sum = Sum + i

    print("Even factors Sum : ",Sum)

def OddFact(No):
    Sum = 0
    for i in range(1,(No//2)+1):
        if((No % i == 0) and (i % 2 != 0)):
            Sum = Sum + i

    print("Odd factors Sum : ",Sum)


def main():
    print("start of main ")
    T1 = threading.Thread(target = EvenFact,args = (12,))
    T2 = threading.Thread(target = OddFact,args = (12,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("end of main")

if __name__ == "__main__":
    main()