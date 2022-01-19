import datetime

from classes import *
from generator import Generator
from abc import abstractmethod
import json


class Maladie:
    id: str
    nom: str
    symptomes: []
    categorie: str

    def __init__(self):
        g = Generator()
        self.id = g.generate_id_formated()
        self.nom = ''
        self.symptomes = []
        self.categorie = ''

    def __str__(self):
        return f"\tID: {self.id} \n\tNom: {self.nom} \n\tSymptomes: {self.symptomes} \n\tType: {self.categorie}"

    # Fonction d'ajout. Elle récupère les données nécessaire puis les enregistre dans le fichier json
    # et utilise la fonction to_class_data()
    def add(self):
        title("Ajouter une maladie")
        data = {
            "id": self.id,
            "nom": str(input("Nom: ")),
            "symptomes": str(input("Les symptômes (séparez avec des virgules): ")).split(','),
            "categorie": str(input("Catégorie: "))
        }

        if data['categorie'] not in ['lesion', 'pathologie']:
            data['categorie'] = str(input("Catégorie (pathologie/lesion):"))

        self.to_class_data(data)
        write("maladies", data)

    # Fonction de modification: Elle récupère l'objet à modifier par son id et demande les données à modifier
    def update(self):
        title("Modifier une maladie")
        id = str(input('\n>>> Entrez l\'identifiant: '))

        # Si l'objet a été retrouvé
        if get_element(get("maladies"), id) is not None:
            self.to_class_data(get_element(get("maladies"), id))

            # Afficher le contenu de l'objet à modifier
            print(self)
            print('Ignorez la saisie des valeurs que vous ne voulez pas modifier')

            # Modification
            data = {
                "id": self.id,
                "nom": str(input("Nouveau Nom :")),
                "symptomes": str(input("Nouvelle liste des symptômes (séparez avec des virgules): ")).split(','),
                "categorie": str(input("Nouvelle catégorie: "))
            }

            # Récupération des données de l'objet classe sous le même type que data
            d = {
                "id": self.id,
                "nom": self.nom,
                "symptomes": self.symptomes,
                "categorie": self.categorie
            }

            # Pour chaque valeur vide lors de la modification, affecter la valeur existante correspondante
            for i in data:
                if not data[i]:
                    data[i] = d[i]

            self.to_class_data(data)
            rewrite("maladies", data)

    # Redefinir les valeurs de l'objet classe à partir de data
    def to_class_data(self, data):
        self.id = data["id"]
        self.nom = data["nom"]
        self.symptomes = data["symptomes"]
        self.categorie = data["categorie"]

    # Afficher un objet sélectionné dans un tableau
    def afficher(self):
        id = str(input('\n>>> Entrez l\'identifiant: '))
        self.to_class_data(get_element(get("maladies"), id))

        title("Une Maladie")
        bar = '+' + '-'*27 + '+' + '-'*49 + '+'
        print(bar)
        print('|', 'ID'.center(25), '|', self.id.center(47), '|')
        print(bar)
        print('|', 'Nom'.center(25), '|', self.nom.center(47), '|')
        print(bar)
        print('|', 'symptômes'.center(25), '|', self.symptomes[0].center(47), '|')
        for elt in range(1, len(self.symptomes)):
            print('|', ''.center(25), '|', self.symptomes[elt].center(47), '|')
        print(bar)
        print('|', 'Catégorie'.center(25), '|', self.categorie.center(47), '|')
        print(bar)

    # Récupérer tous les élements de cette classe
    def get(self):
        read("maladies")




#{"maladies": [{"id": "D9AFd-5ve6v-zpAtk-LdsDu", "nom": "Poux", "symptomes": ["plaies", "rougeurs"], "categorie": "lesion"}, {"id": "E9iPC-eCeSF-rgqyt-hTdEt", "nom": "Acn\u00e9", "symptomes": ["bouttons", "visage huileux"], "categorie": "lesion"}], "medecins": [{"id": "xBib1-xM663-eGCPs-chbuj", "nom": "HIHEA", "prenom": "Ghust", "tel": "91489000", "adr": "K\u00e9gu\u00e9"}, {"id": "PnH9p-AZqz8-vrThg-ttQeD", "nom": "ANALLA", "prenom": "Ace", "tel": "98756233", "adr": "Ago\u00e8"}], "patients": [{"id": "P0l6Z-mPHxZ-K1JTs-JcoW4", "nom": "Tokio", "prenom": "sem", "tel": "79645440", "adr": "Adidogom\u00e9", "consultations": []}]}