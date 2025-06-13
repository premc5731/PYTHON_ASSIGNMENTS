import time

timestamp = time.ctime()
def Header():
    
    # timestamp = time.ctime()

    filename = "MarvellousLog %s.log" %(timestamp)
    filename = filename.replace(" ","_")
    filename = filename.replace(":","_")
    filename = filename.replace("__","_")

    fobj = open(filename,"w")

    Border = "-"*44
    fobj.write(Border+"\n")
    fobj.write("This is a log file of marvellous automation script\n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n")
    return fobj

def Footer(fobj):
    Border = "-"*44

    fobj.write(Border+"\n")
    fobj.write("This file is created at\n"+timestamp+"\n")
    fobj.write(Border+"\n")

# to import this module we have a different approach in assignment_19 in log_test.py file
