# 3. Write a Python script to count the number of lines, words, and characters in a
# given file.


import sys
import os
        
def Count(file_name):

    flag = os.path.exists(file_name)

    if(flag == False):
        print("Invalid file name")
        exit()
    
    fobj = open(file_name,"r")
    Buffer = fobj.read()
    
    lines_count = 0
    words_count = 0
    char_count = 0

    Buffer = Buffer.split("\n")
    for line in Buffer:
        lines_count += 1

        line_buffer = line.split()

        for word in line_buffer:
            if(len(word) > 1):
                words_count += 1

            for letter in word:
                char_count += 1

    return lines_count, words_count, char_count



def main():

    if(len(sys.argv) == 1):
        print("Use the given flags as : ")
        print("--h is used to display the help")
        print("--u is used to display the usage")

    elif (len(sys.argv) == 2):
        if(sys.argv[1] == '--h' or sys.argv[1] == '--H'):
            print("This application is used to count the number of lines, words, and characters in a file")
        elif(sys.argv[1] == '--u' or sys.argv[1] == '--U'):
            print("Use the given script as ")
            print("Scriptname.py file_name")
        else:
            no_lines, no_words, no_char =Count(sys.argv[1])
            print("Number of lines : ",no_lines)
            print("Number of words : ",no_words)
            print("Number of character : ",no_char)
    
if __name__ == "__main__":
    main()