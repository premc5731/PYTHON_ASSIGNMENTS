# Q6. Print Triangle Pattern using Nested Loops
# Expected Output:
# *
# * *
# * * *
# * * * *
def Display():
    for i in range(1,5):
        for j in range(1,5):
            if i >= j:
                print("*\t",end="")

        print("")



def main():
    Display()
    

if __name__ == "__main__":
    main()