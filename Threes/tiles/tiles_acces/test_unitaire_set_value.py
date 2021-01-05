from set_value import set_value
from get_value import get_value
import sys
sys.path.insert(0,"C:\\module_jeu_threes")

from game.play.init_play import init_play
p=init_play()

def test_set_value():
    set_value(p,0,0,1)
    set_value(p,1,0,2)
    set_value(p,2,0,3)
    set_value(p,3,0,4)
    assert get_value(p,0,0)==1
    assert get_value(p,1,0)==2
    assert get_value(p,2,0)==3
    assert get_value(p,3,0)==4
    assert set_value(p,4,0,0)=='erreur'
    print(p)
test_set_value()
