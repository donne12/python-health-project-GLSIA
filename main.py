# patient = Patient('LAWSON-HETCHELY', "Laté Seth", 18, "M")
# patient = patient.ajouterPatient()
# print(patient)
# from controllers.image import Image
# image = Image("png", 80, 50, 'source')
# imagerie = Imagerie('png')
# from datetime import date
# today = date.today()
# # dd/mm/YY
# d1 = today.strftime("%d/%m/%Y")
# print("d1 =", d1)
# print(patient.trouverPatients("UKSB3H2R85"))

from controllers.patient import Patient
from controllers.imagerie import Imagerie
from os import system
from controllers.imagerie import Imagerie
from controllers.image import Image
from controllers.patient import Patient

imagerie = Imagerie()
image = Image()
patient = Patient()

def enregPatient():
    print("*-----------------------------------------------------------------*\n")
    print("*               Entrer les informations du patient                *\n")
    print("*-----------------------------------------------------------------*\n")
    nom = input("Nom du patient : ")
    prenom = input("\nPrenom du patient : ")
    age = input("\nAge du patient : ")
    sexe= input("\nSexe du patient : ")
    print("\nLes données de l'examen du patient : \n")

    patient = Patient(nom, prenom, age, sexe)
    patient.ajouterPatient()

    #print("Les données de l'image prise : \n")
    print("*---------------Données Image--------------------*\n")
    formatImage = input("Le format de l'image :")
    contraste = input("\nLe contraste :")
    luminiosite = input("\nLa luminosite :")
    image = 'source'

    #Ajouter une image
    image = Image(formatImage, contraste, luminiosite, image)
    image.enregistrerImage()

    print("\n*---------------Données Imageries--------------------*\n")
    typeImagerie = input("\nLe type d'imagerie medicale :")
    #numePrise = input("\nNumero de prise :")
    description = input("\nDescription :")
    partieDuCorps = input("\nPartie du corps :")
    etatUrgence = input("\nEtat d'urgence : ")
    
    #Ajouter une nouvelle imagerie 
    imagerie = Imagerie(typeImagerie, description, partieDuCorps, etatUrgence)
    imagerie.nouvelImagerie(patient, image)
    
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
    numeMenu = int(input("1 : Enregistrer un patient \n2 : Afficher les patients\n3 : Rechercher un patient grace a son ID\n4 : La liste des types d'imagerie medicale qui existe\n5 : La liste des images enregistrer\n6 : La liste des examens d'imagerie medicale enregistre (Patients, examens d'imagerie)\n\nMenu : "))

    if numeMenu == 1:
        # Ajouter un patient
        system("cls")
        enregPatient()

    elif numeMenu == 2:
        # Afficher les patients
        print("\nNumero      | nom      | prenom  | age  | sexe \n")
        pats= patient.listePatients()
        for pat in pats["Patients"]:
            print(pat["numero"]," | ", pat["nom"]," | ", pat["prenom"]," | ", pat["age"]," | ", pat["sexe"])
        # print(patient.listePatients())
        print("\n")

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

    elif numeMenu == 5:
        print("\nNumero | fromat | contraste | luminosite | image | date\n")
        imag = image.listeImages()
        for img in imag["Images"]:
            print(img["numero"]," | ", img["format"]," | ", img["contraste"]," | ", img["luminiosite"]," | ", img["image"]," | ", img["date"])

        resp = int(input("\nRetournez au Menu Principal ?? Tapper 1 pour Revenir  2 pour Quitter!! : "))
        if resp == 1: 
            MenuPrincipal()
        elif resp == 2:
            print("\n------------OK !!!------------\n")
            exit

    elif numeMenu == 6:
        print(imagerie.listeImageries())
        resp = int(input("\nRetournez au Menu Principal ?? Tapper 1 pour Revenir  2 pour Quitter!! : "))
        if resp == 1: 
            MenuPrincipal()
        elif resp == 2:
            print("\n------------OK !!!------------\n")
            exit

MenuPrincipal()


