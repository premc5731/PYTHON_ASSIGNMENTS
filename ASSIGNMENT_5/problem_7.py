# Q7. Area and Perimeter of Rectangle
# Accept the length and width of a rectangle. Calculate and display the area and perimeter.
# Expected Input:
# Enter length: 5
# Enter width: 3
# Expected Output:
# Area: 15
# Perimeter: 16

def Area(len, wid):
    Result = 0
    Result = len * wid

    return Result

def Perimeter(len, wid):
    Result = 0
    Result = 2 * (len + wid)

    return Result

def main():
    Length = 0
    Width = 0
    Ret = 0

    print("Enter Length : ",end="")
    Length = int(input())

    print("Enter Width : ",end="")
    Width = int(input())

    Ret = Area(Length,Width)
    print("Area is : ",Ret)

    Ret = Perimeter(Length,Width)
    print("Perimeter is : ",Ret)

    
if __name__ == "__main__":
    main()