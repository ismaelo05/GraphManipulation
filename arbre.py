class Arbre:
    id = 0
    parent = None
    enfants = []

    def __init__(self, id1=0, paren=None, enfant=[]):
        self.id = id1
        self.parent = paren
        self.enfants = enfant

    def estFeuille(self):
        if len(self.enfants) == 0:
            return True
        else:
            return False

    def ajouteParent(self, p):
        self.parent = p

    def ajouteEnfant(self, a):
        if a not in self.enfants:
            self.enfants.append(a)

    def nbEnfants(self):
        return len(self.enfants)

    def size(self):
        nombre_noeud = 0
        if self.estFeuille() == False:
            nombre_noeud = nombre_noeud + len(self.enfants) + 1
        elif self.id != 0:
            nombre_noeud = nombre_noeud + 1
        if self.parent != None:
            nombre_noeud = nombre_noeud + 1

        return nombre_noeud

    def compareTo(self, a):
        if self.id > a.id:
            return 1
        elif self.id < a.id:
            return -1
        else:
            return 0



