import classePersonne1

class Enseignat(classePersonne1.Personne):
    def __init__(self, nom_c, prenom_c, age_c, matiere_enseignee):
        super().__init__(nom_c, prenom_c, age_c)
        self.matiere= matiere_enseignee
    
    def afficherInfo(self):
        print(f"je m'appel {self.nom} {self.prenom} et j'ai {self.age} ans, la matiere enseignée {self.matiere}")

enseignat1 = Enseignat("Mr kabasele", "Achille", 16, "POO avancé avec python")
enseignat1.afficherInfo()