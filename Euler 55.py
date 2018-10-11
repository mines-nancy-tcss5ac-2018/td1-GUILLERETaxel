# Problème d'Euler 55

# Fonction testant si un nombre est un palindrome
def palindrome(M):
    p=0
    mM=[]   # reprÃ©sentation de M sous forme de liste
    # Décomposition de M en base 10
    while(M/(10**p) >= 1):
        p=p+1
    for u in range(p-1,-1,-1):
        d=int(M/(10**u))
        mM.append(d)
        M=M-(10**u)*d
    # Test si M est un palindrome
    l=len(mM)
    c=True
    for r in range(0,int(l/2)):
        if(mM[r]!=mM[l-1-r]):
            c=False
    return(c)

# Test si n + "n ecrit à l'envers" est un palindrome
def auxiliaire(n):
    #Booléen de vérification
    C = False
    # Représentation de n sous forme de liste
    Aux = list(str(n))
    # Création du "symetrique" de n, noté s
    s = 0
    l = len(Aux)
    for k in range(l):
        s = s + int(Aux[l-1-k])*(10**(l-1-k))        
    if(palindrome(n+s)==True):
        C = True
    return(C,n+s)

def solve(N):
    # compteur
    c = 0
    for n in range(N):
        m=n
        i=0
        aux = auxiliaire(m)
        while(i<50)and(aux[0]==False):
            i=i+1
            m=aux[1]
            aux = auxiliaire(m)
        # Si ce n'est toujours pas un palindrome après 50 itérations
        if(aux[0]==False):
            c=c+1
    return(c)

# Solution de Euler 55
print('solve(10000) =', solve(10000))  