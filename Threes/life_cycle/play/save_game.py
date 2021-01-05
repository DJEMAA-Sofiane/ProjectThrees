import json
import sys

sys.path.insert(0,"C:\\module_jeu_threes\\game\\play")
sys.path.insert(0,"C:\\module_jeu_threes\\game\\play\\partie3")

from get_score import get_score
from create_new_game import create_new_game

p=create_new_game()

def save_game(partie):
    p=partie
    score=get_score(p['plateau'])
    p['score']=score
    with open("C:\module_jeu_threes\life_cycle\play\saved_game.json",'w', encoding='utf-8') as wf:
        json.dump(p,wf)

#save_game(p)
