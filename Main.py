

from Models import *
from Functions import *
from os import system







Menu = {
    0: "Enregistrer un nouveau patient",
    1: "consulter et traiter un patient",
    2: "Historique des patients consultés",
    3: "Liste des maladies les plus courants en pédiatrie",
    4: "Liste des patients",
    5: "Etablir le diagnostic sur un patient",
    6: "Rechercher un patient",
    7: "Liste des consultations faites par un patient",
    8: "Liste de tous les consultations",
    9: "Resultats du diagnostic"
}

system("cls")
print("\033[100m"+"==============  PYTHON HEALTH PROJECT  ============="+"\033[0m")
system("pause")
print("................................................................")
system("cls")

print("................................................................")
print("\033[96m"+"==============  BIENVENUE SUR LE MODULE DE LA PEDIATRIE  ============="+"\033[0m")
print("------------------------------------------------------------------------------------------")
print("Notre API dispose des fonctionnalités suivantes :")
print("\n")
for key,value in Menu.items():
    print("\033[94m"+f"{key}- {value} "+"\033[0m")
system("pause")
print("................................................................")

try:
    choix = int(input("Veuillez faire un choix : "))

    while choix:
        if choix not in Menu.keys(): 
            print("------------------------------------------------------------------------------------------")
            print("\033[91m"+"Saisie incorrecte!!!!!!!!!!!!!!"+"\033[0m")
            choix = int(input("Veuillez faire un choix : "))
        else:
            break
except:
    print("------------------------------------------------------------------------------------------")
    print("\033[91m"+"Vous devez saisir un numéro de votre choix!!!!!!!!!!!!!!"+"\033[0m")
    choix = int(input("Veuillez faire un choix : "))


if choix == 0:
    print("\033[93m"+"****************  ENREGISTREMENT D'UN PATIENT  ****************"+"\033[0m")
    system("pause")
    Patient.create()
    reponse = str(input("Voulez-vous enregistrer un autre patient? oui || non :"))
    while reponse :
        if reponse in ["oui", "non"] :
            if reponse == "oui" :
                Patient.create()
                reponse = str(input("Voulez-vous enregistrer un autre patient? oui || non :"))
                continue
            elif reponse == "non":
                break
        else :
            print("\033[91m"+"Vous devez choisir entre oui et non !!!!!!!!!!!!!!"+"\033[0m")
            break

elif choix == 1:
    print("\033[93m"+"****************  CONSULTATION D'UN PATIENT  ****************"+"\033[0m")
    system("pause")
    Patient.consult()
    reponse = str(input("Voulez-vous consulter un autre patient? oui || non :"))
    while reponse :
        if reponse in ["oui", "non"] :
            if reponse == "oui" :
                Patient.consult()
                reponse = str(input("Voulez-vous consulter un autre patient? oui || non :"))
                continue
            elif reponse == "non":
                break
        else :
            print("\033[91m"+"Vous devez choisir entre oui et non !!!!!!!!!!!!!!"+"\033[0m")
            break
elif choix == 2:
    print("\033[93m"+"****************  LISTE DES CONSULTATIONS  ****************"+"\033[0m")
    system("pause")
    Patient.listConsult()
elif choix == 3:
    print("\033[93m"+"****************  LISTE DES MALADIES  ****************"+"\033[0m")
    system("pause")
    Maladie.read()
elif choix == 4:
    print("\033[93m"+"****************  LISTE DES PATIENTS  ****************"+"\033[0m")
    system("pause")
    Patient.read()
elif choix == 5 :
    print("\033[93m"+"****************  ETABLIR LE DIAGNOSTIQUE SUR UN PATIENT  ****************"+"\033[0m")
    system("pause")
    Patient.diagnostic()
elif choix == 6:
    print("\033[93m"+"****************  RECHERCHER D'UN PATIENT  ****************"+"\033[0m")
    system("pause")
    Patient.search()
else:
    print("\033[91m"+"Cas non géré"+"\033[0m")
        







