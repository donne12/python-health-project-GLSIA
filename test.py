from maladie import *
from personne import *
from consultation import *
import os

ma = Maladie()
pa = Patient()
med = Medecin()
con = Consultation()


def mainmenu():
    title("MENU PRINCIPAL")
    print("1- Gestion des maladies")
    print("2- Gestion des médecins")
    print("3- Gestion des patients")
    print("4- Gestion des utilisateurs")
    print()


def menu():
    mainmenu()
    choix = int(input("\nChoisissez une option: "))

    if choix == 1:
        retour = 'o'
        while retour == 'o':
            title("Gestion des maladies")
            print("1- Liste des maladies")
            print("2- Ajouter une maladie")
            print("3- Modifier une maladie")
            print("4- Afficher une maladie")
            print("0- Retour au menu principal")
            choix = int(input("\nChoisissez une option: "))
            if choix == 1:
                read("maladies")
            if choix == 2:
                ma.add()
            if choix == 3:
                ma.update()
            if choix == 4:
                ma.afficher()
            if choix == 0:
                os.system('clear')
                menu()
                break
            retour = str(input("\nRetourner au menu O/N?: "))
    elif choix == 2:
        retour = 'o'
        while retour == 'o':
            title("Gestion des médecins")
            print("1- Liste des médecins")
            print("2- Ajouter un médecin")
            print("3- Modifier un médecin")
            print("4- Afficher un médecin")
            print("0- Retour au menu principal")
            choix = int(input("\nChoisissez une option: "))
            if choix == 1:
                read("medecins")
            if choix == 2:
                med.add()
            if choix == 3:
                med.update()
            if choix == 4:
                med.afficher()
            if choix == 0:
                os.system('clear')
                menu()
                break
            retour = str(input("\nRetourner au menu O/N?: "))
    elif choix == 3:
        retour = 'o'
        while retour == 'o':

            title("Gestion des patients")
            print("1- Liste des patients")
            print("2- Ajouter un patient")
            print("3- Modifier un patient")
            print("4- Afficher un patient")
            print("5- Ajouter une consultation")
            print("0- Retour au menu principal")
            choix = int(input("\nChoisissez une option: "))
            if choix == 1:
                read("patients")
            if choix == 2:
                pa.add()
            if choix == 3:
                pa.update()
            if choix == 4:
                pa.afficher()
            if choix == 5:
                con.add()
            if choix == 0:
                os.system('clear')
                menu()
                break
            retour = str(input("\nRetourner au menu O/N?: "))
    elif choix == 4:
        retour = 'o'
        while retour == 'o':

            title("Gestion des utilisateurs")
            print("1- Liste des utilisateurs")
            print("2- Changer son mot de passe")
            print("3- Ajouter un utilisateur")
            print("0- Retour au menu principal")
            choix = int(input("\nChoisissez une option: "))
            if choix == 1:
                read("users")
            if choix == 2:
                add_user(username, str(input('Nouveau mot de passe: ')))
            if choix == 3:
                add_user({"username": str(input('Nom d''utilisateur: ')), "password": str(input('Mot de passe: '))})
            if choix == 0:
                os.system('clear')
                menu()
                break
            retour = str(input("\nRetourner au menu O/N?: "))

username = str(input('Nom d''utilisateur: '))
password = str(input('Mot de passe: '))
if login(username, password):
    menu()
else:
    print("Identifiants incorrects.")

# with open('json/data.json') as myFile:
#     file_data = json.load(myFile)
#
# ma = Maladie()
# pa = Patient()
# med = Medecin()
# a = ['ftg', "tfgh"]
#
# ma.to_class_data(file_data["maladies"][0])
# pa.to_class_data(file_data["patients"][0])
# med.to_class_data(file_data["medecins"][0])
# pa.update()
# pa.afficher()
# ma.afficher()
# med.afficher()
# #ma.add()
# #read("maladies")
#
# #med = Medecin('','','','')
# con = Consultation()
# #con.to_class_data(file_data["users"][0])
# con.observations = a
# #con.afficher()
# #con.add()
