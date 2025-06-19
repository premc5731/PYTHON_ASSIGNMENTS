for proc in psutil.process_iter(['name','pid','username']):
    #     print(proc.info)