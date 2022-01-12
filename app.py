from constants import PLAYERS,TEAMS

def menu():
    print('-_-_- Menu -_-_-\n')
    print('\nA) Display Team Stats')
    print('B) Quit\n')
    
    opt= input('Enter an option: ').upper()
    

    return opt

game = True
choice = menu()
while game:
    if choice == 'B':
        game = False
        print('Thank You')
    
    


def clean_data():
    pass
    


menu()