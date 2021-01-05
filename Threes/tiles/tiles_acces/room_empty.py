import sys
sys.path.insert(0,"C:\\module_jeu_threes")
from game.play.init_play import init_play

from get_value import get_value

p=init_play()
def room_empty(plateau,lig,col):
    p=get_value(plateau,lig,col)
    if p=='erreur':
        return 'erreur'
    if p==0:
        return True 
    return False
#print(room_empty(p,0,0))
