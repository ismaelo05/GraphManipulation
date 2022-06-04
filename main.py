from graph import Graphe
from noeud import Noeud

#Graph
"""G1 = [2, 5, 4]
G2 = Graphe()
G2.affiche()
G3 = Graphe(G1)
G3.affiche()"""
N1 = Noeud(1, [3, 5, 7, 6, 4])
N2 = Noeud(2, [3, 5, 4])
N3 = Noeud(3, [1, 2, 5])
N4 = Noeud(4, [1, 2, 6])
N5 = Noeud(5, [3, 2, 1, 6, 7])
N6 = Noeud(6, [4, 1, 5, 7])
N7 = Noeud(7, [6, 1, 5])
G = Graphe(N1)
G = Graphe(N2)
G = Graphe(N3)
G = Graphe(N4)
G = Graphe(N5)
G = Graphe(N6)
G = Graphe(N7)
G.affiche()
G.DFS(N3)
G.BFS(N3)
# G.cheminDFS(N2, N7)
# G.cheminBFS(N2, N7)

#Noeud
"""N8 = Noeud()
N8.nbVoisins()
print()
noeud = 1
Liste_sucess = [2, 5, 7]
N9 = Noeud(noeud, Liste_sucess)
N9.nbVoisins()
degre = N9.degreSortant()
print("Le degre sortant du noeud N2 est", degre)

#Voisins du noeud
#Affiche -1 si n'est pas voisin mais si voisin afficher l'indice du noeud
N10 = Noeud(5)
N11 = Noeud(10)
N12 = Noeud(12)
Vois1 = N2.estVoisin(N10)
print(Vois1)
vois2 = N9.estVoisin(N4)
print(vois2)
print()


#Nombre d'arc
nomArc1 = N9.nbArcs(N10)
print(nomArc1)
nomArc2 = N9.nbArcs(N11)
print(nomArc2)
print()


#Ajouter un noeud comme voisin
ajout1 = N9.ajouteVoisin(N10, 4)
print("Le nombre de voisins est:", ajout1)
ajout2 = N9.ajouteVoisin(N11, 5)
print("Le nombre de voisins est:", ajout2)
print()

#Enlever un noeud Voisin
enlev1 = N9.enleveVoisin(N10)
print("Le nombre de voisins est:", enlev1)
enlev2 = N9.enleveVoisin(N12)
print("Le nombre de voisins est:", enlev2)
print()

#Comparaison d'un noeud et du noeud courant
compa1 = N9.compareTo(N8)
print("Compraison de noeud:", compa1)
compa1 = N9.compareTo(N12)
print("Compraison de noeud:", compa1)"""