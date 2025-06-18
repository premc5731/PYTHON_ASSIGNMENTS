# 7. Print Pattern Using Recursion (Right Triangle)
# Write a recursive function to print the following pattern:
# *
# * *
# * * *
# * * * *


iCcnt = 1
iRcnt = 1

def Display(iRow,iCol):
    if iRow != iCol:
        print("Invalid input : ")
        return
    
    global iRcnt, iCcnt

    # while(iRcnt <= iRow):
    #     iCcnt = 1
    #     while(iCcnt <= iCol):
    #         if iRcnt >= iCcnt:
    #             print("*",end = "")
    #         iCcnt +=1
    #     iRcnt += 1
    #     print()

    if(iRcnt <= iRow):
        if(iCcnt <= iCol):
            if iRcnt >= iCcnt:
                print("*",end = "")
            iCcnt +=1
            Display(iRow, iCol)
        if(iRcnt < iRow+1):
            print()
            iRcnt += 1
            iCcnt = 1
            Display(iRow, iCol)

def main():
    Display(4,4)

if __name__ == "__main__":
    main()