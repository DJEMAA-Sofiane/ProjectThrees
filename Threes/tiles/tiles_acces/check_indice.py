import sys
sys.path.insert(0,"C:\\module_jeu_threes")

from game.play.init_play import init_play

p=init_play()
def check_indice(plateau,indice):
    p=plateau["n"]
    if p-1<indice or indice<0:
        return False
    return True
#check_indice(p,5)
