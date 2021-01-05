import sys
sys.path.insert(0,"C:\\module_jeu_threes")

from game.play.tableau_al import tableau_al

p=tableau_al(1000000)

def full_display(plateau):
    i=0
    plat=""
    j=0
    p=plateau['tiles']
    
    while i<4:
        plat="|"+str(p[0+j]).center(6)+"|"+str(p[1+j]).center(6)+"|"+str(p[2+j]).center(6)+"|"+str(p[3+j]).center(6)+"|"
        print('-----------------------------')
        print(plat)
        j+=4
        i+=1
    print('-----------------------------')
#full_display(p)
#print(p)

