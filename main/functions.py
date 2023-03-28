import time
import constants as cts
from main import *

def help():
    print(cts.JUMP_LINE)
    time.sleep(0.1)
    print(cts.HELP)
    time.sleep(0.1)
    print(cts.INFO_HELP)
    inp = input(cts.INP_SHOW_DATA)
    if inp.isupper():
        inp = inp.lower()
    if inp == 'y':
        print(cts.JUMP_LINE)
        time.sleep(0.1)
        print(cts.LOADING_DATA)
        print(cts.JUMP_LINE)
        user = cts.User()
        user.print_xlsx()
        time.sleep(0.1)
        print(cts.JUMP_LINE)
        print(cts.LOAD_DATA)
        time.sleep(0.1)
        print(cts.JUMP_LINE, cts.CHECK_XLSX)
        time.sleep(0.1)
    elif inp == 'n':
        time.sleep(0.1)
    else:
        error()

def return_menu():
    inp = input(cts.QUESTION_RET)
    if inp.isupper():
        inp = inp.lower()
    if inp == 'y':
        print(cts.JUMP_LINE)
        time.sleep(0.1)
        print(cts.RETURN_MENU)
        time.sleep(0.1)
    elif inp == 'n':
        exit_program()
        exit()
    else:
        error()

def exit_program():
    print(cts.JUMP_LINE)
    time.sleep(0.1)
    print(cts.EXIT)
    time.sleep(0.1)

def error():
    print(cts.JUMP_LINE)
    print(cts.ERR)
    time.sleep(0.1)
    print(cts.JUMP_LINE)
    print(cts.RETURN_MENU)
    time.sleep(0.1)