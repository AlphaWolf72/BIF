class DynamicMatrix:
    '''
    stores a matrix |S|x|T| (|S|+1 lines and |T|+1columns), sequences S and T and the score system (match, mismatch, gap)
    defines some global alignment functions
    '''

    def __init__(self, S, T, match, mismatch, gap):
        ''' defines and stores initial values'''

        self.S = S
        self.T = T
        self.gap = gap
        self.match = match
        self.mismatch = mismatch

        self.matrix = [0 for i in range(len(S) + 1)]
        for i in range(len(S) + 1):
            self.matrix[i] = [0 for j in range(len(T) + 1)]

    def printMatrix(self):
        ''' prints the matrix'''

        width = 4
        vide = " "
        line = f"{vide:>{2 * width}}"
        for j in range(0, len(self.T)):
            line += f"{self.T[j]:>{width}}"
        print(line)
        line = f"{vide:>{width}}"
        for j in range(0, len(self.T) + 1):
            line += f"{self.matrix[0][j]:>{width}}"
        print(line)
        for i in range(1, len(self.S) + 1):
            line = f"{self.S[i - 1]:>{width}}"
            for j in range(0, len(self.T) + 1):
                line += f"{self.matrix[i][j]:>{width}}"
            print(line)

    # 1 Préliminaires
    # Q 1. Quel type d’objet python est utilisé pour stocker la matrice de programmation dynamique ?
    # Avec quelle commande accède-t-on à la valeur de la cellule en face de la i-ème lettre de S et la j-ième de T ?
    # Une list de list. matrix[i][j] donne la valeur de la cellule i j.

    # Q 2. Écrire une méthode score qui prend en argument 2 caractères et qui renvoie le score d’un match si
    # les deux caractères sont égaux et le score d’un mismatch sinon.
    def score(self, a, b):
        if a == b:
            return self.match
        else:
            return self.mismatch

    # 2 Alignement global
    # Q 3. Écrire une méthode initGlobal qui initialise la matrice pour l’alignement global (première ligne et première colonne).
    def initGlobal(self):
        for i in range(1, len(self.S) + 1):
            self.matrix[i][0] = i * self.gap
        for j in range(1, len(self.T) + 1):
            self.matrix[0][j] = j * self.gap

    #Q 4. Écrire une méthode fill qui remplit la matrice selon l’algorithme de Needleman-Wunsch (formule
    # de récurrence avec les trois cases voisines en haut et à gauche), et renvoie le score du meilleur alignement
    # global des deux séquences.
    def fill(self):
        for i in range(1, len(self.S) + 1):
            for j in range(1, len(self.T) + 1):
                self.matrix[i][j] = max(
                    self.matrix[i - 1][j - 1] + self.score(self.S[i - 1], self.T[j - 1]),
                    self.matrix[i - 1][j] + self.gap,
                    self.matrix[i][j - 1] + self.gap
                )
        return self.matrix[len(self.S)][len(self.T)]

    #Q 5. Proposer une méthode printGlobalAln qui affiche un alignement de meilleur score de S contre T qui renvoie son pourcentage d’identité.
    def printGlobalAln(self):
        i = len(self.S)
        j = len(self.T)
        alnS = ""
        alnT = ""
        while i > 0 or j > 0:
            if i > 0 and j > 0 and self.matrix[i][j] == self.matrix[i - 1][j - 1] + self.score(self.S[i - 1], self.T[j - 1]):
                alnS = self.S[i - 1] + alnS
                alnT = self.T[j - 1] + alnT
                i -= 1
                j -= 1
            elif i > 0 and self.matrix[i][j] == self.matrix[i - 1][j] + self.gap:
                alnS = self.S[i - 1] + alnS
                alnT = "-" + alnT
                i -= 1
            else:
                alnS = "-" + alnS
                alnT = self.T[j - 1] + alnT
                j -= 1
        print("alignement optimal :")
        print(alnS)
        print(alnT)
        ident = 0
        for i in range(len(alnS)):
            if alnS[i] == alnT[i]:
                ident += 1
        print(f"pcId = {100 * ident / len(alnS)}%")

    #3 Heuristique : alignement contraint dans une bande
    # Q 6. Implémenter une heuristique de l’alignement global qui consiste à contraindre l’alignement autour de
    # la diagonale dans une bande. Dans cette heuristique, on gagne du temps puisqu’on ne remplit pas la matrice
    # en entier, mais seulement une sous-partie : les cellules situées autour de la diagonale (bande). C’est une
    # heuristique car on n’explore pas tout l’espace de recherche, on peut donc manquer un alignement de score
    # maximal qui "deborderait" de la bande. La largeur horizontale de la bande sera déterminée par le paramètre
    # width, qui représente le nombre de cellules à gauche (et à droite) des cellules (i, i) à considérer dans la
    # bande, soit une largeur de bande égale à 2×width+1. On se restreindra au cas où les 2 séquences sont de
    # même taille et on se contentera de calculer le score de l’alignement global (sans afficher l’alignement).

    # initBand initialise tout ce qui est en dehors de la bande à -inf
    def initBand(self, width):
        for i in range(1, width + 1):
            self.matrix[i][0] = i * self.gap
        for i in range(width + 1, len(self.S) + 1):
            self.matrix[i][0] = float("-inf")
        for j in range(1, width + 1):
            self.matrix[0][j] = j * self.gap
        for j in range(width + 1, len(self.T) + 1):
            self.matrix[0][j] = float("-inf")
        for i in range(1, len(self.S) + 1):
            for j in range(1, len(self.T) + 1):
                if abs(i - j) > width:
                    self.matrix[i][j] = float("-inf")

    def fillBand(self, width):
        for i in range(1, len(self.S) + 1):
            for j in range(max(1, i - width), min(len(self.T) + 1, i + width + 1)):
                self.matrix[i][j] = max(
                    self.matrix[i - 1][j - 1] + self.score(self.S[i - 1], self.T[j - 1]),
                    self.matrix[i - 1][j] + self.gap,
                    self.matrix[i][j - 1] + self.gap
                )
        return self.matrix[len(self.S)][len(self.T)]



#m = DynamicMatrix("GGATAGC","AATGAATC", 2, -1, -2)
#m.initGlobal()
#m.initBand(1)
#m.fillBand(1)
#m.printMatrix()
#m.printGlobalAln()