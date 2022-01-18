import json
import base64
import os
import random

from .attendance import attendance_main

def login() -> int:
    uid = input("PLEASE ENTER YOUR UID (User ID): ")

    with open("assets\\users.json" , "r") as f:
        z = json.load(f)

    if uid not in z:
        print("Invalid User ID")
        return 1
    
    else:
        pwd = input("PLEASE ENTER YOUR PASSWORD: ")
        if str(base64.b64encode(pwd.encode('ascii'))) != z[uid]["password"]:
            print("Invalid Password")
        else:
            os.system('cls')
            print("Welcome {}".format(z[uid]["name"]))
            attendance_main()

        return [0 , uid]