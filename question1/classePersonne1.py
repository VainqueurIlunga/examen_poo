class Personne:
    def __init__(self, nom_c, prenom_c, age_c):
        self.nom = nom_c
        self.prenom = prenom_c
        self.age= age_c
        
    def afficherInfo(self):
        print(f"je m'appel {self.nom} {self.prenom} et j'ai {self.age} ans")

personne1= Personne("ilunga", "Franck", "15")
personne1.afficherInfo()