import json
import base64
import os

def register() -> int:
    name = input("ENTER YOUR NAME: ")

    while True:
        pwd = input("ENTER A PASSWORD: ")
        if len(pwd) < 8:
            print("Password must be 8 characters long")
        else:
            break

    with open("assets\\users.json" , "r") as f:
        x = json.load(f)

    x[str(len(x)+1)] = {}
    x[str(len(x))]["name"] = name
    x[str(len(x))]["password"] = str(base64.b64encode(pwd.encode('ascii')))
    x[str(len(x))]["user_id"] = str(len(x))
    x[str(len(x))]["attendance"] = 0

    USER_ID = str(len(x))

    with open("assets\\users.json" , "w") as f_2:
        json.dump(x , f_2)

    print("Succesfully Registered!\nYour USER ID is {}".format(USER_ID))

    return 0

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

        return 0