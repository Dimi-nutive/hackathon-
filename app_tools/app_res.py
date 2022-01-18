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
        return sales()

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
<<<<<<< HEAD
        
=======
>>>>>>> e3521f2a99f0ae64560aaabcc30786d9e5d0c4cf
Ingredients
2 cup cocoa powder
1/2 cup sugar
1/4 teaspoon flour
3/4 cup butter
2/3 cup milk
1 cup Water
<<<<<<< HEAD
Recipe
=======

Recipe

>>>>>>> e3521f2a99f0ae64560aaabcc30786d9e5d0c4cf
1. Mix the ingredients
2. Whisk the chocolate paste
3. Make sure there are no lumps
4. Pour the mixture in the moulds and refrigerate
<<<<<<< HEAD
        '''
=======
'''
>>>>>>> e3521f2a99f0ae64560aaabcc30786d9e5d0c4cf
        print(chocolate)

        return 0

    else:
        return 0
<<<<<<< HEAD

def sales():
    with open("assets\\sales_data.json" , "r") as f:
        d = json.load(f)

    sales_menu= '''
[C] - Choco Truffle Sales Info
[B] - Brown Bar Sales Info
[W] - White Bubble Sales Info
[H] - Hazzle Drops Sales Info
[D] - Caramel Blast Info

Please Enter Menu Key: 
    '''

    c = input(sales_menu)
    if c.lower() not in d:
        print("Not a valid choice")
        return 0
    else:
        cost = d[c]['production-cost']
        mrp = d[c]['market-price']
        produced = d[c]['produced']
        sold = d[c]['sold']
        tpc = produced*cost #total production cost
        tsp = sold*mrp #total sold price
        
        if tpc > tsp:
            state = "loss"
            pl = tpc-tsp
        elif tsp > tpc:
            state = "profit"
            pl = tsp-tpc
        else:
            state = "neutral"
            pl = 0

        result = f'''
Name: {d[c]['name']}
Produced this month: {produced}
Sold this month: {sold}
Loss/Profit: {state} of Rs. {round(pl)}        
1 Chocolate Production Cost: Rs. {cost}
MRP: Rs. {mrp}
'''

        print(result)
        return 0
=======
>>>>>>> e3521f2a99f0ae64560aaabcc30786d9e5d0c4cf
