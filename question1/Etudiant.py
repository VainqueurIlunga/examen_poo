import classePersonne1



class Etudiant(classePersonne1.Personne):
    
    def __init__(self, nom_c, prenom_c, age_c, num_etud_c):
        super().__init__(nom_c, prenom_c, age_c)
        self.num_etud= num_etud_c
        self.cote= []
    
    def afficherInfo(self):
        print(f"je m'appel {self.nom} {self.prenom} et j'ai {self.age} ans, mon numero etudiant est {self.num_etud}")

etudiant1= Etudiant("Vainqueer","Franck",15,452)
etudiant1.afficherInfo()