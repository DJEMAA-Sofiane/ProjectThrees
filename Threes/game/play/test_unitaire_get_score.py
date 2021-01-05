from init_play import init_play

from get_score import get_score

import sys
sys.path.insert(0,"C:\\module_jeu_threes\\tiles\\tiles_acces")
from set_value import  set_value
from check_room import check_room 
 

p=init_play()

def test_get_score():
    set_value(p,0,0,1)
    set_value(p,1,0,2)
    set_value(p,2,0,3)
    set_value(p,3,0,4)
    assert get_score(p)==10
    print('ok')
test_get_score()
