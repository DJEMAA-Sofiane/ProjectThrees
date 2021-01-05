import sys
sys.path.insert(0,"C:\\module_jeu_threes")
from game.play.init_play import init_play

sys.path.insert(0,"C:\\module_jeu_threes")
from game.play.tableau_al import tableau_al

from get_nb_empty_rooms import get_nb_empty_rooms 

p=init_play()
p2=tableau_al()

def test_get_nb_empty_rooms():
    assert get_nb_empty_rooms(p)==16 
    assert get_nb_empty_rooms(p2)==0
    print(p)
    print(p2)
    print('ok')
test_get_nb_empty_rooms()
