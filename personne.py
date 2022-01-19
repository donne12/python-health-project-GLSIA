from classes import *

from generator import Generator
from abc import abstractmethod
import json


class Personne:
    id: str
    nom: str
    prenom: str
    tel: str
    adr: str

    def __init__(self):
        g = Generator()
        self.id = g.generate_id_formated()
        self.nom = ''
        self.prenom = ''
        self.tel = ''
        self.adr = ''

    def __str__(self):
        return f"\tID: {self.id} \n\tNom: {self.nom} \n\tPrenom: {self.prenom} \n\tTéléphone: {self.tel} \n\tAdresse: {self.adr}"

    @abstractmethod
    def add(self):
        pass

    def update(self):
        pass

    def get(self):
        pass


class Patient(Personne):
    consultations: []
    def __init__(self):
        super().__init__()
        self.consultation = []

    def __str__(self):
        return f"\tID: {self.id} \n\tNom: {self.nom} \n\tPrenom: {self.prenom} \n\tTéléphone: {self.tel} \n\tAdresse: {self.adr} \n\tConsultations: {self.consultations}"

    # Fonction d'ajout. Elle récupère les données nécessaire puis les enregistre dans le fichier json
    # et utilise la fonction to_class_data()
    def add(self):
        title("Ajouter un patient")
        data = {
            "id": self.id,
            "nom": str(input("Nom :")),
            "prenom": str(input("Prénom :")),
            "tel": str(input("Téléphone :")),
            "adr": str(input("Adresse :")),
            "consultations": []
        }
        self.to_class_data(data)
        write("patients", data)

    # Fonction de modification: Elle récupère l'objet à modifier par son id et demande les données à modifier
    def update(self):
        title("Modifier un patient")
        id = str(input('\n>>> Entrez l\'identifiant: '))

        # Si l'objet a été retrouvé
        if get_element(get("patients"), id) is not None:
            self.to_class_data(get_element(get("patients"), id))

            # Afficher le contenu de l'objet à modifier
            print(self)

            # Modification
            print('Ignorez la saisie des valeurs que vous ne voulez pas modifier')
            data = {
                "id": self.id,
                "nom": str(input("Nouveau Nom :")),
                "prenom": str(input("Nouveau Prénom :")),
                "tel": str(input("Nouveau Téléphone :")),
                "adr": str(input("Nouvelle Adresse :")),
                "consultations": self.consultations
            }

            # Récupération des données de l'objet classe sous le même type que data
            d = {
                "id": self.id,
                "nom": self.nom,
                "prenom": self.prenom,
                "tel": self.tel,
                "adr": self.adr
            }

            # Pour chaque valeur vide lors de la modification, affecter la valeur existante correspondante
            for i in data:
                if not data[i]:
                    data[i] = d[i]

            self.to_class_data(data)

            rewrite("patients", data)

    # Redefinir les valeurs de l'objet classe à partir de data
    def to_class_data(self, data):
        self.id = data["id"]
        self.nom = data["nom"]
        self.prenom = data["prenom"]
        self.tel = data["tel"]
        self.adr = data["adr"]
        self.consultations = data["consultations"]

    # Afficher un objet sélectionné dans un tableau
    def afficher(self):
        title("Un Patient")
        id = str(input('\n>>> Entrez l\'identifiant: '))
        self.to_class_data(get_element(get("patients"), id))
        print(self)
        bar = '+' + '-' * 27 + '+' + '-' * 49 + '+'
        print(bar)
        print('|', 'ID'.center(25), '|', self.id.center(47), '|')
        print(bar)
        print('|', 'Nom'.center(25), '|', self.nom.center(47), '|')
        print(bar)
        print('|', 'Prénom'.center(25), '|', self.prenom.center(47), '|')
        print(bar)
        print('|', 'Téléphone'.center(25), '|', self.tel.center(47), '|')
        print(bar)
        print('|', 'Adresse'.center(25), '|', self.adr.center(47), '|')
        print(bar)
        print('|', 'Consultations'.center(75), '|\n+' + '-' * 77 + '+')

        for i in range(len(self.consultations)):
            print('\nConsultation', i+1, ':\n' + json.dumps(self.consultations[1], indent=2).center(77))

    # Récupérer tous les élements de cette classe
    def get(self):
        read("patients")


class Medecin(Personne):

    def __init__(self):
        super().__init__()

    # Fonction d'ajout. Elle récupère les données nécessaire puis les enregistre dans le fichier json
    # et utilise la fonction to_class_data()
    def add(self):
        title("Ajouter un médecin")
        data = {
            "id": self.id,
            "nom": str(input("Nom :")),
            "prenom": str(input("Prénom :")),
            "tel": str(input("Téléphone :")),
            "adr": str(input("Adresse :"))
        }
        self.to_class_data(data)
        write("medecins", data)

    # Fonction de modification: Elle récupère l'objet à modifier par son id et demande les données à modifier
    def update(self):
        title("Modifier un médecin")
        id = str(input('\n>>> Entrez l\'identifiant: '))

        # Si l'objet a été retrouvé
        if get_element(get("medecins"), id) is not None:
            self.to_class_data(get_element(get("medecins"), id))

            # Afficher le contenu de l'objet à modifier
            print(self)
            print('Ignorez la saisie des valeurs que vous ne voulez pas modifier')

            # Modification
            data = {
                "id": self.id,
                "nom": str(input("Nouveau Nom :")),
                "prenom": str(input("Nouveau Prénom :")),
                "tel": str(input("Nouveau Téléphone :")),
                "adr": str(input("Nouvelle Adresse :"))
            }

            # Récupération des données de l'objet classe sous le même type que data
            d = {
                "id": self.id,
                "nom": self.nom,
                "prenom": self.prenom,
                "tel": self.tel,
                "adr": self.adr
            }

            # Pour chaque valeur vide lors de la modification, affecter la valeur existante correspondante
            for i in data:
                if not data[i]:
                    data[i] = d[i]

            self.to_class_data(data)
            rewrite("medecins", data)

    # Redefinir les valeurs de l'objet classe à partir de data
    def to_class_data(self, data):
        self.id = data["id"]
        self.nom = data["nom"]
        self.prenom = data["prenom"]
        self.tel = data["tel"]
        self.adr = data["adr"]

    # Afficher un objet sélectionné dans un tableau
    def afficher(self):
        title("Afficher un Médecin")
        id = str(input('\n>>> Entrez l\'identifiant: '))

        # Si l'objet a été retrouvé
        if get_element(get("medecins"), id) is not None:
            self.to_class_data(get_element(get("medecins"), id))

            bar = '+' + '-' * 27 + '+' + '-' * 49 + '+'
            print(bar)
            print('|', 'ID'.center(25), '|', self.id.center(47), '|')
            print(bar)
            print('|', 'Nom'.center(25), '|', self.nom.center(47), '|')
            print(bar)
            print('|', 'Prénom'.center(25), '|', self.prenom.center(47), '|')
            print(bar)
            print('|', 'Téléphone'.center(25), '|', self.tel.center(47), '|')
            print(bar)
            print('|', 'Adresse'.center(25), '|', self.adr.center(47), '|')
            print(bar)

    # Récupérer tous les élements de cette classe
    def get(self):
        read("medecins")
