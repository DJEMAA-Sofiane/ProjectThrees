import sys
sys.path.insert(0,"C:\\module_jeu_threes")

from game.play.init_play import init_play
p=init_play()
def check_room(plateau,lig,col):
    p=plateau["n"]
    if lig>p-1 or lig<0:
        return False
    elif col>p-1 or col<0:
        return False
    return True

#check_room(p,4,0)
