import sys
sys.path.insert(0,"C:\\module_jeu_threes\\game\\play")
sys.path.insert(0,"C:\\module_jeu_threes\\tiles\\tiles_acces")
from init_play import init_play
from is_game_over import is_game_over
from room_empty import room_empty
from random import*
p=init_play()


def get_next_aléa_tiles(plateau,mode):
    d={}
    if mode=='init':
        d['mode']='init'
        d['0']={'val':2, 'lig':randint(0,3), 'col':randint(0,3)}
        lig=randint(0,3)
        col=randint(0,3)
        d0=d['0']
        while lig==d0['lig'] and col==d0['col']:
            lig=randint(0,3)
            col=randint(0,3)
        d['1']={'val':1, 'lig':lig, 'col':col}
        d['check']=True
    elif mode=='encours':
        d['mode']='encours'
        if is_game_over(plateau)==True :
            d['check']=False
        else:
            lig=randint(0,3)
            col=randint(0,3)
            while room_empty(plateau,lig,col)==False:
                lig=randint(0,3)
                col=randint(0,3)
            d['0']={'val':randint(1,3), 'lig':lig, 'col':col}
            d['check']=True
    return d
#print(get_next_aléa_tiles(p,'encours'))     
