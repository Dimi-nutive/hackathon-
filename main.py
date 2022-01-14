import app_tools as at
import os

os.system("@echo off")
os.system("cls")

print(at.INTRO_TEXT)

def signin():
    print('[R] - Register\n[L] - Login')
    x = input("Welcome!\nPlease Choose if you want to register or login: ").lower()

    return x

signin_ = signin()

if signin_ != 'r' and signin_ != 'l':
    print("Thats an invalid choice please try again by running the application again")

else:
    if signin_ == 'r':
        at.register()
    else:
        at.login()
        print(at.MENU_UI)