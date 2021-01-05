from tableau_al import tableau_al

p=tableau_al(1)

def get_score(plateau):
    t=plateau["tiles"]
    i=0
    somme=0
    while i < len(t):
        somme+=t[i]
        i+=1
    return somme
#print(get_score(p))
