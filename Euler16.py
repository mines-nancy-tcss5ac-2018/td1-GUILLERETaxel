# projet Euler numéro 16
def solve(n):
    # n la puissance de 2
    N=2**n
    # s la somme des chiffres de N
    s=0
    Nenbase10=[]
    # p un indice des puissances de 10
    p=0
    # on décompose N en base 10
    while((N/(10**p)) >= 1):
        p=p+1
    for u in range(p-1,-1,-1):
        # valeur du coefficient 
        d=int(N/(10**u))
        Nenbase10.append(d)
        # on soustrait à N ce que l'on a mis dans la liste Nenbase10
        N=N-(10**u)*d
    # On somme tous les coefficients dans Nenbase10
    for k in range(len(Nenbase10)):
        s=s+Nenbase10[k]
    return(s)

# solution du problème d'Euler16
print('solve(1000) =', solve(1000))
assert solve(15)==26