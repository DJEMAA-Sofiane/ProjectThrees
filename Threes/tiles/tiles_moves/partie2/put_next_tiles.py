import sys

sys.path.insert(0,"C:\\module_jeu_threes\\game\\play")
sys.path.insert(0,"C:\\module_jeu_threes\\tiles\\tiles_acces")
sys.path.insert(0,'C:\\module_jeu_threes\\ui\\play_display')

from init_play import init_play
from full_display import full_display
from set_value import set_value
from get_next_aléa_tiles import get_next_aléa_tiles

d=init_play()

def put_next_tiles(plateau,tiles):
    if tiles['check']==True:
        if tiles['mode']=='init':
            d0=tiles['0']
            d1=tiles['1']
            set_value(plateau,d0['lig'],d0['col'],d0['val'])
            set_value(plateau,d1['lig'],d1['col'],d1['val'])
        elif tiles['mode']=='encours':
            d0=tiles['0']
            set_value(plateau,d0['lig'],d0['col'],d0['val'])
        return plateau
    elif tiles['check']==False:
        return False

            

#put_next_tiles(d,get_next_aléa_tiles(d,'init'))    
#full_display(d)    
