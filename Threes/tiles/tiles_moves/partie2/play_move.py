import sys
sys.path.insert(0,"C:\\module_jeu_threes\\game\\play")
sys.path.insert(0,'C:\\module_jeu_threes\\ui\\play_display')


from tableau_al import tableau_al
from full_display import full_display
from columns_moves import columns_moves
from lines_moves import lines_moves

a=tableau_al(2)


def play_move(plateau,sens):
    if sens=='h':
        sens=1
        columns_moves(plateau,sens)
    elif sens=='b':
        sens=0
        columns_moves(plateau,sens)
    elif sens=='g':
        sens=1
        lines_moves(plateau,sens)
    elif sens=='d':
        sens=0
        lines_moves(plateau,sens)
    return plateau

#full_display(a)
#full_display(play_move(a,'d'))
