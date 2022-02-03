from Patient import *
from Maladie import *
from os import system

while True:
    system("cls")
    print("Bienvenu sur la plateforme pour le module de la gynécologie")
    print("---------------------------------------------------------")
    print("\t1- Enregistrer patient")
    print("\t2- Liste des patients")
    print("\t3- Enregistrer une maladie")
    print("\t4- Liste des maladies")
    print("\t5- Opérations avancées sur les patients")
    print("\t6- Opérations avancées sur les maladies")
    print("\t0- Quitter")
    print("---------------------------------------------------------\n")
    choix = input("Faite votre choix: ")
    while choix not in ("0","1","2","3","4","5","6"):
        system("cls")
        print("Erreur - Saisie incorrect !")
        system("pause")
        system("cls")
        print("Bienvenu sur la plateforme pour le module de la gynécologie")
        print("---------------------------------------------------------")
        print("\t1- Enregistrer patient")
        print("\t2- Liste des patients")
        print("\t3- Enregistrer une maladie")
        print("\t4- Liste des maladies")
        print("\t5- Opérations avancées sur les patients")
        print("\t6- Opérations avancées sur les maladies")
        print("\t0- Quitter")
        print("---------------------------------------------------------\n")
        choix = input("Faite votre choix: ")
    if choix == "1":
        print("Enregistrons un patient...")
        nom = input("Entrer le nom du patient: ")
        prenom = input("Entrer le prenom du patient: ")
        adresse = input("Entrer l'adresse du patient: ")
        age = int(input("Entrer l'âge du patient: "))
        zone = input("Entrer la zone de residance du patient: ")
        try:
            patient = Patient(nom, prenom, adresse, age, zone)
            patient.create()
        except:
            print("Erreur de creation du patient, veuillez reessayer !!")
            exit(-7)
        print("Patient: {} créé avec succes !\n".format(patient))
        consul = verifier(input("Voulez-vous faire une consultation à ce patient ?[O/N]: "))
        if consul:
            patient.consulter()
            diag = verifier(input("Voulez-vous donner votre diagnostique ?[O/N]: "))
            if diag and authentication():
                print("Les maladies probables: ", end="")
                patient.calculDeProbabilite()
                if not verifier(input("Cela vous a aidez ?[O/N]: ")):
                    Maladie.toList()
                if verifier(input("La maladie est-elle présente dans la liste ?[O/N]: ")):
                    name = input("Entrer le nom de la maladie: ")
                    maladie = Maladie.find(name)
                    if maladie is None:
                        print("Maladie introuvable, reéssayez !")
                        continue
                    patient.diagnostic(maladie)
                    print("Diagnostic terminé avec succes !")
                    continue
                else:
                    print("Enregistrons la maladie...")
                    nom = input("Entrer le nom de la maladie: ")
                    description = input("Entrer la description de la maladie: ")
                    sympto = input("Entrer la liste des symptomes avec ',' pour les séparer: ").split(",")
                    traitement = input("Entrer le traitement de la maladie: ")
                    try:
                        maladie = Maladie(nom, description, sympto, traitement)
                        maladie.create()
                    except:
                        print("Entrer invalide -- Retour aux options")
                        system("pause")
                        continue
                    print("Maladie: {} créée avec succes !\n".format(maladie))
                    patient.diagnostic(maladie)
                    print("Diagnostic terminé avec succes !")
        system("pause")
    elif choix == "2":
        Patient.toList()
        system("pause")
    elif choix == "3":
        print("Enregistrons une maladie...")
        nom = input("Entrer le nom de la maladie: ")
        description = input("Entrer la description de la maladie: ")
        sympto = input("Entrer la liste des symptomes avec ',' pour les séparer: ").split(",")
        traitement = input("Entrer le traitement de la maladie: ")
        try:
            maladie = Maladie(nom, description, sympto, traitement)
            maladie.create()
        except:
            print("Erreur de creation de la maladie, veuillez reessayer !!")
            exit(-7)
        print("Maladie: {} créée avec succes !\n".format(maladie))
        system("pause")
    elif choix == "4":
        Maladie.toList()
        system("pause")
    elif choix == "5":
        Patient.advanced()
    elif choix == "6":
        Maladie.advanced()
    elif choix == "0":
        break;
system("cls")
print("Au revoir !!!!")
system("pause")
