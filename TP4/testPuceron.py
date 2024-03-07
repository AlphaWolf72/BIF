import random
import time
from TP4.dynamicProg import DynamicMatrix

def parse_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as fasta_file:
        current_sequence = ''
        for line in fasta_file:
            line = line.strip()
            if line.startswith('>'):
                current_sequence = line[1:]
                sequences[current_sequence] = ''
            else:
                sequences[current_sequence] += line
    return sequences

file_path = "sequences_puceron.fasta"
sequences = parse_fasta(file_path)

sequences = parse_fasta(file_path)  # Supposons que parse_fasta est une fonction qui lit le fichier FASTA et renvoie un dictionnaire de séquences

first_sequence = list(sequences.values())[0]  # Récupérer la première séquence
remaining_sequences = list(sequences.values())[1:]  # Exclure la première séquence

pairs = [(first_sequence, sequence) for sequence in remaining_sequences]  # Créer des paires avec la première séquence et chaque séquence restante

width = [1, 5, 10, 20, 40]

# On initialise les scores et les temps de calcul
scores = {}
times = {}
for t in range(len(pairs)):
    scores[t] = {"Exact": [], "Heuristique": []}
    times[t] = {"Exact": [], "Heuristique": []}

# On effectue les tests
for t in range(len(pairs)):
    S, T = pairs[t]
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
for t in range(len(pairs)):
    print("width \tscore \ttemps")
    print("___________________________________")
    for w in width:
        print(w, "\t\t", scores[t]["Heuristique"][width.index(w)], "\t", times[t]["Heuristique"][width.index(w)])
    print("___________________________________")
    print("Exact ", "\t", scores[t]["Exact"][0], "\t", times[t]["Exact"][0], "\n")
