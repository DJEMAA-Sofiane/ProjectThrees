import sys
sys.path.insert(0,"C:\\module_jeu_threes\\game\\play")
sys.path.insert(0,'C:\\module_jeu_threes\\ui\\play_display')


from tableau_al import tableau_al
from full_display import full_display
from line_pack import line_pack

a=tableau_al(2)

def line_move(plateau,num_lig,sens):
    p=plateau['tiles']
    if sens==1:
        debut=0
        while debut < 3 :
            if p[debut+(4*num_lig)]==0:
                line_pack(plateau,num_lig,debut,sens)
                return plateau
            
            elif p[debut+(4*num_lig)]<3 :
                if (p[debut+(4*num_lig)]+p[debut+1+(4*num_lig)])%3==0:
                    p[debut+(4*num_lig)]+=p[debut+1+(4*num_lig)]
                    p[debut+1+(4*num_lig)]=0
            
            elif p[debut+(4*num_lig)]>=3 :
                if p[debut+(4*num_lig)]==p[debut+1+(4*num_lig)]:
                    p[debut+(4*num_lig)]*=2
                    p[debut+1+(4*num_lig)]=0
            debut+=1
            
    elif sens==0:
        debut=3
        while debut > 0 :
            if p[debut+(4*num_lig)]==0:
                line_pack(plateau,num_lig,debut,sens)
                return plateau
            
            elif p[debut+(4*num_lig)]<3 :
                if (p[debut+(4*num_lig)]+p[debut-1+(4*num_lig)])%3==0:
                    p[debut+(4*num_lig)]+=p[debut-1+(4*num_lig)]
                    p[debut-1+(4*num_lig)]=0
            
            elif p[debut+(4*num_lig)]>=3 :
                if p[debut+(4*num_lig)]==p[debut-1+(4*num_lig)]:
                    p[debut+(4*num_lig)]*=2
                    p[debut-1+(4*num_lig)]=0
            debut-=1
            
    return plateau
#full_display(a)
#full_display(line_move(a,0,1))
