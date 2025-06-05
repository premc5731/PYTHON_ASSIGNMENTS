# 2.Design python application which creates two threads as evenfactor and  oddfactor. 
# Both the thread accept one parameter as integer. Evenfactor thread will display 
# addition of even factors of given number and oddfactor will display addition of odd 
# factors of given number. After execution of both the thread gets completed main thread should display message as “exit from main”.
import threading

def EvenFact(no):
    sum = 0
    for i in range(1,(no//2)+1):
        if((no % i == 0) and (i % 2 == 0)):
            sum = sum + i

    print("Even factors sum : ",sum)

def OddFact(no):
    sum = 0
    for i in range(1,(no//2)+1):
        if((no % i == 0) and (i % 2 != 0)):
            sum = sum + i

    print("Odd factors sum : ",sum)


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