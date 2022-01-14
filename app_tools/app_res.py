import json

def process_choice(choice) -> int:
    choice = choice.lower()
    CHOICES = ['h' , 's' , 't' , 'p' , 'l']

    if choice not in CHOICES or choice == 'h':
        return 0

    elif choice == 'p':
        try:
            uid = input("PLEASE ENTER A UID: ")
            with open("assets\\users.json" , "r") as f:
                data = json.load(f)

            to_p = f'''
NAME: {data[uid]["name"]}
ATTENDANCE: {data[uid]["attendance"]}
USER ID: {data[uid]["user_id"]}
            '''

            print(to_p)
        except:
            print("User with that uid not found")

        return 0

    elif choice == 'l':
        return 1

    elif choice == 's':
        print("COMING SOON")
        return 0

    elif choice == 't':

        some_random_var = '''
[C] How to Make chocolate
[B] Go back
        '''

        print(some_random_var)

        return train()

def train() -> int:
    x = input("PLEASE ENTER YOUR CHOICE: ").lower()

    if x == 'b':
        return 0

    if x == 'c':
        chocolate = '''
        
Please add the recipe here
~ Atidipt
        
        '''
        print(chocolate)

        return 0

    else:
        return 0