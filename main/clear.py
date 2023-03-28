import os
import platform

def clear():
    if platform.system() == "Linux": 
        os.system("clear")
    elif platform.system() == "Windows":
        os.system("cls")
    else:
        None