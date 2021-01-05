import sys
sys.path.insert(0,"C:\\module_jeu_threes\\game\\play")
sys.path.insert(0,'C:\\module_jeu_threes\\ui\\play_display')


from tableau_al import tableau_al
from full_display import full_display

a=tableau_al(2)

def line_pack(plateau,num_lig,debut,sens):
    p=plateau['tiles']
    if sens==1:
           while debut <= 2:
                p[(debut)+(4*num_lig)]=p[(debut+1)+(4*num_lig)]
                p[debut+1+(4*num_lig)]=0
                debut+=1
    elif sens==0:
         while debut > 0:
                p[(debut)+(4*num_lig)]=p[(debut-1)+(4*num_lig)]
                p[debut-1+(4*num_lig)]=0
                debut-=1
    return plateau
#full_display(a)
#full_display(line_pack(a,3,3,0))
