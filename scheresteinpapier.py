import random as rd # random will be imported

""" This following Pythoncode is the game: Rock paper scissors """

def game(): # game definition
    
    """ The following part take the userinput 
    and the computerchoice"""
    
    user = int(input('Schere(1), Stein(2), Papier(3), Beenden(4)? :' ,)) # user choice input
    computer = rd.choice(['Schere', 'Stein', 'Papier']) # computers random choice

    print(f'Spieler hat {user} eingetippt \n')

    if user == 1:
        print('Spieler: Schere')
    elif user == 2:
        print('Spieler: Stein')
    elif user == 3:
        print('Spieler: Papier')
    elif user == 4:
        sicher = input('Sind sie sich sicher (y) zum bestätigen sonstiges um abbzubrechen? ' ,)
        exit() if sicher == 'y' else game()
    else:
        print('Falsche Eingabe \n')
        game()

    print('Computer: ', computer)

    if user == computer:
        print('Unentschieden \n')
    elif user == 1 and computer == 'Stein':
        print('Computer hat gewonnen \n')
    elif user == 2 and computer == 'Papier':
        print('Computer hat gewonnen \n')
    elif user == 3 and computer == 'Schere':
        print('Computer hat gewonnen \n')
    elif user == 1 and computer == 'Schere':
        print ('unentschieden')
    elif user == 2 and computer == 'Stein':
        print ('unentschieden')
    elif user == 3 and computer == 'Papier':
        print ('unentschieden')
    else:
        print('Du hast gewonnen \n')

def restarting(): # restarting
    
    """ The following part ask the player 
    for restarting the game"""
    
    restart = input('Noch einmal? (y/n) :')

    if restart == 'y':
        main()
    elif restart == 'n':
        print('Auf Wiedersehen')
        exit()
    else:
        print('Falsche Eingabe!')
        restarting()
    restart = input('Noch einmal? (y/n) :')   

def main():
    
    """ This part defines main which is necessary 
    to start the game first and after the game
    is finished the player can choose to restart or to exit"""
    
    game()
    restarting()

if __name__ == '__main__':
    main()
