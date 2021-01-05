from init_play import init_play
from is_game_over import is_game_over
from tableau_al import tableau_al

p=init_play()
p2=tableau_al()

def test_is_game_over():
    assert is_game_over(p)==False
    assert is_game_over(p2)==True
    print('ok')
test_is_game_over()
