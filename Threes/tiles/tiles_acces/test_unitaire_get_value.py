from get_value import get_value

import sys
sys.path.insert(0,"C:\\module_jeu_threes")

from game.play.tableau_al import tableau_al
p=tableau_al()

def test_get_value():
    t=p["tiles"]
    assert get_value(p,0,0)==t[0]
    assert get_value(p,1,0)==t[4]
    assert get_value(p,2,0)==t[8]
    assert get_value(p,3,0)==t[12]
    assert get_value(p,4,0)=='erreur'
    print("ok")
test_get_value()
