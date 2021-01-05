from check_room import check_room
import sys
sys.path.insert(0,"C:\\module_jeu_threes")

from game.play.init_play import init_play
p=init_play()

def set_value(plateau,lig,col,val):
    c=check_room(plateau,lig,col)
    if c==False:
        return 'erreur'
    p=plateau["tiles"]
    p[col+(lig*4)]=val
    return plateau
#p=set_value(p,3,3,2)
#print(p)
