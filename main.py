import random

def roll():
    rollResult = random.randint(1, 6)
    if rollResult == 1:
        print('''
░░███╗░░
░████║░░
██╔██║░░
╚═╝██║░░
███████╗
╚══════╝''')
    elif rollResult == 2:
        print('''
██████╗░
╚════██╗
░░███╔═╝
██╔══╝░░
███████╗
╚══════╝''')
    elif rollResult == 3:
        print('''
██████╗░
╚════██╗
░█████╔╝
░╚═══██╗
██████╔╝
╚═════╝░''')
    elif rollResult == 4:
        print('''
░░██╗██╗
░██╔╝██║
██╔╝░██║
███████║
╚════██║
░░░░░╚═╝''')
    elif rollResult == 5:
        print('''
███████╗
██╔════╝
██████╗░
╚════██╗
██████╔╝
╚═════╝░''')
    else:
        print('''
░█████╗░
██╔═══╝░
██████╗░
██╔══██╗
╚█████╔╝
░╚════╝░''')

while True:
    print("Hello Do you want to roll a dice")
    choice = input("Y/N: ")
    if choice.lower() == 'y':
        roll()

    elif choice.lower() == 'n':
        break

    else:
        print("Error")