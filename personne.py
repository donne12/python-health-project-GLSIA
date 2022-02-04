import datetime

from classes import *

from generator import Generator
from abc import abstractmethod
import json
from maladie import Maladie


class Personne:
    id: int
    nom: str
    prenom: str
    tel: str
    adr: str

    def __init__(self):
        self.id = 0
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
    traitements: []

    def __init__(self):
        super().__init__()
        self.consultation = []

    def __str__(self):
        return f"\tID: {self.id} \n\tNom: {self.nom} \n\tPrenom: {self.prenom} \
        \n\tTéléphone: {self.tel} \n\tAdresse: {self.adr} \n\tTraitements: {self.traitements}"

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
            "traitements": []
        }

        p = get("patients")

        # si la liste de patient n'est pas vide,
        # L'id du nouveau élément est celui du dernier de la liste + 1
        if len(p) != 0:
            data["id"] = p[-1]["id"] + 1

        write("patients", data)

    # Ajouter un traitement
    def add_traitement(self):
        title("Ajouter un traitement à un patient")

        # Récupérer la maladie
        data = read("maladies")
        find = str(input('La maladie existe? o/n: '))
        maladie = None
        if find == 'n':
            maladie = Maladie()
            maladie.add()
        else:
            while maladie is None:
                id = int(input('\n>>> L\'identifiant du maladie: '))
                maladie = Maladie()
                maladie.to_class_data(get_element(data, id))

        id = int(input('\n>>> Entrez l\'identifiant du patient: '))
        # Si le patient a été retrouvé
        if get_element(get("patients"), id) is not None:
            self.to_class_data(get_element(get("patients"), id))

            # Afficher le contenu de l'objet à modifier
            print(self)

            data = {
                "id": len(self.traitements),
                "maladie": maladie.nom,
                "debut": str(datetime.datetime.now().date()),
                "Fin": "",
                "Reussi": "",
                "consultations": []
            }

            # Si la liste de traitements n'est pas vide,
            # L'id du nouveau élément est celui du dernier de la liste + 1
            if data["id"] != 0:
                data["id"] = self.traitements[-1]["id"] + 1

            self.traitements.append(data)
            self.write_traitement()
        else:
            print("Elément non trouvé")

    # Enregistrer un traitement pour un patient dans le fichier json
    def write_traitement(self):
        with open('json/data.json') as myFile:
            file_data = json.load(myFile)

        cpt = 0
        for i in file_data["patients"]:
            if i["id"] == self.id:
                file_data["patients"][cpt]["traitements"] = self.traitements
                break
            cpt += 1

        with open('json/data.json', 'w', encoding='utf-8') as myFile:
            json.dump(file_data, myFile, indent=4)
        myFile.close()
        print('Enregistrement réussi!!!')

    # Enregistrer une consultation pour un patient dans le fichier json
    def add_consultation(self):
        title("Ajouter une consultation à un traitement")

        # Récupérer le médecin
        data = read("medecins")
        find = str(input('Le médecin existe? o/n: '))
        medecin = None
        if find == 'n':
            medecin = Medecin()
            medecin.add()
        else:
            while medecin is None:
                id = int(input('\n>>> L\'identifiant du médecin: '))
                medecin = Medecin()
                medecin.to_class_data(get_element(data, id))

        # Récupérer le patient
        id = int(input('\n>>> L\'identifiant du patient: '))

        # Si l'objet a été retrouvé
        if get_element(get("patients"), id) is not None:
            self.to_class_data(get_element(get("patients"), id))
            print(self)

            id = int(input('\n>>> Entrez l\'identifiant du traitement: '))

            cpt = 0
            for elt in self.traitements:
                if elt["id"] == id:
                    data = {
                        "id": len(elt["consultations"]),
                        "medecin": medecin.nom + ' ' + medecin.prenom,
                        "date consultation": str(datetime.datetime.now().date()),
                        "observations": str(input("Observations (séparez avec des virgules): ")).split(','),
                        "prescriptions": str(input("Prescriptions (séparez avec des virgules): ")).split(','),
                        "rdv": str(input("Prochain RDV (2022-10-28): "))
                    }


                    # Vérifier s'il y a une date de RDV
                    # si oui, vérifier la date entrée est supérieur à la date d'aujourd'hui
                    if data["rdv"] != "":
                        rdv = data["rdv"].split('-')
                        data["rdv"] = ""
                        while data["rdv"] == "":
                            if len(rdv) != 3:
                                print('Veuillez entrer une date valide')
                                rdv = str(input("Prochain RDV (2022-10-28): ")).split('-')
                            else:
                                for i in rdv:
                                    if not i.isdigit():
                                        rdv = []
                                        break
                                if rdv:
                                    t = datetime.datetime(int(rdv[0]), int(rdv[1]), int(rdv[2]))
                                    if t < datetime.datetime.now():
                                        print("La date de RDV doit être une date après aujourd'hui")
                                        rdv = str(input("Prochain RDV (2022-10-28): ")).split('-')
                                    else:
                                        for i in rdv:
                                            data["rdv"] += i

                    # si la liste de consultation n'est pas vide,
                    # L'id du nouveau élément est celui du dernier de la liste + 1
                    if data["id"] != 0:
                        data["id"] = elt["consultations"][-1]["id"] + 1

                    self.traitements[cpt]["consultations"].append(data)
                    self.write_traitement()
                    cpt = 0
                    break
                cpt += 1

            if cpt != 0:
                print("Cette consultation n'existe pas")
        else:
            print("Elément non trouvé")

    # Finaliser un traitement pour un patient
    def end_traitement(self):
        title("Finaliser un traitement")

        # Récupérer le patient
        id = int(input('\n>>> L\'identifiant du patient: '))

        # Si l'objet a été retrouvé
        if get_element(get("patients"), id) is not None:
            self.to_class_data(get_element(get("patients"), id))
            print(self)

            id = int(input('\n>>> Entrez l\'identifiant du traitement: '))

            cpt = 0
            for elt in self.traitements:
                if elt["id"] == id:
                    self.traitements[cpt]["Reussi"] = str(input("Traitement réussi? Oui/Non: "))
                    self.traitements[cpt]["Fin"] = str(datetime.datetime.now().date())
                    self.write_traitement()
                    cpt = 0
                    break
                cpt += 1

            if cpt != 0:
                print("Cette consultation n'existe pas")


    # Fonction de modification: Elle récupère l'objet à modifier par son id et demande les données à modifier
    def update(self):
        title("Modifier un patient")
        id = int(input('\n>>> Entrez l\'identifiant: '))

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
                "traitements": self.traitements
            }

            # Récupération des données de l'objet classe sous le même type que data
            d = {
                "id": self.id,
                "nom": self.nom,
                "prenom": self.prenom,
                "tel": self.tel,
                "adr": self.adr,
                "traitements": self.traitements
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
        self.traitements = data["traitements"]

    # Afficher un objet sélectionné dans un tableau
    def afficher(self):
        title("Un Patient")
        id = int(input('\n>>> Entrez l\'identifiant: '))
        self.to_class_data(get_element(get("patients"), id))
        print(self)
        print()
        # bar = '+' + '-' * 27 + '+' + '-' * 49 + '+'
        # print(bar)
        # print('|', 'ID'.center(25), '|', str(self.id).center(47), '|')
        # print(bar)
        # print('|', 'Nom'.center(25), '|', self.nom.center(47), '|')
        # print(bar)
        # print('|', 'Prénom'.center(25), '|', self.prenom.center(47), '|')
        # print(bar)
        # print('|', 'Téléphone'.center(25), '|', self.tel.center(47), '|')
        # print(bar)
        # print('|', 'Adresse'.center(25), '|', self.adr.center(47), '|')
        # print(bar)
        # print('|', 'Consultations'.center(75), '|\n+' + '-' * 77 + '+')
        #
        # for i in range(len(self.traitements)):
        #     print('\nConsultation', i + 1, ':\n' + json.dumps(self.traitements[1], indent=2).center(77))

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

        med = get("medecins")

        # si la liste de médecins n'est pas vide,
        # L'id du nouveau élément est celui du dernier de la liste + 1
        if len(med) != 0:
            data["id"] = med[-1]["id"] + 1

        write("medecins", data)

    # Fonction de modification: Elle récupère l'objet à modifier par son id et demande les données à modifier
    def update(self):
        title("Modifier un médecin")
        id = int(input('\n>>> Entrez l\'identifiant: '))

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
        id = int(input('\n>>> Entrez l\'identifiant: '))

        # Si l'objet a été retrouvé
        if get_element(get("medecins"), id) is not None:
            self.to_class_data(get_element(get("medecins"), id))

            bar = '+' + '-' * 27 + '+' + '-' * 49 + '+'
            print(bar)
            print('|', 'ID'.center(25), '|', str(self.id).center(47), '|')
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
