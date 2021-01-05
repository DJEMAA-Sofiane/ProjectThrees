import sys
sys.path.insert(0,"C:\\module_jeu_threes")
from tiles.tiles_moves.get_nb_empty_rooms import get_nb_empty_rooms

from init_play import init_play

p=init_play()



def is_game_over(plateau):
    p=get_nb_empty_rooms(plateau)
    if p==0:
        return True
    return False
#print(is_game_over(p))
