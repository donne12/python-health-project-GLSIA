from os import system
import os
import sys
sys.path.append(r"C:\pediatrie")
from Models import Patient
from Models.Helpers \
import addNewInPatientStore, loadPatientStore, listToString, editNewInPatientStore, deleteNewInPatientStore, \
addConsultationInPatientStore, addResultatInPatientStore
from prettytable import PrettyTable
import datetime
import win32com.client as win32 # pip install pywin32


date = datetime.datetime.now()

def addPatient() :
    nom = str(input("Entrer le nom du patient :"))
    prenom = str(input("Entrer le prénom du patient :"))
    age = str(input("Entrer l'âge du patient :"))
    adresse = str(input("Entrer l'adresse du patient :"))
    contact = str(input("Entrer le contact du patient :"))
    poids = str(input("Entrer le poids du patient :"))
    taux_glyc = str(input("Entrer le taux de glycémie du patient :"))
    grp_sang = str(input("Entrer le groupe sanguin du patient :"))
    print("................................................................")
    print("Veuillez saisir les symptomes séparés par des virgules!!")
    system("pause")
    symptome = str(input("Entrer les symptomes :"))
    symptomes=symptome.split(",")
    p = Patient.Patient(nom,prenom,age,adresse,contact,poids,taux_glyc, grp_sang, symptomes)
    obj = [
            {
                "id" : p.id,
                "nom" : p.nom,
                "prenom" : p.prenom,
                "age" : p.age,
                "adresse" : p.adresse,
                "contact" : p.contact,
                "poids" : p.poids,
                "taux_glycémie" : p.taux_glycémie,
                "groupe_sanguin" : p.groupe_sanguin,
                "symptomes" : p.symptomes,
                "consultations" : [
                    
                ],
                "resultats" : [
                    
                ]
            }
    ]
    addNewInPatientStore(obj)
    print("\033[92m"+"Patient enregistré avec succès!!"+"\033[0m")


def listPatient() :
    try :
        data = loadPatientStore()
        t = PrettyTable(['Id', 'Nom', 'Prénom', 'age', 'adresse', 'contact', 'poids', 'taux_glyc', 'grp_sang', 'symptomes'])
        for key, value in data.items():
            for s in value :
                t.add_row([s["id"], s["nom"], s["prenom"], s["age"], s["adresse"], s["contact"], s["poids"], s["taux_glycémie"], s["groupe_sanguin"], listToString(s["symptomes"])])
            print(t)
    except :
        print("\033[91m"+"Une erreur s'est produit lors de récupération des données de patient !!!!!!!!!!!!!!"+"\033[0m")


def displayOne() :
    id = int(input("Entrer l'identifiant du patient :"))
    data = loadPatientStore()
    t = PrettyTable(['Id', 'Nom', 'Prénom', 'age', 'adresse', 'contact', 'poids', 'taux_glyc', 'grp_sang', 'symptomes'])
    for key, value in data.items():
        y = next((x for x in value if x["id"] == id), None)
        if not y == None :
             t.add_row([y["id"], y["nom"], y["prenom"], y["age"], y["adresse"], y["contact"], y["poids"], y["taux_glycémie"], y["groupe_sanguin"], listToString(y["symptomes"])])
        else :
            print("\033[91m"+"Aucun patient ayant cet identifiant.. !!!!!!!!!!!!!!"+"\033[0m")
    print(t)


def updateOne() :
    try :
        id = int(input("Entrer l'identifiant du patient :"))
        nom = str(input("Entrer le nom du patient :"))
        prenom = str(input("Entrer le prénom du patient :"))
        age = str(input("Entrer l'âge du patient :"))
        adresse = str(input("Entrer l'adresse du patient :"))
        contact = str(input("Entrer le contact du patient :"))
        poids = str(input("Entrer le poids du patient :"))
        taux_glyc = str(input("Entrer le taux de glycémie du patient :"))
        grp_sang = str(input("Entrer le groupe sanguin du patient :"))
        print("................................................................")
        print("Veuillez saisir les symptomes séparés par des virgules!!")
        system("pause")
        symptome = str(input("Entrer les symptomes :"))
        symptomes=symptome.split(",")
        obj = [
            {
                "nom" : nom,
                "prenom" : prenom,
                "age" : age,
                "adresse" : adresse,
                "contact" : contact,
                "poids" : poids,
                "taux_glycémie" : taux_glyc,
                "groupe_sanguin" : grp_sang,
                "symptomes" : symptomes,
                "consultations" : [
                    
                ],
                "resultats" : [
                    
                ]
            }
        ]
        editNewInPatientStore(obj, id)
    except :
        print("\033[91m"+"Une erreur s'est produit lors de la modification du patient !!!!!!!!!!!!!!"+"\033[0m")


def deleteOne() :
    try :
        id = int(input("Entrer l'identifiant du patient :"))
        deleteNewInPatientStore(id)
    except :
        print("\033[91m"+"Une erreur s'est produit lors de la suppression du patient !!!!!!!!!!!!!!"+"\033[0m")

def consult() :
    try :
        id = int(input("Entrer l'identifiant du patient :"))
        nom_medoc = str(input("Entrer le nom du medecin :"))
        prenom_medoc = str(input("Entrer le prénom du medecin :"))
        contact_medoc = str(input("Entrer le contact du médecin :"))
        obj = [
            {
                "nom_medoc": nom_medoc,
                "prenom_medoc": prenom_medoc,
                "contact": contact_medoc,
                "date_consult": str(date.date())
            }
        ]
        addConsultationInPatientStore(obj, id)
    except :
        print("\033[91m"+"Une erreur s'est produit lors de la consultation du patient !!!!!!!!!!!!!!"+"\033[0m")


def listConsult() :
    id = int(input("Entrer l'identifiant du patient :"))
    data = loadPatientStore()
    t = PrettyTable(['Id', 'Nom', 'Prénom', 'consultations'])
    for key, value in data.items():
        y = next((x for x in value if x["id"] == id), None)
        if not y == None :
            for c in y["consultations"] :
                t.add_row([y["id"], y["nom"], y["prenom"], c])
        else :
            print("\033[91m"+"Aucun patient ayant cet identifiant.. !!!!!!!!!!!!!!"+"\033[0m")
    print(t)


def saveResult() :
    try :
        id = int(input("Entrer l'identifiant du patient :"))
        lib = str(input("Entrer le libelle :"))
        obj = [
            {
                "libelle": lib,
                "date_result": str(date.date())
            }
        ]
        addResultatInPatientStore(obj, id)
    except :
        print("\033[91m"+"Une erreur s'est produit lors de l'enregistrement du resultat !!!!!!!!!!!!!!"+"\033[0m")


def listResult() :
    id = int(input("Entrer l'identifiant du patient :"))
    data = loadPatientStore()
    t = PrettyTable(['Id', 'Nom', 'Prénom', 'resultats'])
    for key, value in data.items():
        y = next((x for x in value if x["id"] == id), None)
        if not y == None :
            for r in y["resultats"] :
                t.add_row([y["id"], y["nom"], y["prenom"], r])
        else :
            print("\033[91m"+"Aucun patient ayant cet identifiant.. !!!!!!!!!!!!!!"+"\033[0m")
    print(t)

def exportData() :
    data = loadPatientStore()
    rows = []

    for key, value in data.items():
        for s in value :
            id = s["id"]
            nom = s["nom"]
            prenom = s["prenom"]
            age = s["age"]
            adresse = s["adresse"]
            poids = s["poids"]
            contact = s["contact"]
            taux = s["taux_glycémie"]
            grp = s["groupe_sanguin"]
            symp = s["symptomes"]
            consultations = s["consultations"]
            resultats = s["resultats"]
            rows.append([id, nom, prenom, age, poids, adresse, contact, taux, grp, symp, consultations, resultats])
    
    ExcelApp = win32.Dispatch('Excel.Application')
    ExcelApp.Visible = True

    wb = ExcelApp.Workbooks.Add()
    ws = wb.Worksheets(1)

    headers = ('id', 'nom', 'prenom', 'age', 'poids', 'adresse', 'contact', 'taux', 'groupe_sang', 'symptomes', 'consultations', 'resultats')
    for i,v in enumerate(headers) :
        ws.Cells(1, i+1).Value = v
    

    row_tracker = 2
    column_size = len(headers)

    for row in rows :
        ws.Range(
            ws.Cells(row_tracker, 1),
            ws.Cells(row_tracker, column_size)
        ).value = row
        row_tracker += 1
    
    wb.SaveAs(os.path.join(os.getcwd(), 'Patients output.xlsx'), 51)
    wb.close()
    ExcelApp.Quit()
    ExcelApp = None

    print("\033[92m"+"Exportation effectuée avec succes!!"+"\033[0m")

