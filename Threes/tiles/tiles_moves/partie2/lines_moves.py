import sys
sys.path.insert(0,"C:\\module_jeu_threes\\game\\play")
sys.path.insert(0,'C:\\module_jeu_threes\\ui\\play_display')


from tableau_al import tableau_al
from full_display import full_display
from line_move import line_move

a=tableau_al(2)



def lines_moves(plateau,sens):
    num_lig=0
    while num_lig<4:
        line_move(plateau,num_lig,sens)
        num_lig+=1
    return plateau
#full_display(a)
#full_display(lines_moves(a,0))
