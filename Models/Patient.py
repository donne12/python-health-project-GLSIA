import sys
sys.path.append(r"C:\pediatrie")
from . import Helpers

class Patient :
    id: str
    nom: str
    prenom: str
    age: int
    adresse: str
    contact: str
    poids: float
    taux_glycémie: float
    groupe_sanguin: str
    symptomes: list


    def __init__(self, nom, prenom, age, adresse, contact,poids, taux_glycémie, groupe_sanguin, symptomes):
        self.id  = Helpers.autoIncrement("Patient.json", 1, "patient")
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse
        self.contact = contact
        self.poids = poids
        self.taux_glycémie = taux_glycémie
        self.groupe_sanguin =groupe_sanguin
        self.symptomes = symptomes
    

    def __str__(self):
        return f"id: {self.id} \n nom: {self.nom} \n prenom: {self.prenom} \n taille: {self.taille} \n poids: {self.poids} \n taux_glycémie: {self.taux_glycémie}\n groupe sanguin: {self.groupe_sanguin} \n symtomes: {self.symptomes}"