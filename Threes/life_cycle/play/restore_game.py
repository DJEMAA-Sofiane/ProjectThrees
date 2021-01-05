import json


def restore_game():
    with open("C:\module_jeu_threes\life_cycle\play\saved_game.json",'r', encoding='utf-8') as rf:
        save= json.load(rf)
        return save
#p=restore_game()
#print(p)
