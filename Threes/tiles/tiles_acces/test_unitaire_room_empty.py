import sys
sys.path.insert(0,"C:\\module_jeu_threes")
from game.play.init_play import init_play

from set_value import set_value
from room_empty import room_empty

p=init_play()

def test_room_empty():
    set_value(p,0,0,1)
    set_value(p,1,0,2)
    set_value(p,2,0,3)
    set_value(p,3,0,4)
    assert room_empty(p,0,0)==False
    assert room_empty(p,0,1)==True
    assert room_empty(p,2,0)==False
    assert room_empty(p,4,0)=='erreur'
    print('ok')
test_room_empty()
