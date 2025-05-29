# Q6. Celsius to Fahrenheit Converter
# Accept temperature in Celsius and convert it to Fahrenheit using the formula:
# F = (C × 9/5) + 32
# Expected Input:
# Enter temperature in Celsius: 25
# Expected Output:
# Temperature in Fahrenheit: 77.0°F

def CtoF(No):
    Faren = 0.0
    Faren = (No * 9/5) + 32

    return Faren

def main():
    Temp = 0.0
    Result = 0.0
    print("Enter Temperature in Celsius : ",end="")
    Temp = float(input())
    
    Result = CtoF(Temp)
    print("Temperature in Farenhit ",Result)

if __name__ == "__main__":
    main()