from cours import Cours

class University:
    
    def __init__(self, cours_c):
        Cours.cours=cours_c
    
    def ajouter_Cours(self):
        print(f"le cours {Cours.cours} à ete ajouter")
        
cour1= Cours("Java", "Mr Hergy",'franck')
ajouter_cours= University(cour1.cours)
ajouter_cours.ajouter_Cours()