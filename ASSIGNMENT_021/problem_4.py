# 4. Design automation script which accept directory name and mail id from user and create log
# file in that directory which contains information of running processes as its name, PID,
# Username. After creating log file send that log file to the specified mail.
# Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com
# Demo is name of Directory.
# marvellousinfosystem@gmail.com is the mail id.


import psutil
import sys
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def SendMail(log_filename):

    print("Sending email...")
    
    from_address = "ajay194703@gmail.com"
    to_address = sys.argv[2]
    password = "lcomjjnktdfuyiqi"
    
    msg = MIMEMultipart()

    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = "Delete Duplicate Files Log-file"

    body = "This is a log file of python script scheduled to delete duplicate files"

    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent 
    filename = os.path.basename(log_filename)
    attachment = open(log_filename, "rb")

    # instance of MIMEBase
    mimebase_obj = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    mimebase_obj.set_payload((attachment).read())
    encoders.encode_base64(mimebase_obj)
    
    mimebase_obj.add_header('Content-Disposition', "attachment; filename= %s" %(filename))

    msg.attach(mimebase_obj)

    server_connection = smtplib.SMTP('smtp.gmail.com', 587)
    server_connection.starttls()
    server_connection.login(from_address, password)
    text = msg.as_string()
    server_connection.sendmail(from_address, to_address, text)
    server_connection.quit()

    print("Email sent successfully")

def CreateLog(Data):
    dirname = sys.argv[1]
    flag = os.path.isabs(dirname)

    if flag == False:
        dirname = os.path.abspath(dirname)

    flag = os.path.exists(dirname)

    if flag == False:
        print("Invalid directory name")
        exit()

    flag = os.path.isdir(dirname)

    if flag == False:
        print("Given name is not directory")
        exit()

    timestamp = time.ctime()
    filename = "Running_Porcesses_Log %s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")
    filename = filename.replace("__","_")

    filename = os.path.join(dirname,filename)

    fobj = open(filename, "w")

    border = "-"*80
    fobj.write(border+"\n")
    fobj.write("This is a log file of running processes on machine created using automation script\n")
    fobj.write(border+"\n")

    for value in Data:
        fobj.write(value)
        fobj.write("\n")

    
    fobj.write(border+"\n")
    fobj.write("Total running processes are : %s \n"%(len(Data)))
    fobj.write("This file is created at\n"+timestamp+"\n")
    fobj.write(border+"\n")

    fobj.close()

    SendMail(filename)

def RunningProcesses():
    info_list = []
    for proc in psutil.process_iter(['name','pid','username']):#less system calls
        info_list.append(str(proc.info))

    CreateLog(info_list)
         

def main():

    if(len(sys.argv) == 1):
        print("Use the given flags as : ")
        print("--h is used to display the help")
        print("--u is used to display the usage")

    elif (len(sys.argv) == 2):
        if(sys.argv[1] == '--h' or sys.argv[1] == '--H'):
            print("This application is used to create a log of running processes and mail that file log file to receivers maild id")
        elif(sys.argv[1] == '--u' or sys.argv[1] == '--U'):
            print("Use the given script as ")
            print("Scriptname.py directory receiver'smailid")
        else:
            print("Use the given flags as : ")
            print("--h is used to display the help")
            print("--u is used to display the usage")

    elif(len(sys.argv) == 3):
            RunningProcesses()

if __name__ == "__main__":
    main()