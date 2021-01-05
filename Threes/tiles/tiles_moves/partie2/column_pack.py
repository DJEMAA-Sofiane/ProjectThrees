import sys
sys.path.insert(0,"C:\\module_jeu_threes\\game\\play")
sys.path.insert(0,'C:\\module_jeu_threes\\ui\\play_display')


from tableau_al import tableau_al
from full_display import full_display

a=tableau_al(2)

def column_pack(plateau,num_col,debut,sens):
    p=plateau['tiles']
    if sens==1:
        while debut < 3:
            p[(debut*4)+(num_col)]=p[(debut*4+4)+(num_col)]
            p[(debut*4+4)+(num_col)]=0
            debut+=1    
    elif sens==0:
        while debut > 0:
            p[(debut*4)+(num_col)]=p[(debut*4-4)+(num_col)]
            p[(debut*4-4)+(num_col)]=0
            debut-=1
    return plateau
#full_display(a)
#full_display(column_pack(a,0,0,1))   
