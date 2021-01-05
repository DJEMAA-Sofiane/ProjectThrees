import sys
sys.path.insert(0,"C:\\module_jeu_threes\\game\\play")
sys.path.insert(0,'C:\\module_jeu_threes\\ui\\play_display')


from tableau_al import tableau_al
from full_display import full_display
from column_move import column_move

a=tableau_al(2)


def columns_moves(plateau,sens):
    num_col=0
    while num_col<4:
        column_move(plateau,num_col,sens)
        num_col+=1
    return plateau

#full_display(a)
#full_display(columns_moves(a,1))
