import app_tools as at
import os

os.system("@echo off")
os.system("cls")

print(at.INTRO_TEXT)

def signin():
    print('[L] - Login')
    x = input("Welcome!\nPlease enter 'l' to login: ").lower()

    return x

signin_ = signin()

if signin_ != 'l':
    print("Thats an invalid choice please try again by running the application again")
else:
    e = at.login()
        
    if e[0] == 0:
        while True:
            print(at.MENU_UI)
            choice = input("PLEASE ENTER WHAT YOU WANT TO DO: ")
            response = at.process_choice(choice)

            if response == 1:
                exit()