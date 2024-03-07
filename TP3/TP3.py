#1 Build BWT
#Q 1. Codez (et testez) la fonction get_BW T(S, SA) renvoyant la transformée de Burrows Wheeler BW T
#du texte S. Pour le calcul du tableau des suffixes, vous pouvez utiliser votre implémentation du TP2 ou
#utiliser la fonction SA = simple_kark_sort(S). (from karkkainan import simple_kark_sort)

from karkkainen import simple_kark_sort

def get_BWT(S, SA):
    n = len(S)
    return ''.join([S[i-1] for i in SA])

#Test Q1
print("### Question 1 ###")

S = "AACCGATTAACC$"
SA = simple_kark_sort(S)
print("S =", S)
print("SA =", SA)
print("BWT =", get_BWT(S, SA), "\n")

#2 Reverse BWT
#Q 2. Codez la fonction get_R(BW T) renvoyant un tableau tel que R[i]= rang dans BW T du caractère BW T[i].

def get_R(BWT):
    n = len(BWT)
    R = [0]*n
    for i in range(n):
        R[i] = BWT[:i].count(BWT[i])+1
    return R

#Test Q2
print("### Question 2 ###")

BWT = get_BWT(S, SA)
R = get_R(BWT)
print("BWT =", BWT)
print("R =", R, "\n")

#Q 3. Codez la fonction get_N(BW T) renvoyant un tableau associatif tel que N[c] = position du premier c dans F.
#Rappel : si BWT(S) est la dernière colonne de la matrice des rotations cycliques de S dans l’ordre lexicographique, F en est la première colonne.

def get_N(BWT):
    N = {}
    A = BWT.count("A")
    C = A + BWT.count("C")
    G = C + BWT.count("G")
    N["$"] = 0
    N["A"] = 1
    N["C"] = A + 1
    N["G"] = C + 1
    N["T"] = G + 1

    return N

#Test Q3
print("### Question 3 ###")

N = get_N(BWT)
print("BWT =", BWT)
print("N =", N, "\n")

#Q 4. Codez la fonction LF(c, r, N) qui renvoie la position dans F du caractère c de rang r.

def LF(c, r, N):
    return N[c] + r - 1

#Test Q4
print("### Question 4 ###")

c = "A"
r = 3
print("c =", c)
print("r =", r)
print("LF(c, r, N) =", LF(c, r, N), "\n")

#Q 5. Codez la fonction BW T2seq(BW T, N, R) qui reconstruit, en temps linéaire, la séquence S à partir de sa BW T.

def BW_T2seq(BWT, N, R):
    res = "$"
    ligne = 0
    while BWT[ligne] != "$":
        res = BWT[ligne] + res
        ligne = LF(BWT[ligne], R[ligne], N)
    return res

#Test Q5
print("### Question 5 ###")

print("BWT =", BWT)
print("N =", N)
print("R =", R)
print("BW T2seq(BW T, N, R) =", BW_T2seq(BWT, N, R), "\n")


#3 Pattern matching - BWT
#Q 6. Codez la fonction f ind_f irst(c, i, BW T) qui renvoie la position du premier c entre i et |BW T| − 1.

def find_first(c, i, i_max, BWT):
    for j in range(i, i_max):
        if BWT[j] == c:
            return j
    return -1

#Test Q6
print("### Question 6 ###")

c = "A"
i = 0
i_max = len(BWT)
print("c =", c)
print("i =", i)
print("i_max =", i_max)
print("f ind_f irst(c, i, BW T) =", find_first(c, i, i_max, BWT), "\n")

#Q 7. Codez la fonction f ind_last(c, j, BW T) qui renvoie la position du dernier c entre 0 et j.

def find_last(c, i, i_max, BWT):
    for j in range(i_max-1, i-1, -1):
        if BWT[j] == c:
            return j
    return -1

#Test Q7
print("### Question 7 ###")

c = "A"
i = 0
i_max = len(BWT)
print("c =", c)
print("i =", i)
print("i_max =", i_max)
print("find_last(c, j, BW T) =", find_last(c, i, i_max, BWT), "\n")

#Q 8. A partir des fonctions LF, f ind_f irst et f ind_last, codez la fonction P_in_S(P, BW T, N, R, SA) qui
#renvoie les occurences de P dans S si elles existent, sinon -1.

def P_in_S(P, BWT, N, R, SA):
    start = 0
    end = len(BWT) - 1
    for i in range(len(P)-1, -1, -1):
        l = find_first(P[i], start, end+1, BWT)
        if l == -1:
            return -1
        if i > 0:
            n_start = LF(P[i], R[l], N)
            end = LF(P[i], R[find_last(P[i], start, end+1, BWT)], N)
            start = n_start

    return [SA[i] for i in range(start, end+1)]

#Test Q8
print("### Question 8 ###")

P = "ACC"
SA = simple_kark_sort(S)
print("P =", P)
print("SA =", SA)
print("P_in_S(P, BW T, N, R, SA) =", P_in_S(P, BWT, N, R, SA), "\n")

#4 Bonus
#Q 9. Garder les rangs est coûteux en mémoire, implémentez un sous-échantillonage des rangs pour sacrifier
#un peu de temps de calcul au profit d’espace mémoire. Pour ce faire , codez get_R_bis(BW T, p) qui notera
#une valeur des rangs de chaque caractère de la BWT tous les p caractères.

def get_R_bis(BWT, p):
    Res = {}
    for i in range(p, len(BWT), p):
        A = BWT[:i].count("A")
        C = BWT[:i].count("C")
        G = BWT[:i].count("G")
        T = BWT[:i].count("T")
        Res[i] = [A, C, G, T]
    return Res

#retourne le rang de BWT[i] dans R de get_R_bis
def get_Rang(BWT, i, R):
    res = 0
    if i % p == 0:
        if BWT[i] == "A":
            return R[i][0]
        if BWT[i] == "C":
            return R[i][1]
        if BWT[i] == "G":
            return R[i][2]
        if BWT[i] == "T":
            return R[i][3]
    if i % p > p//2:
        var = ((i // p)+1) * p
        if BWT[i] == "A":
            res = R[var][0]
        if BWT[i] == "C":
            res = R[var][1]
        if BWT[i] == "G":
            res = R[var][2]
        if BWT[i] == "T":
            res = R[var][3]
        for j in range(var, i, -1):
            if BWT[j] == BWT[i]:
                res = res - 1
        return res
    else:
        var = i // p * p
        print(R[var])
        if BWT[i] == "A":
            res = R[var][0]
            print(res)
        if BWT[i] == "C":
            res = R[var][1]
        if BWT[i] == "G":
            res = R[var][2]
        if BWT[i] == "T":
            res = R[var][3]
        for j in range(var, i+1):
            if BWT[j] == BWT[i]:
                res = res + 1
        return res


#Test Q9
print("### Question 9 ###")

p = 5
print("p =", p)
print("get_R_bis(BW T, p) =", get_R_bis(BWT, p), "\n")

#test de get_Rang
R = get_R_bis(BWT, p)
i = 12
print("i =", i)
print("get_Rang(BW T, i, R) =", get_Rang(BWT, i, R), "\n")

#Q 10. Idem, pour SA.

def simple_kark_sort_bis(S, p):
    SA = simple_kark_sort(S)
    print(SA)
    Res = {}
    for i in range(p, len(BWT), p):
        A = SA[:i].count("A")
        C = SA[:i].count("C")
        G = SA[:i].count("G")
        T = SA[:i].count("T")
        Res[i] = [A, C, G, T]
    return Res

#Test Q10
print("### Question 10 ###")

p = 4
print("p =", p)
print("simple_kark_sort_bis(S, p) =", simple_kark_sort_bis(S, p), "\n")
