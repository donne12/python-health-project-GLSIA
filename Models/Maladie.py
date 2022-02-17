import sys
sys.path.append(r"C:\pediatrie")
from . import Helpers


class Maladie:
    id : str
    nom: str
    symptomes: list
    departement: str


    # constructeur
    def __init__(self, nom, symptomes, departement):
        self.id  = Helpers.autoIncrement("Maladie.json", 1, "maladie")
        self.nom = nom
        self.symptomes = symptomes
        self.departement = departement

    # 
    def __str__(self):
        return f"id: {self.id} \n nom: {self.nom} \n symptomes: {self.symptomes} \n departement: {self.departement} \n"
    

        




