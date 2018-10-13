# Projet Euler22

# Algorithme principal
def solve():
    f=open('names.txt','r')
    s=0
    T=[]
    # construction de la liste des noms
    for ligne in f:
        T=T+ligne.split(",")
    # Enlever les " présents en première et dernière position des mots
    for k in range(len(T)):
        aux = list(T[k])
        aux = aux[:len(aux)-1]
        aux = aux[1:]
        aux2 = str()
        for lettre in aux:
            aux2 = aux2 + str(lettre)
        T[k]=aux2
    # Tri de T par ordre alphabétique
    T=sorted(T)
    # calcul de la somme
    for i,mot in enumerate(T):
        s+=(i+1)*valeur(mot)
    return(s)


# Calcul de la valeur d'un nom (en majuscules seulement)
def valeur(c):
    # Où c est la représentation en chaîne du nom
    # Tuple des valeurs des lettres de l'alphabet
    Va=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # dictionnaire de l'alphabet
    d={}
    for k,lettre in enumerate(Va):
        d[lettre]=k+1        
    # valeur du nom
    v=0
    C=list(c)
    for lettre in C:
        v+=d[lettre]
    return(v)


# Solution du problème d'Euler16
print('solve()=',solve())























## Tests

"""def transformation_de_lettres_en_valeurs(T):
    n=len(T)
    # Tuple des valeurs des lettres de l'alphabet
    Va=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')    
    L=[]
    Aux1 = []
    for k in range(n):
        Aux2 = []
        Aux1 = list(T[k])
        for i in range(len(Aux1)):
            if(Aux1[i]!='"'):
                for u in range(26):
                    if(Aux1[i]==Va[u]):
                        Aux2.append(u+1)
        L.append(Aux2)



def ordre_alphabétique(T):
    L=transformation_de_lettres_en_valeurs(T)
    n=len(L)
    V=[]  # liste des "valeurs" des noms
    for k in range(n):
        m=len(L[k])
        aux =0
        for i in range(m):
            aux = aux + L[k]*(10**(100-2*i))
        V.append(aux)"""