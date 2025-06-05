# Q6. Celsius to Fahrenheit Converter
# Accept temperature in Celsius and convert it to Fahrenheit using the formula:
# F = (C × 9/5) + 32
# Expected Input:
# Enter temperature in Celsius: 25
# Expected Output:
# temperature in Fahrenheit: 77.0°F

def CtoF(no):
    faren = 0.0
    faren = (no * 9/5) + 32

    return faren

def main():
    temp = 0.0
    result = 0.0
    print("Enter temperature in Celsius : ",end="")
    temp = float(input())
    
    result = CtoF(temp)
    print("temperature in farenhit ",result)

if __name__ == "__main__":
    main()