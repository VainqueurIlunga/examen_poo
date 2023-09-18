from enseignant import Enseignat
from Etudiant import Etudiant, etudiant1
import statistics as st
#from math import mean
#from note import Note

class Cours:
    
    def __init__(self, nom_cours, nom_enseignant, etudiant):
        self.cours = nom_cours
        Enseignat.nom= nom_enseignant
        Etudiant.nom = etudiant
        
    
    def calculMoyenne(self, note1, note2, note3):
        notes=(note1,note2,note3)
        moyenne = st.mean(notes)
        print(f"la moyenne de {Etudiant.nom} est de: {moyenne} dans le cours {self.cours}")
    
    def ajouterEtudiant(self):
        print(f"l'etudiant {Etudiant.nom} a ete ajouter au cours {self.cours}")
        

    def ajouterNote(self):
        print(f"la note pour l'etudiant {Etudiant.nom} inscrit au cours {self.cours} à la note {Note.note}")
        

cours1= Cours("python", "Mr Achille",etudiant1.nom)
cours1.calculMoyenne(5,6,8)
#cours1.ajouterEtudiant()
#cours1.ajouterNote()