import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

path = "C:/Users/premc/Desktop/Folder"
parent = os.path.abspath(os.path.join(path, ".."))
print(parent)  # ➜ C:/Users/premc/Desktop

import LogModule as lm

obj = lm.Header()
obj.write("this is a test a function\n")
lm.Footer(obj)