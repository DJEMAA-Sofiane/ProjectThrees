from init_play from init_play

p=init_play()

def test_get_score():
    set_value(p,0,0,1)
    set_value(p,1,0,2)
    set_value(p,2,0,3)
    set_value(p,3,0,4)
    assert get_score(p)==10
    print('ok')
test_get_score()
