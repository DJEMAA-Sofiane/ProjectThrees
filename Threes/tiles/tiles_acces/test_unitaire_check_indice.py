from check_indice import check_indice
import sys
sys.path.insert(0,"C:\\module_jeu_threes")

from game.play.init_play import init_play


p=init_play()

def test_check_indice():
    assert check_indice(p,4)==False
    assert check_indice(p,-1)==False
    assert check_indice(p,3)==True
    print("ok")
test_check_indice()
