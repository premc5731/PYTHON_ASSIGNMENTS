# 4.Design python application which creates three threads as small,
#  capital, digits. All the threads accepts string as parameter. Small thread display number of small 
# characters, capital thread display number of capital characters and digits thread display number of 
# digits. Display id and name of each thread. 

import threading


def SumSmall(data):
    sum = 0
    for c in data:
        if c.islower():
            sum += 1
    print("")
    print("Number of small characters : ",sum)

def SumCap(data):
    sum = 0
    for c in data:
        if c.isupper():
            sum += 1
    print("")
    print("Number of capital characters : ",sum)

def SumDig(data):
    sum = 0
    for c in data:
        if c.isdigit():
            sum += 1
    print("")
    print("Number of digits characters : ",sum)

def main():
    data = []
    print("Enter a String : ",end="")
    istr = input()

    T1 = threading.Thread(target = SumSmall,args = (istr,))
    T2 = threading.Thread(target = SumCap,args = (istr,))
    T3 = threading.Thread(target = SumDig,args = (istr,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("end of main")

if __name__ == "__main__":
    main()
