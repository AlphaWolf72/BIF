import random
import time

from TP4.dynamicProg import DynamicMatrix


# 4 Tests de l’heuristique
# Dans cette section nous utiliserons match = 2, mismatch = −1, gap = −2.
# Q 7. Générer des couples de séquences d’ADN aléatoires de taille 500, 1000, et 2000. Pour chacune de ces
# tailles, tester l’alignement global exact et l’alignement global heuristique (score et temps de calcul), avec
# différentes valeurs de width : 1, 5, 10, 20 et 40. Vous présenterez les résultats sous la forme de tableaux, un
# tableau par taille de séquence (cf. exemple ci-dessous). Quelles conclusions tirer des résultats obtenus ?
# Exemple de tableau pour la taille 500 :
#taille = 500pb
#width score temps
# 1
# 5
# 10
# 20
# 40
# Exact

taille = [500, 1000, 2000]
width = [1, 5, 10, 20, 40]

# On génère les séquences d'ADN aléatoires
sequences = {}
for t in taille:
    sequences[t] = ("".join(random.choices("ACGT", k=t)), "".join(random.choices("ACGT", k=t)))

# On initialise les scores et les temps de calcul
scores = {}
times = {}
for t in taille:
    scores[t] = {"Exact": [], "Heuristique": []}
    times[t] = {"Exact": [], "Heuristique": []}

# On effectue les tests
for t in taille:
    S, T = sequences[t]
    # Alignement global exact
    D = DynamicMatrix(S, T, 2, -1, -2)
    D.initGlobal()
    start = time.time()
    scores[t]["Exact"].append(D.fill())
    times[t]["Exact"].append(time.time() - start)
    for w in width:
        # Alignement global heuristique
        D = DynamicMatrix(S, T, 2, -1, -2)
        D.initBand(w)
        start = time.time()
        scores[t]["Heuristique"].append(D.fillBand(w))
        times[t]["Heuristique"].append(time.time() - start)

# On affiche les résultats
for t in taille:
    print(f"taille = {t}pb")
    print("width \tscore \ttemps")
    print("___________________________________")
    for w in width:
        print(w, "\t\t", scores[t]["Heuristique"][width.index(w)], "\t", times[t]["Heuristique"][width.index(w)])
    print("___________________________________")
    print("Exact ", "\t", scores[t]["Exact"][0], "\t", times[t]["Exact"][0], "\n")

# Quelles conclusions tirer des résultats obtenus ?
# On observe que plus la taille des séquences est grande, plus le temps de calcul est long. On observe également que
# le score de l'alignement global exact est toujours supérieur ou égal à celui de l'alignement global heuristique.
# Enfin, on observe que plus la largeur de la bande est grande, plus le temps de calcul est long.