import statistics as st
from cours import Cours, etudiant1

class Departement:
    nom="genie logiciel"
    enseignant=""
    
    def ajouter_enseignant( nom_ensei):
        Departement.enseignant = nom_ensei
        enseignant=[]
        enseignant.append(Departement.enseignant)
        print(enseignant)
        print(f"l'enseignat {Departement.enseignant} a ete ajoutee au departement {Departement.nom}")
        
    def calculMoyenne(self, note1, note2, note3):
        notes=(note1,note2,note3)
        moyenne = st.mean(notes)
        print(f"la moyenne de {Etudiant.nom} est de: {moyenne} dans le cours {self.cours}")
        
ense1= Departement.ajouter_enseignant("Mr achille")
ense2= Departement.ajouter_enseignant("Mr hergy")
cour5= Cours("flutter",ense1,etudiant1.nom )
cour5.calculMoyenne(6,8,14)