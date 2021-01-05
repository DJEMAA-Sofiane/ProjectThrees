import sys

sys.path.insert(0,"C:\\module_jeu_threes\\game\\play\\partie3")
sys.path.insert(0,"C:\\module_jeu_threes\\game\\play")
sys.path.insert(0,"C:\\module_jeu_threes\\ui\\user_entries")
sys.path.insert(0,"C:\module_jeu_threes\life_cycle\play")

from get_score import get_score
from create_new_game import create_new_game
from put_next_tiles import put_next_tiles
from get_next_aléa_tiles import get_next_aléa_tiles
from get_user_menu import get_user_menu
from cycle_play import cycle_play
from save_game import save_game
from restore_game import restore_game


def threes():
    partie=None
    menu=get_user_menu(partie)
    if menu=='N':
        partie=create_new_game()
    elif menu=='L':
        partie=restore_game()
    jeu=False
    while jeu==False:
        jeu=cycle_play(partie)
        
        if jeu == False:
            menu=get_user_menu(partie)
            if menu=='S':
                save_game(partie)
                return 'Partie sauvegarder'
            elif menu=='Q':
                save_game(create_new_game())
                return 'fin du jeu'
        
        elif jeu == True:
            save_game(create_new_game())
            x=''
            while x!='o'and  x!='n':
                print('rejouer o/n')
                x=input()
                x=x.lower()
            if x=='o':
                jeu=False
                partie=create_new_game()
            else:
                return 'fin du jeu'
print(threes())          
