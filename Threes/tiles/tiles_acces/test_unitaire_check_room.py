from check_room import check_room

import sys
sys.path.insert(0,"C:\\module_jeu_threes")

from game.play.init_play import init_play
p=init_play()
def test_check_room():
    assert check_room(p,4,0)==False
    assert check_room(p,2,6)==False
    assert check_room(p,3,0)==True
    print("ok")
test_check_room()
