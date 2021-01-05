import sys
sys.path.insert(0,"C:\\module_jeu_threes")

from game.play.init_play import init_play
p=init_play()

from check_room import check_room

def get_value(plateau,lig,col):
    c=check_room(plateau,lig,col)
    if c==False:
        return "erreur"
    p=plateau["tiles"]
    return p[col+(lig*4)]
   
#print(get_value(p,3,0))
