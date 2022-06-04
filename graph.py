
# Implémentation d'un graphe avec python
# Ici, il est question de pouvoir utiliser le code pour implémenter
# les graphes en python dans le cadre du cours de
# Recherche Opérationnelle
from noeud import Noeud
from arbre import Arbre
class Graphe:
    # Classe représentant un graphe
    nbNoeuds = 0
    noeuds = []

    def __init__(self, nds):
        # A implémenter ce constructeur
        self.noeuds.append(nds)
        self.nbNoeuds = len(self.noeuds)


    def affiche(self):
        # Affiche les éléments d'un graphe
        print("Ce graphe possède ", self.nbNoeuds, " noeuds")

    #################################################################################################
    #################################################################################################
                                #Parcours en profondeur d’abord (DFS)
    #################################################################################################
    #################################################################################################
    def DFS(self, noeud):
        la_pile = [] # Liste contenant la liste des voisins du noeud courant non traité
        list_noeud_traite = [] # Liste des noeuds non traités
        # circuit Liste des noeuds courant, voisins du noeud courant et traités
        # circuit va permettre d'éviter les circuits lors de la construction de l'arbre
        circuit = []
        la_pile.append(noeud.id) # Ajouter le sommet du noeud de départ
        if noeud in self.noeuds: # Permet de vérifier si le noeud appartient au graphe
            index = self.noeuds.index(noeud) # Renvoie l'indice ou position du noeud dans le graphe
            # print(index)
        else:
            return # Noeud n'appartenant pas au graphe
        # liste_arbre = list((noeud.id, noeud.successeurs))
        liste_arbre = [] # Création d'une liste de tuple représentant l'arbre
        # arbre = Arbre(noeud.id, None, noeud.successeurs)
        racine = None # variable permettant de dire qu'il n'y a pas de parent du sous-arbre
        circuit.append(noeud.id) # initialiser la variable circuit au 1er sommet
        node = la_pile[-1] # Récupérer le dernier élément de la liste ie le sommet de la pile
        instruction = 0
        while la_pile: # sort de while quand la_pile est vide
            del la_pile[-1] # Supprime le dernier élément de la liste
            if node not in list_noeud_traite: # Teste si le sommet a déjà été traité
                list_noeud_traite.append(node) # Ajoute à la liste des sommets traité le sommet
                unvisited = [n for n in noeud.successeurs if n not in list_noeud_traite]
                # unvisited contient tous les voisins non-traités du noeud courant
                enfant = [n for n in noeud.successeurs if n not in (circuit)]
                # enfant contient tous voisins du noeud courant qui ne sont pas dans la_pile
                # et unvisited y compris le noeud courant lui meme
                la_pile.extend(unvisited) # Ajoute les voisins du noeud courant à la_pile
                circuit.extend(unvisited) # Ajoute les voisins du noeud courant à ciruit
                circuit = list(set(circuit))
                # Forme une liste unique d'élément de circuit ie évite supprime
                # les doublons d'éléments
                node = la_pile[-1] # Contient le dernier sommet de la liste
                if racine != noeud.id and racine != None:
                    # Vérifie si un sommet a un parent et des enfants
                    arbre = Arbre(noeud.id, racine, enfant) # Construit l'arbre avec parent et enfants
                    # enfant = [n for n in noeud.successeurs if n not in circuit]
                    liste_arbre.append((noeud.id, enfant)) # Construit l'arbre sous forme de liste
                    # avec parent et enfants
                    racine = node # Modifie la valeur du parent
                else: # si sous-arbre n'a pas de parent ou d'enfants
                    liste_arbre.append((noeud.id, enfant))
                    arbre = Arbre(noeud.id, racine, enfant)
                    racine = noeud.id
                    # print(racine)
            for a in self.noeuds: # Parcourt du graphe
                if a.id == node: # Vérifie si le noeud sommet courant est un sommet du graphe
                    noeud = a # Changer le courant
                    instruction = instruction + 1
                    index = self.noeuds.index(noeud) # Prendre sa nouvelle position dans le graphe
                    break
        print("La liste des sommets traités sont:")
        print(list_noeud_traite)  # Afficher la liste des sommet traités
        print("L'arbre obtenu par un parcours en profondeur est le suivant:")
        print("le nombre d'intruction est:", instruction)
        print(liste_arbre)        # Afficher l'arbre couvrant sous forme de liste
        print()
        print()
        print()

    #################################################################################################
    #################################################################################################
                                # Parcours en largeur d’abord (BFS)
    #################################################################################################
    #################################################################################################
    def BFS(self, noeud):
        la_pile = [] # Liste contenant la liste des voisins du noeud courant non traité
        list_noeud_traite = [] # Liste des noeuds non traités
        # circuit Liste des noeuds courant, voisins du noeud courant et traités
        # circuit va permettre d'éviter les circuits lors de la construction de l'arbre
        circuit = []
        la_pile.append(noeud.id) # Ajouter le sommet du noeud de départ
        if noeud in self.noeuds: # Permet de vérifier si le noeud appartient au graphe
            index = self.noeuds.index(noeud) # Renvoie l'indice ou position du noeud dans le graphe
            # print(index)
        else:
            return # Noeud n'appartenant pas au graphe
        # liste_arbre = list((noeud.id, noeud.successeurs))
        liste_arbre = [] # Création d'une liste de tuple représentant l'arbre
        # arbre = Arbre(noeud.id, None, noeud.successeurs)
        racine = None # variable permettant de dire qu'il n'y a pas de parent du sous-arbre
        circuit.append(noeud.id) # initialiser la variable circuit au 1er sommet
        node = la_pile[0] # Récupérer le premier élément de la liste ie le 1er de la file
        instruction = 0
        while la_pile: # sort de while quand la_pile est vide
            instruction = instruction + 1
            del la_pile[0] # Supprime le 1er élément de la liste
            if node not in list_noeud_traite: # Teste si le sommet a déjà été traité
                list_noeud_traite.append(node) # Ajoute à la liste des sommets traité le sommet
                unvisited = [n for n in noeud.successeurs if n not in list_noeud_traite]
                # unvisited contient tous les voisins non-traités du noeud courant
                enfant = [n for n in noeud.successeurs if n not in (circuit)]
                # enfant contient tous voisins du noeud courant qui ne sont pas dans la_pile
                # et unvisited y compris le noeud courant lui meme
                for a in unvisited:
                    la_pile.insert(0, a) # Ajoute les voisins du noeud courant à la_pile
                # print(la_pile)
                circuit.extend(unvisited) # Ajoute les voisins du noeud courant à ciruit
                circuit = list(set(circuit))
                # Forme une liste unique d'élément de circuit ie évite supprime
                # les doublons d'éléments
                node = la_pile[0] # Contient le 1er sommet de la liste
                if racine != noeud.id and racine != None:
                    # Vérifie si un sommet a un parent et des enfants
                    arbre = Arbre(noeud.id, racine, enfant) # Construit l'arbre avec parent et enfants
                    # enfant = [n for n in noeud.successeurs if n not in circuit]
                    liste_arbre.append((noeud.id, enfant)) # Construit l'arbre sous forme de liste
                    # avec parent et enfants
                    racine = node # Modifie la valeur du parent
                else: # si sous-arbre n'a pas de parent ou d'enfants
                    liste_arbre.append((noeud.id, enfant))
                    arbre = Arbre(noeud.id, racine, enfant)
                    racine = noeud.id
                    # print(racine)
            for a in self.noeuds: # Parcourt du graphe
                if a.id == node: # Vérifie si le noeud sommet courant est un sommet du graphe
                    noeud = a # Changer le courant
                    # index = self.noeuds.index(noeud) # Prendre sa nouvelle position dans le graphe
                    break
        print("La liste des sommets traités sont:")
        print(list_noeud_traite)  # Afficher la liste des sommet traités
        print("L'arbre obtenu par un parcours en largeur est le suivant:")
        print(liste_arbre)        # Afficher l'arbre couvrant sous forme de liste
        print("le nombre d'intruction est:", instruction)
        print()
        print()

        #################################################################################################
        #################################################################################################
                            # Chemin Parcours en profondeur d’abord (DFS)
        #################################################################################################
        #################################################################################################

    def cheminDFS(self, noeud1, noeud2):
        la_pile = []  # Liste contenant la liste des voisins du noeud courant non traité
        list_noeud_traite = []  # Liste des noeuds non traités
        la_pile.append(noeud1.id)  # Ajouter le sommet du noeud de départ
        if noeud1 not in self.noeuds or noeud2 not in self.noeuds:  # Permet de vérifier si le noeud1 et 2 appartient au graphe
            return
        node = la_pile[-1]  # Récupérer le dernier élément de la liste ie le sommet de la pile
        while la_pile:  # sort de while quand la_pile est vide
            del la_pile[-1]  # Supprime le dernier élément de la liste
            if node not in noeud2.successeurs:
                if node not in list_noeud_traite:  # Teste si le sommet a déjà été traité
                    list_noeud_traite.append(node)  # Ajoute à la liste des sommets traité le sommet
                    unvisited = [n for n in noeud1.successeurs if n not in list_noeud_traite]
                    # unvisited contient tous les voisins non-traités du noeud courant
                    la_pile.extend(unvisited)  # Ajoute les voisins du noeud courant à la_pile
                    node = la_pile[-1]  # Contient le dernier sommet de la liste
                for a in self.noeuds:  # Parcourt du graphe
                    if a.id == node:  # Vérifie si le noeud sommet courant est un sommet du graphe
                        noeud1 = a  # Changer le courant
                        break
            else:
                print("La chemin parcourir en profondeur en ces 2 noeud est:")
                list_noeud_traite.extend([node, noeud2.id])
                print(list_noeud_traite)  # Afficher la liste des sommet traités
                print()
                print()
                return
        print("Pas de chemin existnt")
        print()
        print()


    #################################################################################################
    #################################################################################################
                                # Chemin Parcours en largeur d’abord (BFS)
    #################################################################################################
    #################################################################################################
    def cheminBFS(self, noeud1, noeud2):
        la_pile = []  # Liste contenant la liste des voisins du noeud courant non traité
        list_noeud_traite = []  # Liste des noeuds non traités
        la_pile.append(noeud1.id)  # Ajouter le sommet du noeud de départ
        if noeud1 not in self.noeuds or noeud2 not in self.noeuds:  # Permet de vérifier si le noeud1 et 2 appartient au graphe
            return

        node = la_pile[0]  # Récupérer le dernier élément de la liste ie le sommet de la pile
        while la_pile:  # sort de while quand la_pile est vide
            del la_pile[0]  # Supprime le dernier élément de la liste
            if node not in noeud2.successeurs:
                if node not in list_noeud_traite:  # Teste si le sommet a déjà été traité
                    list_noeud_traite.append(node)  # Ajoute à la liste des sommets traité le sommet
                    unvisited = [n for n in noeud1.successeurs if n not in list_noeud_traite]
                    # unvisited contient tous les voisins non-traités du noeud courant
                    for a in unvisited:
                        la_pile.insert(0, a)  # Ajoute les voisins du noeud courant à la_pile
                    node = la_pile[0]  # Contient le dernier sommet de la liste
                for a in self.noeuds:  # Parcourt du graphe
                    if a.id == node:  # Vérifie si le noeud sommet courant est un sommet du graphe
                        noeud1 = a  # Changer le courant
                        break
            else:
                print("Le chemin parcourit en largeur est:")
                list_noeud_traite.extend([node, noeud2.id])
                print(list_noeud_traite)  # Afficher la liste des sommet traités
                print()
                print()
                return
        print("Pas de chemin existnt")