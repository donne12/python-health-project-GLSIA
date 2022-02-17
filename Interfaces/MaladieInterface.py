from os import system
import sys
sys.path.append(r"C:\pediatrie")
from Models import Maladie
from Models.Helpers \
import addNewInMaladieStore, editNewInMaladieStore, loadMaladieStore, listToString, deleteNewInMaladieStore
from prettytable import PrettyTable # pip install prettytable


# ajouter une nouvelle maladie
def addMaladie():
    try :
        nom = str(input("Entrer le nom de la maladie :"))
        departement = str(input("Entrer le département :"))
        print("................................................................")
        print("Veuillez saisir les symptomes séparés par des virgules!!")
        system("pause")
        symptome = str(input("Entrer les symptomes :"))
        symptomes=symptome.split(",")
        m = Maladie.Maladie(nom, symptomes, departement)
        obj = [
            {
                "id" : m.id,
                "nom" : m.nom,
                "symptomes" : m.symptomes,
                "département" : m.departement
            }
        ]
        addNewInMaladieStore(obj)
        print("\033[92m"+"Maladie enregistré avec succès!!"+"\033[0m")
    except :
        print("\033[91m"+"Une erreur s'est produit lors de l'enregistrement de la maladie !!!!!!!!!!!!!!"+"\033[0m")


# liste des maladies
def listMaladie() :
    try :
        data = loadMaladieStore()
        t = PrettyTable(['Id', 'Nom', 'Département', 'Symptômes'])
        for key, value in data.items():
            for s in value :
                t.add_row([s["id"], s["nom"], s["département"], listToString(s["symptomes"])])
            print(t)
    except :
        print("\033[91m"+"Une erreur s'est produit lors de récupération des données de maladie !!!!!!!!!!!!!!"+"\033[0m")
    
    

# afficher les détails d'une maladie
def displayOne() :
    id = int(input("Entrer l'identifiant de la maladie :"))
    data = loadMaladieStore()
    t = PrettyTable(['Id', 'Nom', 'Département', 'Symptômes'])
    for key, value in data.items():
        y = next((x for x in value if x["id"] == id), None)
        if not y == None :
            t.add_row([y["id"], y["nom"], y["département"], listToString(y["symptomes"])])
        else :
            print("\033[91m"+"Aucune maladie ayant cet identifiant.. !!!!!!!!!!!!!!"+"\033[0m")
    print(t)
    

    


# modifier les informations d'une maladie
def updateOne() :
    try :
        id = int(input("Entrer l'identifiant de la maladie :"))
        nom = str(input("Entrer le nom de la maladie :"))
        departement = str(input("Entrer le département :"))
        print("................................................................")
        print("Veuillez saisir les symptomes séparés par des virgules!!")
        system("pause")
        symptome = str(input("Entrer les symptomes :"))
        symptomes=symptome.split(",")
        obj = [
            {
                "nom" : nom,
                "symptomes" : symptomes,
                "département" : departement
            }
        ]
        editNewInMaladieStore(obj, id)
    except :
        print("\033[91m"+"Une erreur s'est produit lors de la modification de la maladie !!!!!!!!!!!!!!"+"\033[0m")


def deleteOne() :
    try :
        id = int(input("Entrer l'identifiant de la maladie :"))
        deleteNewInMaladieStore(id)
    except :
        print("\033[91m"+"Une erreur s'est produit lors de la suppression de la maladie !!!!!!!!!!!!!!"+"\033[0m")

   


