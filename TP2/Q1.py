#Utilitaire : générateur de séquences

#Q 1. Ecrire un générateur de séquences aléatoires sur l’alphabet {a, c, g, t}. La fonction prendra en paramètre la taille de la séquence à générer. On utilisera des fonctions de la librairie random.

import random

def gen_seq_alea(n: int) -> str:
    return ''.join([random.choice('ACGT') for _ in range(n)])+'$'

print("### Question 1 ###")
test = gen_seq_alea(10)
print(test,"\n")

#1 Tableau des suffixes

#Q 2. Implémentez l’ensemble des fonctions nécessaires au calcul du tableau des suffixes pour une séquence S. (énumération des suffixes, tri (sort() en python))
#return a list of index of suffixes of s
def tableau_des_suffixes(s):
    n = len(s)
    suffixes = [s[i:] for i in range(n)]
    suffixes.sort()
    return [s.find(suffix) for suffix in suffixes], suffixes

def tableau_des_suffixes2(s):
    n = len(s)
    suffixes = [s[i:] for i in range(n)]
    suffixes.sort()
    return [s.find(suffix) for suffix in suffixes]

test = tableau_des_suffixes(gen_seq_alea(10))

def affiche_tableau_des_suffixes(s, sa):
    print("Tableau des suffixes pour ")
    print("-------------------------------------")
    print("Index \t| Suffixe \t| Suffixe dans S")
    print("-------------------------------------")
    for i in range(len(s)):
        print(i,"\t\t|",sa[i],"\t\t|", s[i])
        print("-------------------------------------")

print("### Question 2 ###")
affiche_tableau_des_suffixes(test[1], test[0])

#Q 4. Implémentez la fonction search(p, s, sa) renvoyant :
#la position d’une occurrence du mot p dans s si elle existe
#-1 sinon

def search(p, s, sa):
    n = len(s)
    m = len(p)
    l = 0
    r = n-1
    while l <= r:
        mid = (l+r)//2
        if p == s[sa[mid]:sa[mid]+m]:
            return sa[mid]
        elif p < s[sa[mid]:sa[mid]+m]:
            r = mid-1
        else:
            l = mid+1
    return -1


print("### Question 4 ###")
p = "AGGTACC$"
test = search('AC', p , tableau_des_suffixes(p)[0])
affiche_tableau_des_suffixes(tableau_des_suffixes(p)[1], tableau_des_suffixes(p)[0])
print("Test P = AC dans "+p+" =", test,"\n")

p = gen_seq_alea(20)
test = search('AC', p , tableau_des_suffixes(p)[0])
affiche_tableau_des_suffixes(tableau_des_suffixes(p)[1], tableau_des_suffixes(p)[0])
print("Test P = AC dans "+p+" =", test,"\n")

#2 LCP array

#Q 5. Implémentez une fonction permettant de construire la LCP array à partir de S et SA.

def LCP(s, suffix_array):
    n = len(s)
    rank = [0 for i in range(n)]
    LCP = [0 for i in range(n)]
    for i in range(n):
        rank[suffix_array[i]] = i
    l = 0
    for j in range(n):
        l = max(0, l-1)
        i = rank[j]
        j2 = suffix_array[i-1]
        if i:
            while l + j < n and l + j2 < n and s[j+l] == s[j2+l]:
                l += 1
            LCP[i] = l
    return LCP

def affiche_tableau_lcp(s, sa, lcp):
    print("Tableau des suffixes pour ")
    print("--------------------------------------------")
    print("Index \t| Suffixe \t| LCP \t| Suffixe dans S")
    print("--------------------------------------------")
    for i in range(len(s)):
        print(i,"\t\t|",sa[i],"\t\t|", lcp[i],"\t\t|", s[i])
        print("--------------------------------------------")


p = gen_seq_alea(20)
print("### Question 5 ###")
test = LCP(p, tableau_des_suffixes(p)[0])
print("Test LCP de "+p, test,"\n")
affiche_tableau_lcp(tableau_des_suffixes(p)[1], tableau_des_suffixes(p)[0], test)

#Q 7. Implémentez la fonction longest_repeat(s, sa, lcp) qui renvoie les plus grand mots répétés de S ainsi que leurs positions dans S.

def longest_repeat(s, sa, lcp):
    n = len(s)
    max_lcp = max(lcp)
    index = lcp.index(max_lcp)
    return s[sa[index]:sa[index]+max_lcp], sa[index]

print("### Question 7 ###")
p = gen_seq_alea(20)
test = longest_repeat(p, tableau_des_suffixes(p)[0], LCP(p, tableau_des_suffixes(p)[0]))
affiche_tableau_lcp(tableau_des_suffixes(p)[1], tableau_des_suffixes(p)[0], LCP(p, tableau_des_suffixes(p)[0]))
print("Test longest_repeat de "+p, test,"\n")

#Q 8. Comparez le résultat de cette fonction pour des séquences biologiques et pour des séquences aléatoires. La séquence biologique se trouve dans le fichier MC58.fasta (séquence du génome de la bactérie
#Neisseria meningitidis strain MC58) (utiliser la fonction get_seq_from_f asta dans le fichier fasta.py)

from fasta import get_seq_from_fasta

print("### Question 8 ###")
p = get_seq_from_fasta("MC58.fasta")
test = longest_repeat(p+"$", tableau_des_suffixes2(p), LCP(p, tableau_des_suffixes2(p)))
print("Test longest_repeat de "+p, test,"\n")

