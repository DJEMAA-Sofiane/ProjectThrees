import sys

sys.path.insert(0,"C:\\module_jeu_threes\\game\\play\\partie3")

from create_new_game import create_new_game

d=create_new_game()

def get_user_menu(partie):
    x=''
    if partie==None:
         while x!="N" and x!="L":
            print("Commencer une nouvelle partie:-N ")
            print("Charger une partie:-L")
            x=input()
            x=x.upper()
    elif partie!=None:
        while x!="S" and x!="C" and x!="Q":
            print("Sauvegarder la partie en cours:-S ")            
            print("Reprendre la partie en cours:-C ")
            print("Terminer le jeu:-Q ")
            x=input()
            x=x.upper()
    return x
#print(get_user_menu(None))
#print(get_user_menu(d))
