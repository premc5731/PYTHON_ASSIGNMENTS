# 10. Write a program which accept name from user and display length of its name.
# Input : Marvellous Output : 10

def DisplayLen(name):
    print(len(name))
    
def main():
    print("Enter your name : ",end ="")
    Name = input()
    DisplayLen(Name)

if __name__ == "__main__":
    main()