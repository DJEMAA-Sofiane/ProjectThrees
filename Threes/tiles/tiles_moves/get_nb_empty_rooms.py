import sys
sys.path.insert(0,"C:\\module_jeu_threes")
from game.play.init_play import init_play

p=init_play()

def get_nb_empty_rooms(plateau):
    t=plateau["tiles"]
    plateau["nb_cases_libres"]=16
    i=0
    j=0
    while i<len(t):
        if t[i]!=0:
            j+=1
        i+=1
    plateau["nb_cases_libres"]-=j
    return plateau["nb_cases_libres"]
#print(get_nb_empty_rooms(p))    
            
