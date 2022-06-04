class Noeud:
    id = 0
    nbVoisin = 0
    # c'est plus simple d'ajouter et d'enlever des elements avec une liste qu'avec un array
    successeurs = []
    arcs = []  # Arcs sortant

    # cree un noeud isole
    # cree un noeud a partir d'une liste de voisins
    # les arcs sont de poids 1

    def __init__(self, id1=0, successeur=[], **args):
        self.id = id1
        self.successeurs = successeur
        if self.successeurs == []:
            self.arcs = []
        else:
            for a in range(len(self.successeurs)):
                self.arcs.append(1)
                self.nbVoisin = self.nbVoisin + 1

    # renvoie le nombre de voisins
    def nbVoisins(self):
        print("Le nombre de voisins est de ", len(self.successeurs))

    # renvoie le degre sortant, qui vaut la somme des elements de arcs
    def degreSortant(self):
        degSortant = 0
        for a in self.arcs:
            degSortant = degSortant + a
        return degSortant

    # renvoie l'indice de v dans voisins si v est voisin
    # renvoie -1 si v n'est pas voisin
    def estVoisin(self, v):
        if v.id in self.successeurs:
            return v.id
        else:
            return -1

    # renvoie le poids de l'arc correspondant si v est voisin, 0 sinon
    def nbArcs(self, v):
        indice = self.estVoisin(v)
        if indice != -1:
            position = self.successeurs.index(indice)
            return self.arcs[position - 1]
        else:
            return 0

    # si v est deja voisin, modifie la poids de l'arc correspondant
    # sinon, ajoute v comme un nouveau voisin avec un arc de poids d
    # (il faut incrementer nbArcs si c'est un nouveau voisin)
    # revoie le nouveau nombre de voisins
    def ajouteVoisin(self, v, d):
        indice = self.estVoisin(v)
        # print("La valeur indice est", indice)
        if indice != -1:  # Si le noeud est voisin
            position = self.successeurs.index(indice)
            self.arcs[position] = d
            # print(self.arcs[position])
        else:  # Si le noeud n'est pas voisin
            self.successeurs.append(v.id)
            self.arcs.append(d)
            self.nbVoisin = self.nbVoisin + 1
            # print(self.successeurs)
            # print(self.arcs)

        return self.nbVoisin

    # si v n'est pas voisin, ne fait rien
    # sinon enleve v de la liste de voisins
    # renvoie le nouveau nombre de voisins
    def enleveVoisin(self, v):
        indice = self.estVoisin(v)
        # print("La valeur indice est", indice)
        if indice != -1:
            position = self.successeurs.index(indice)
            del (self.successeurs[position])
            del (self.arcs[position])
            self.nbVoisin = self.nbVoisin - 1

        return self.nbVoisin

    def compareTo(self, o):
        if self.id > o.id:
            return 1
        elif self.id < o.id:
            return -1
        else:
            return 0

