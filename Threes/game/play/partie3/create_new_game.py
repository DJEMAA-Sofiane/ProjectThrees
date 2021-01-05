import sys
sys.path.insert(0,"C:\\module_jeu_threes\\tiles\\tiles_moves")
sys.path.insert(0,"C:\\module_jeu_threes\\game\\play")
sys.path.insert(0,"C:\\module_jeu_threes\\tiles\\tiles_moves\\partie2")

from init_play import init_play
from get_score import get_score
from get_nb_empty_rooms import get_nb_empty_rooms
from put_next_tiles import put_next_tiles
from get_next_aléa_tiles import get_next_aléa_tiles

def create_new_game():
    p=init_play()
    put_next_tiles(p,get_next_aléa_tiles(p,'init'))
    d={'plateau':p,'next_tile':None ,'score':get_score(p)}
    get_nb_empty_rooms(d['plateau'])
    return d
d=create_new_game()
print(d)
