def get_user_move():
    x=''
    while x!="h" and x!="b" and x!="g" and x!="d" and x!="m":
        print("pour aller en :haut(h), bas(b), gauche(g), droite(d)")
        print('pour ouvrir le menu:(m)')
        x=input()
        x=x.lower()
    return x

#get_user_move()
