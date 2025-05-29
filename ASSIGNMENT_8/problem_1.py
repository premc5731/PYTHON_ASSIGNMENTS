# 1.Design python application which creates two thread named as even and odd. Even
# thread will display first 10 even numbers and odd thread will display first 10 odd numbers. 

import threading


def Even():
    for i in range(1,11):
        if i % 2 == 0:
            print("Even number : ",i)


def Odd():
    for i in range(1,11):
        if i % 2 != 0:
            print("Odd number : ",i)

def main():
    print("In main ")
    T1 = threading.Thread(target = Even)
    T2 = threading.Thread(target = Odd)

    T1.start()
    T1.join()

    T2.start()
    T2.join()

if __name__ == "__main__":
    main()