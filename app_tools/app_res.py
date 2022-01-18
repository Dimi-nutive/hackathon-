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
Ingredients
2 cup cocoa powder
1/2 cup sugar
1/4 teaspoon flour
3/4 cup butter
2/3 cup milk
1 cup Water

Recipe

1. Mix the ingredients
2. Whisk the chocolate paste
3. Make sure there are no lumps
4. Pour the mixture in the moulds and refrigerate
'''
        print(chocolate)

        return 0

    else:
        return 0
