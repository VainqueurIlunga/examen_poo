from Etudiant import Etudiant
from cours import Cours
import statistics as st
#from math import mean(data)
class Note:
    
    def __init__(self, etudiant, cours, notes):
    
        Etudiant.nom = etudiant
        Cours.cours = cours
        self.note = notes
        
    def calculMoyenne(self, note1, note2, note3):
        notes=(note1,note2,note3)
        moyenne = st.mean(notes)
        print(f"la moyenne de {Etudiant.nom} est de: {moyenne} dans le cours {self.cours}")
    
    def afficherInfo(self):
        print(f"la note de l'etudiant {Etudiant.nom} dans le cours {Cours.cours} est de : {self.note}")
#t1= Etudiant("ilunga", "franck",15,56)

note1= Note(etudiant="franck", cours="dart",notes=5 )
note1.afficherInfo()