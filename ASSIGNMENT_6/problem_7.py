# Q7. Accept 5 numbers from the user. Find and print the largest number.
# Expected Input:
# Enter 5 numbers: 23 89 12 56 45
# Expected Output:
# maximum number is: 89

def Largest(Data):
    max = Data[0]

    for i in range(1,5):
        if Data[i] > max:
            max = Data[i]
    
    return max


def main():
    IData = []
    print("Enter 5 numbers :")

    for i in range(5):
        IData.append(int(input()))

    ret = Largest(IData)

    print("Largest number is : ",ret)
    
if __name__ == "__main__":
    main()