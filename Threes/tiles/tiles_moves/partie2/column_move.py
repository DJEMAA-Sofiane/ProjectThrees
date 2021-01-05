import sys
sys.path.insert(0,"C:\\module_jeu_threes\\game\\play")
sys.path.insert(0,'C:\\module_jeu_threes\\ui\\play_display')


from tableau_al import tableau_al
from full_display import full_display
from column_pack import column_pack

a=tableau_al(2)

def column_move(plateau,num_col,sens):
    p=plateau['tiles']
    if sens==1:
        debut=0
        while debut < 3 :
            if p[(debut*4)+(num_col)]==0:
                column_pack(plateau,num_col,debut,sens)
                return plateau
            
            elif p[(debut*4)+(num_col)]<3 :
                if (p[(debut*4)+(num_col)]+p[(debut*4+4)+(num_col)])%3==0:
                    p[(debut*4)+(num_col)]+=p[(debut*4+4)+(num_col)]
                    p[(debut*4+4)+(num_col)]=0                    
            
            elif p[(debut*4)+(num_col)]>=3 :
                if p[(debut*4)+(num_col)]==p[(debut*4+4)+(num_col)]:
                    p[(debut*4)+(num_col)]*=2
                    p[(debut*4+4)+(num_col)]=0
            debut+=1
        
    elif sens==0:
        debut=3
        while debut > 0 :
            if p[(debut*4)+(num_col)]==0:
                column_pack(plateau,num_col,debut,sens)
                return plateau
            
            elif p[(debut*4)+(num_col)]<3 :
                if (p[(debut*4)+(num_col)]+p[(debut*4-4)+(num_col)])%3==0:
                    p[(debut*4)+(num_col)]+=p[(debut*4-4)+(num_col)]
                    p[(debut*4-4)+(num_col)]=0
            
            elif p[(debut*4)+(num_col)]>=3 :
                if p[(debut*4)+(num_col)]==p[(debut*4-4)+(num_col)]:
                    p[(debut*4)+(num_col)]*=2
                    p[(debut*4-4)+(num_col)]=0
            debut-=1
            
    return plateau
#full_display(a)
#full_display(column_move(a,0,1))
