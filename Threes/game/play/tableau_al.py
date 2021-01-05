from random import*

def tableau_al(n):
    p={'n':4,"nb_cases_libres":16}
    t=[]
    i=0
    while i<16:
        t.append(randint(1,n))
        i+=1
    p["tiles"]=t
    return p
#p=tableau_al(10)
#print(p)
