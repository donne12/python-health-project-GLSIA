#from datetime import date, datetime
from typing import Any
from os import system
#from controllers.imagerie import Imagerie
#from controllers.image import Image
from controllers.patient import Patient

def enregPatient():
    print("*-----------------------------------------------------------------*\n")
    print("*               Entrer les informations du patient                *\n")
    print("*-----------------------------------------------------------------*\n")
    nom = input("Nom du patient : ")
    prenom = input("\nPrenom du patient : ")
    age = input("\nAge du patient : ")
    sexe= input("\nSexe du patient : ")
    print("\nLes données de l'examen du patient : \n")
    print("*---------------Données Imageries--------------------*\n")
    patient = Patient(nom, prenom, age, sexe)
    #patient = Patient(patient.nom, patient.prenom, patient.age, patient.sexe)
    patient.ajouterPatient()

    typeImagerie = input("Le type d'imagerie medicale :")
    numePrise = input("\nNumero de prise :")
    description = input("\nDescription :")
    partieDuCorps = input("\nPartie du corps :")
    etatUrgence = input("\nEtat d'urgence : ")
    datePrise = input("\nDate : ")
    
    #Ajouter une nouvelle imagerie 
    #imagerie = Imagerie(typeImagerie, numePrise, description, partieDuCorps, etatUrgence, datePrise )
    
    print("Les données de l'image prise : \n")
    print("*---------------Données Image--------------------*\n")
    formatImage = input("Le format de l'image :")
    contraste = input("\nLe contraste :")
    luminiosite = input("\nLa luminosite :")
    resolution = input("\nLa resolution :")

    #Ajouter une image
    #Image(formatImage, contraste, luminiosite, resolution)
    
    repsPatient=0
    repsPatient = int(input("\nVoulez-vous enregistrer un autre patient ? : Tapper 1 pour OUI  2 pour NON et 3 Pour revenir au Menu Principal : "))
    if repsPatient == 1:
        enregPatient()
    elif repsPatient == 2:
        print("\n------------OK !!!------------\n")
    elif repsPatient == 3:
        MenuPrincipal()
    
def MenuPrincipal():
    system("cls")
    print("*-----------------------------------------------------------------*\n")
    print("*                         Menu principal                          *\n")
    print("*-----------------------------------------------------------------*\n")

    print("Tapper : \n")
    numeMenu = int(input("1 : pour enregistrer un patient \n2 : pour afficher les patients\n3 : Rechercher un patient grace a son ID\n4 : Liste des types d'imagerie medicale qui existe\n\nMenu : "))

    if numeMenu == 1:
        # Ajouter un patient
        system("cls")
        enregPatient()

    elif numeMenu == 2:
        # Afficher les patients
        print(Patient.listePatients(Any))

    elif numeMenu == 3:
        # Rechercher un patient grace a son ID
        IDPatient = input("\nEntrer l'ID du patient à rechercher : \n\n")
        print("\n", Patient.trouverPatients(IDPatient))
    elif numeMenu == 4:
        print("\n 1  : Artériographie \n 2  : Cœlioscopie \n 3  : Coloscopie\n 4  : Echographie \n 5  : Fibroscopie \n 6  : Fibroscopie_bronchique \n 7  : Fibroscopie_gastrique \n 8  : Hystéroscopie \n 9  : IRM \n 10 : Mammographie \n 11 : Ostéodensitométrie \n 12 : Radiologie \n 13 : Scanner \n")
        resp = int(input("\nRetournez au Menu Principal ?? Tapper 1 pour Revenir  2 pour Quitter!! : "))
        if resp == 1: 
            MenuPrincipal()
        elif resp == 2:
            print("\n------------OK !!!------------\n")
            exit
MenuPrincipal()