import sys

sys.path.insert(0,"C:\\module_jeu_threes\\game\\play\\partie3")
sys.path.insert(0,"C:\\module_jeu_threes\\tiles\\tiles_moves\\partie2")
sys.path.insert(0,"C:\\module_jeu_threes\\ui\\play_display")
sys.path.insert(0,"C:\\module_jeu_threes\\ui\\user_entries")
sys.path.insert(0,"C:\\module_jeu_threes\\tiles\\tiles_moves\\partie2")
sys.path.insert(0,"C:\\module_jeu_threes\\game\\play")
sys.path.insert(0,"C:\\module_jeu_threes\\tiles\\tiles_acces")

from get_score import get_score
from play_move import play_move
from get_user_move import get_user_move
from full_display import full_display
from create_new_game import create_new_game
from put_next_tiles import put_next_tiles
from get_next_aléa_tiles import get_next_aléa_tiles
from room_empty import room_empty
from set_value import set_value

d=create_new_game()


def cycle_play(partie):
    p=partie['plateau']
    i=0
    while i > -1 :
        full_display(p)
        tile=partie['next_tile']
        if tile==None:
            tile=get_next_aléa_tiles(p,'encours')
        
        if tile['check']==False:
            partie['score']=get_score(p)
            print('score final:',partie['score'])
            return True
        
        val=tile['0']
        print(val['val'])
        sens=get_user_move()
        if sens=='m':
            return False
               
        play_move(p,sens)
        
        if room_empty(p,val['lig'],val['col'])==False:
            tile2=get_next_aléa_tiles(p,'encours')        
            val2=tile2['0']
            set_value(p,val2['lig'],val2['col'],val['val'])
        
        else:
            put_next_tiles(p,tile)
        partie['next_tile']=get_next_aléa_tiles(p,'encours')
        i+=1
#print(cycle_play(d))
