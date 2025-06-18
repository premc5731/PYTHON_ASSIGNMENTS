# Q7. Area and Perimeter of Rectangle
# Accept the length and width of a rectangle. Calculate and display the area and perimeter.
# Expected Input:
# Enter length: 5
# Enter width: 3
# Expected Output:
# Area: 15
# Perimeter: 16

def Area(len, wid):
    result = 0
    result = len * wid

    return result

def Perimeter(len, wid):
    result = 0
    result = 2 * (len + wid)

    return result

def main():
    length = 0
    width = 0
    ret = 0

    print("Enter length : ",end="")
    length = int(input())

    print("Enter width : ",end="")
    width = int(input())

    ret = Area(length,width)
    print("Area is : ",ret)

    ret = Perimeter(length,width)
    print("Perimeter is : ",ret)

    
if __name__ == "__main__":
    main()