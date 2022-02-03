from os import system, path
from Maladie import *
from Personne import Personne
import json
from datetime import date, datetime
import pandas as pd

def export(data,filename: str):
    try:
        marks_data = pd.DataFrame(data)
        marks_data.to_excel(filename+".xlsx")
        print("Exportation réussie")
    except:
        print("Exportation échouée !")

#Se charge de controler la structure du fichier
def normalisation(fichier: str):
    #Test de l'intégrité du fichier
    try:
        f = open(fichier,"r", encoding="utf8")
        if f.read() == "":
            data = {
                "Patient":[],
                "Maladie":[
                    {
                        "nom": "hyper-ménorrhée",
                        "description": "Troubles de la durée",
                        "traitement": "",
                        "sympto": []
                    },
                    {
                        "nom": "polymenorrhe",
                        "description": "Troubles de la quantité",
                        "traitement": "",
                        "sympto": []
                    },
                    {
                        "nom": "Ménorragie",
                        "description": "Règles longues et abondantes",
                        "traitement": "",
                        "sympto": []
                    },
                    {
                        "nom": "Métrorragie",
                        "description": "Hémorragie en dehors des règles",
                        "traitement": "",
                        "sympto": []
                    },
                    {
                        "nom": "Métroménorragie",
                        "description": "Saignement perpétuel",
                        "traitement": "",
                        "sympto": []
                    },
                    {
                        "nom": "Aménorrhé",
                        "description": "Absence de règles pendant au moins 3 mois en dehors de la grossesse",
                        "traitement": "",
                        "sympto": []
                    },
                    {
                        "nom": "Menopause",
                        "description": "",
                        "traitement": "",
                        "sympto": []
                    },
                    {
                        "nom": "Fibrome",
                        "description": "Tumeur bénigne du muscle utérin",
                        "traitement": "",
                        "sympto": []
                    },
                    {
                        "nom": "Polype",
                        "description": "Excroissance, formation bénigne associée à un risque d'apparition de cancer",
                        "traitement": "",
                        "sympto": []
                    },
                    {
                        "nom": "Aplasie",
                        "description": "Absence d'utérus",
                        "traitement": "",
                        "sympto": []
                    },
                    {
                        "nom": "Cervicite",
                        "description": "Inflammation et infection parasitaire, microbienne ou virale se declarant par les leucorrhées",
                        "traitement": "",
                        "sympto": []
                    },
                    {
                        "nom": "Cancer de l'ovaire",
                        "description": "",
                        "traitement": "",
                        "sympto": []
                    },
                    {
                        "nom": "Cancer du col",
                        "description": "",
                        "traitement": "",
                        "sympto": []
                    },
                    {
                        "nom": "Cancer de l'endomètre",
                        "description": "",
                        "traitement": "",
                        "sympto": []
                    },
                    {
                        "nom": "Cancer du sein",
                        "description": "",
                        "traitement": "",
                        "sympto": []
                    },
                ]
            }
            f.close()
            f = open(fichier, "w",encoding="utf8")
            json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()
    #En cas d'erreur, on restructure le fichier
    except:
        f = open(fichier,"w+",encoding="utf8")
        data = {
            "Patient":[],
            "Maladie":[
                {
                    "nom": "hyper-ménorrhée",
                    "description": "Troubles de la durée",
                    "traitement": "",
                    "sympto": []
                },
                {
                    "nom": "polymenorrhe",
                    "description": "Troubles de la quantité",
                    "traitement": "",
                    "sympto": []
                },
                {
                    "nom": "Ménorragie",
                    "description": "Règles longues et abondantes",
                    "traitement": "",
                    "sympto": []
                },
                {
                    "nom": "Métrorragie",
                    "description": "Hémorragie en dehors des règles",
                    "traitement": "",
                    "sympto": []
                },
                {
                    "nom": "Métroménorragie",
                    "description": "Saignement perpétuel",
                    "traitement": "",
                    "sympto": []
                },
                {
                    "nom": "Aménorrhé",
                    "description": "Absence de règles pendant au moins 3 mois en dehors de la grossesse",
                    "traitement": "",
                    "sympto": []
                },
                {
                    "nom": "Menopause",
                    "description": "",
                    "traitement": "",
                    "sympto": []
                },
                {
                    "nom": "Fibrome",
                    "description": "Tumeur bénigne du muscle utérin",
                    "traitement": "",
                    "sympto": []
                },
                {
                    "nom": "Polype",
                    "description": "Excroissance, formation bénigne associée à un risque d'apparition de cancer",
                    "traitement": "",
                    "sympto": []
                },
                {
                    "nom": "Aplasie",
                    "description": "Absence d'utérus",
                    "traitement": "",
                    "sympto": []
                },
                {
                    "nom": "Cervicite",
                    "description": "Inflammation et infection parasitaire, microbienne ou virale se declarant par les leucorrhées",
                    "traitement": "",
                    "sympto": []
                },
                {
                    "nom": "Cancer de l'ovaire",
                    "description": "",
                    "traitement": "",
                    "sympto": []
                },
                {
                    "nom": "Cancer du col",
                    "description": "",
                    "traitement": "",
                    "sympto": []
                },
                {
                    "nom": "Cancer de l'endomètre",
                    "description": "",
                    "traitement": "",
                    "sympto": []
                },
                {
                    "nom": "Cancer du sein",
                    "description": "",
                    "traitement": "",
                    "sympto": []
                },
            ]
        }
        f.close()

#Se charge d'écrire dans le fichier
def ecrire(fichier: str, data):
    normalisation(fichier)
    rollback = lire("fichier.json")
    f = open(fichier, "w", encoding="utf8")
    try:
        json.dump(data, f,indent=4,ensure_ascii=False)
    except:
        print("Une erreur d'entrer de données est survenue")
        json.dump(rollback, f,indent=4,ensure_ascii=False)
    f.close()

#Charger les données du fichier
def lire(fichier: str):
    normalisation(fichier)
    f = open(fichier, "r", encoding="utf8")
    data = json.load(f)
    f.close()
    return data

#Se charge de recupérer les reponses en booléen
def verifier(critere: str="n"):
    if critere[0].lower() == "o":
        return True
    return False

#Fait le contraire de "verifier()"
def verify(etat):
    if isinstance(etat, str):
        return etat
    if etat:
        return "Oui"
    return "Non"

#La classe Patient, qui contient tout ce qui peut se faire sur les patients
class Patient(Personne):
    #Le constructeur
    def __init__(self, nom: str, prenom: str, adresse: str, age: int, zone: str, consultations = [], pathologies = [], numero: int=0):
        Personne.__init__(Patient,nom,prenom, adresse,age)
        self.zone = zone
        self.consultations = consultations
        self.pathologies = pathologies
        if (numero == 0):
            data = lire("fichier.json")
            if len(data["Patient"]) == 0:
                self.numero = 1
            else:
                self.numero = data["Patient"][-1]["numero"]+1
        else:
            self.numero = numero
    
    #Supprimer le patient de la base
    def delete(self):
        data = lire("fichier.json")
        del data["Patient"][
            data["Patient"].index({
                "numero": self.numero,
                "nom": self.nom,
                "prenom": self.prenom,
                "adresse": self.adresse,
                "zone": self.zone,
                "age": self.age,
                "consultations": self.consultations,
                "pathologies": self.pathologies
            })
        ]
        ecrire("fichier.json", data)
        print("Patient supprimer avec succes !")
    
    def  __str__(self):
        return str(self.numero) + " " +super().__str__() + " " + str(self.zone)+ " "+", ".join(self.pathologies)

    def consulter(self):
        print("Faisons une consultation pour {} {}...".format(self.nom, self.prenom))
        print("-----------------------------\n")
        consul = {}
        consul["douleur"] = verifier(input("Douleur[O/N]: "))
        consul["polype"] = verifier(input("Poype[O/N]: "))
        consul["lesion_cervicale"] = verifier(input("Lesion_cevicale[O/N]: "))
        consul["leucorrhe"] = verifier(input("Leucorrhe[O/N]: "))
        consul["date"] = str(datetime.today())
        if(verifier(input("Avez vous d'autres criteres observés ?[O/N]: "))):
            tred = True
            while tred:
                critere = input("Entrer le critere: ")
                consul[critere] = input("Entrer le resultat constaté: ")
                tred = verifier(input("Avez-vous d'autres criteres ?[O/N]: "))
        
        self.consultations.append(consul)
        self.update()
        print("Consultation fait :-)")
    
    def listConslutation(self, list: str = "n"):
        if list.lower() == "o":
            consultation = {}
            for consultation in self.consultations:
                print("------------------------------")
                for critere in consultation:
                    print(critere,": ",consultation[critere])
                print("------------------------------")
        else:
            print("------------------------------")
            for critere in self.consultations[-1]:
                print(critere,": ",self.consultations[-1][critere])
            print("------------------------------")            

    def calculDeProbabilite(self):
        maladies :list(Maladie) = lire("fichier.json")["Maladie"]
        for index, consultation in self.consultations[-1].items():
            if isinstance(consultation, bool):
                if consultation is True:
                    for maladie in maladies:
                        for sympto in maladie["sympto"]:
                            if index == sympto:
                                print(maladie["nom"], end=", ")
        print()

    def diagnostic(self, maladie: Maladie):
        if maladie is not None:
            if maladie.nom not in self.pathologies:
                self.pathologies.append(maladie.nom)
                self.update()

    #Enregistrer le patient dans la base de données
    def create(self):
        data = lire("fichier.json")
        data["Patient"].append(
            {
                "numero": self.numero,
                "nom" : self.nom,
                "prenom" : self.prenom,
                "adresse" : self.adresse,
                "zone" : self.zone,
                "age" : self.age,
                "consultations": [],
                "pathologies": []
            }
        )
        
        ecrire("fichier.json",data)
    
    #Retrouver le patient par son nom pour une modification
    def find(numero: int):
        data = lire("fichier.json")
        for patient in data["Patient"]:
            if numero == patient["numero"]:
                numero = patient["numero"]
                nom = patient["nom"]
                prenom = patient["prenom"]
                adresse = patient["adresse"]
                zone = patient["zone"]
                age = patient["age"]
                consultations = patient["consultations"]
                pathologies = patient["pathologies"]
                return Patient(nom, prenom, adresse, age, zone, consultations, pathologies, numero)
        return None

    #Mettre à jour le patient dans la base de données
    def update(self):
        data = lire("fichier.json")
        data["Patient"][
            data["Patient"].index({
                "numero": Patient.find(self.numero).numero,
                "nom": Patient.find(self.numero).nom,
                "prenom": Patient.find(self.numero).prenom,
                "adresse": Patient.find(self.numero).adresse,
                "zone": Patient.find(self.numero).zone,
                "age": Patient.find(self.numero).age,
                "consultations": Patient.find(self.numero).consultations,
                "pathologies": Patient.find(self.numero).pathologies
            })
        ] = {
            "numero": self.numero,
            "nom": self.nom,
            "prenom": self.prenom,
            "adresse": self.adresse,
            "zone": self.zone,
            "age": self.age,
            "consultations": self.consultations,
            "pathologies": self.pathologies
        }
        ecrire("fichier.json",data)

    #Rechercher un patient par son nom et prenom
    def search(recherche: str=''):
        data = lire("fichier.json")
        for patient in data["Patient"]:
            p = Patient.find(patient["numero"])
            if (recherche.lower() in p.nom.lower()) or (recherche.lower() in p.prenom.lower()):
                print(p)

#rechercher une consultation en entrant la date ou un intervalle de dates
    def listDateConsultation(self,dates: str, intervalle: bool):
        if not intervalle:
            try:
                ant = dates.split("-")
                dateConsultation = date(int(ant[0]), int(ant[1]), int(ant[2]))
            except:
                print("Erreur - Code -8")
                system("pause")
                return
            trouve = False
            print("\n\t------------------ Consultation du %s -------------------" % str(dateConsultation))
            for consultation in self.consultations:
                if str(dateConsultation) in consultation["date"]:
                    trouve = True
                    for critere, resultat in consultation.items():
                        print(critere, " : ", verify(resultat))
            if not trouve:
                print("Pas de consultation trouvée à cette date pour ce patient")
            print("\t--------------------------------------------------------------------------")
        else:
            datedebut, datefin = dates.split("&")
            try:
                ant = datedebut.split("-")
                spide = datefin.split("-")
                datedebut = date(int(ant[0]), int(ant[1]), int(ant[2]))
                datefin = date(int(spide[0]), int(spide[1]), int(spide[2]))
                iteration = pd.date_range(datedebut,datefin)
            except:
                print("Erreur - Code -8")
                system("pause")
                return
            trouve = False
            print("\n\t------------------ Consultation du %s -------------------" % (str(datedebut)+" au "+ str(datefin)))
            for consultation in self.consultations:
                for dateConsultation in iteration.to_pydatetime():
                    if str(dateConsultation.date()) in consultation["date"]:
                        trouve = True
                        for critere, resultat in consultation.items():
                            print(critere, " : ", verify(resultat))
                        print()
            if not trouve:
                print("Pas de consultation trouvée à cette date pour ce patient")
            print("\t--------------------------------------------------------------------------")

    #Lister les patients
    def toList():
        data = lire("fichier.json")
        print("\n--------------------Liste des patients-------------------------")
        if len(data["Patient"]) > 0:
            for patient in data["Patient"]:
                print(Patient.find(patient["numero"]))
        else:
            print("Pas de patient enregisté !")
        print("-----------------------------------------------------------------\n")

    def importExcel(filename):
        colonne = []
        for col in lire("fichier.json")["Patient"][-1]:
            colonne.append(col)
        try:
            data = pd.read_excel(filename, "Feuil1")
            donne = pd.DataFrame(data,columns=colonne)
            t = lire("fichier.json")
            for i in donne.index:
                if not Patient.exist(
                    {
                        "nom": donne["nom"][i],
                        "prenom": donne["prenom"][i],
                        "adresse": donne["adresse"][i],
                        "zone": donne["zone"][i],
                        "age": int(donne["age"][i]),
                        "consultations": [],
                        "pathologies": []
                    }
                ):
                    t["Patient"].append(
                        {
                            "numero": lire("fichier.json")["Patient"][-1]["numero"]+1,
                            "nom": donne["nom"][i],
                            "prenom": donne["prenom"][i],
                            "adresse": donne["adresse"][i],
                            "zone": donne["zone"][i],
                            "age": int(donne["age"][i]),
                            "consultations": [],
                            "pathologies": []
                        }
                    )
                    ecrire("fichier.json", t)
                    patient = Patient.find(lire("fichier.json")["Patient"][-1]["numero"])
                    cons = pd.DataFrame(pd.read_excel(filename, "Feuil2"), columns=["numero","douleur","polype","lesion_cervicale","leucorrhe","date"])
                    for j in cons.index:
                        if cons["numero"][j] == donne["numero"][i]:
                            patient.consultations.append(
                                {
                                    "douleur": verifier(cons["douleur"][j]),
                                    "polype": verifier(cons["polype"][j]),
                                    "lesion_cervicale": verifier(cons["lesion_cervicale"][j]),
                                    "leucorrhe": verifier(cons["leucorrhe"][j]),
                                    "date": str(cons["date"][j])
                                }
                            )
                    patient.update()
            
            ecrire("fichier.json", t)
            print("Importation réussie")
        except:
            print("Importation échouée !")

#verifie si la personne existe deja ou pas afin d*ajouter ou pas
    def exist(value):
        data = lire("fichier.json")["Patient"]
        for p in data:
            if (p["nom"] == value["nom"]) and (p["prenom"] == value["prenom"]) \
                and (p["adresse"] == value["adresse"]) and (p["zone"] == value["zone"])\
                    and (p["age"] == value["age"]) and (p["consultations"] == value["consultations"])\
                        and (p["pathologies"] == value["pathologies"]):
                return True
        return False

    def importation(filename):
        try:
            f = open(filename, "r", encoding="utf8")
            data_in = json.load(f)
            f.close()
            data = lire("fichier.json")
            rollback = lire("fichier.json")
            
            for patient in data_in:
                if not Patient.exist(patient):
                    data["Patient"].append(
                        {
                            "numero": data["Patient"][-1]["numero"]+1,
                            "nom": patient["nom"],
                            "prenom": patient["prenom"],
                            "adresse": patient["adresse"],
                            "zone": patient["zone"],
                            "age": patient["age"],
                            "consultations": patient["consultations"],
                            "pathologies": patient["pathologies"]
                        }
                    )
            print("Importation effectuée avec succes ...")
        except:
            data = rollback
            print("Erreur survenue lors de l'importation")
        ecrire("fichier.json", data)

    #Les options avancées des patients
    def advanced():
        if authentication():
            while True:
                system("cls")
                print("++++++++++++++ Option avancée des patients ++++++++++++++++")
                print("\t1- Modifier les informations d'un patient")
                print("\t2- Supprimer un patient !")
                print("\t3- Faire une consultation à un patient déjà inscrit")
                print("\t4- Faire un nouveau diagnostic à un patient")
                print("\t5- Lister les consultations d'un patient")
                print("\t6- Voir une consultation d'un patient")
                print("\t7- Fiche siganlitique d'un patient")
                print("\t8- Importer des données en json sur des patients")
                print("\t9- Exporter des données en json sur des patients")
                print("\t10- Importer des patients en Excel")
                print("\t0- Revenir au menu principal")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                choix = input("Faites votre choix: ")
                while choix not in ("0","1","2","3","4","5","6","7","8","9","10"):
                    system("cls")
                    print("Erreur - Saisie incorrect !")
                    system("pause")
                    system("cls")
                    print("++++++++++++++ Option avancée des patients ++++++++++++++++")
                    print("\t1- Modifier les informations d'un patient")
                    print("\t2- Supprimer un patient !")
                    print("\t3- Faire une consultation à un client déjà inscrit")
                    print("\t4- Faire un nouveau diagnostic à un patient")
                    print("\t5- Lister les consultations d'un patient")
                    print("\t6- Voir une consultation prise d'un patient")
                    print("\t7- Fiche siganlitique d'un patient")
                    print("\t8- Importer des données en json sur des patients")
                    print("\t9- Exporter des données en json sur des patients")
                    print("\t10- Importer des patients en Excel")
                    print("\t0- Revenir au menu principal")
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    choix = input("Faites votre choix: ")
                if choix == "1":
                    Patient.toList()
                    if verifier(input("Un peu d'aide pour trouver le patient ?[O/N]: ")):
                        print("Faisons une recherche....\n")
                        recherche = input("Recherche: ")
                        Patient.search(recherche)
                    try:
                        patient = Patient.find(int(input("Entrer le numero du patient: ")))
                    except:
                        print("Entrer invalide -- Retour aux options")
                        system("pause")
                        continue
                    if patient is None:
                        print("Patient introuvable, reéssayez !")
                        continue
                    try:
                        if verifier(input("Voulez-vous changer le nom ?[O/N]: ")):
                            patient.nom = input("Entrer le nouveau nom: ")
                        if verifier(input("Voulez-vous changer le prenom ?[O/N]: ")):
                            patient.prenom = input("Entrer le nouveau prenom: ")
                        if verifier(input("Voulez-vous changer l'adresse ?[O/N]: ")):
                            patient.adresse = input("Entrer la nouvelle adresse: ")
                        if verifier(input("Voulez-vous changer l'âge ?[O/N]: ")):
                            patient.age = int(input("Entrer la nouvelle age: "))
                        if verifier(input("Voulez-vous changer la zone ?[O/N]: ")):
                            patient.zone = input("Entrer le nouvelle zone: ")
                        patient.update()
                    except:
                        print("Erreur survenue lors de la mise à jour -- Retour aux options")
                        system("pause")
                        continue
                    system("pause")
                elif choix == "2":
                    Patient.toList()
                    if verifier(input("Un peu d'aide pour trouver le patient ?[O/N]: ")):
                        print("Faisons une recherche....\n")
                        recherche = input("Recherche: ")
                        Patient.search(recherche)
                    try:
                        patient = Patient.find(int(input("Entrer le numero du patient: ")))
                        patient.delete()
                    except:
                        print("Entrer invalide -- Retour aux options")
                        system("pause")
                        continue
                    if patient is None:
                        print("Patient introuvable, reéssayez !")
                        continue
                    system("pause")
                elif choix == "3":
                    Patient.toList()
                    if verifier(input("Un peu d'aide pour trouver le patient ?[O/N]: ")):
                        print("Faisons une recherche....\n")
                        recherche = input("Recherche: ")
                        Patient.search(recherche)
                    try:
                        patient = Patient.find(int(input("Entrer le numero du patient: ")))
                    except:
                        print("Entrer invalide -- Retour aux options")
                        system("pause")
                        continue
                    if patient is None:
                        print("Patient introuvable, reéssayez !")
                        continue
                    patient.consulter()
                    system("pause")
                elif choix == "4":
                    Patient.toList()
                    if verifier(input("Un peu d'aide pour trouver le patient ?[O/N]: ")):
                        print("Faisons une recherche....\n")
                        recherche = input("Recherche: ")
                        Patient.search(recherche)
                    try:
                        patient = Patient.find(int(input("Entrer le numero du patient: ")))
                    except:
                        print("Entrer invalide -- Retour aux options")
                        system("pause")
                        continue
                    if patient is None:
                        print("Patient introuvable, reéssayez !")
                        continue
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
                elif choix == "5":
                    Patient.toList()
                    if verifier(input("Un peu d'aide pour trouver le patient ?[O/N]: ")):
                        print("Faisons une recherche....\n")
                        recherche = input("Recherche: ")
                        Patient.search(recherche)
                    try:
                        patient = Patient.find(int(input("Entrer le numero du patient: ")))
                    except:
                        print("Entrer invalide -- Retour aux options")
                        system("pause")
                        continue
                    if patient is None:
                        print("Patient introuvable, reéssayez !")
                        continue
                    patient.listConslutation(input("Voulez-vous tout lister ou la dernière ?[O/N]: "))
                    system("pause")
                elif choix == "6":
                    Patient.toList()
                    if verifier(input("Un peu d'aide pour trouver le patient ?[O/N]: ")):
                        print("Faisons une recherche....\n")
                        recherche = input("Recherche: ")
                        Patient.search(recherche)
                    try:
                        patient = Patient.find(int(input("Entrer le numero du patient: ")))
                    except:
                        print("Entrer invalide -- Retour aux options")
                        system("pause")
                        continue
                    if patient is None:
                        print("Patient introuvable, reéssayez !")
                        continue
                    if not verifier(input("Voulez-vous rechercher par intervalle de date ?[O/N]: ")):
                        dateConsultation = input("Entrer la date de la consultation(YYYY-MM-JJ): ")
                        while "-" not in dateConsultation:
                            print("Erreur - Date invalide")
                            dateConsultation = input("Entrer la date de la consultation(YYYY-MM-JJ): ")
                        patient.listDateConsultation(dateConsultation, False)
                    else:
                        datedebut = input("Entrer la date debut (YYYY-MM-JJ): ")
                        datefin =  input("Entrer la date fin (YYYY-MM-JJ): ")
                        while ("-" not in datedebut) or ("-" not in datefin):
                            print("Erreur - Date invalide")
                            datedebut = input("Entrer la date debut (YYYY-MM-JJ): ")
                            datefin =  input("Entrer la date fin (YYYY-MM-JJ): ")
                        patient.listDateConsultation((datedebut+"&"+datefin), True)
                    system("pause")
                elif choix == "7":
                    pass
                elif choix == "8":
                    system("cls")
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Importation des donnees de patient <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
                    filename = input("Entrer le chemin absolu du fichier: ")
                    if path.exists(filename):
                        Patient.importation(filename)
                    else:
                        print("Introuvable - "+filename)
                    system("pause")
                elif choix == "9":
                    system("cls")
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Exportation des donnees de patient <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
                    chemin = input("Entrer l'emplacement du fichier: ")
                    if path.exists(chemin):
                        fichier = input("Entrer le nom du fichier exporté: ")
                        if fichier.strip() == "":
                            fichier = "Export_Patient"
                        else:
                            fichier = fichier.strip()
                        try:
                            fichier = fichier.removesuffix(".json")+".json"
                            f = open("%s\\%s"%(chemin, fichier), "w+", encoding="utf8")
                            json.dump(lire("fichier.json")["Patient"], f, indent=4, ensure_ascii=False)
                            f.close()
                            print("%s exporté avec succes sur le %s"%(fichier, chemin))
                        except:
                            print("Erreur survenu lors de l'exportation !")
                    else:
                        print("Introuvable - "+chemin)
                    system("pause")
                elif choix == "10":
                    system("cls")
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Importation des donnees de patient en excel <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
                    filename = input("Entrer le chemin absolu du fichier: ")
                    if path.exists(filename):
                        Patient.importExcel(filename)
                    else:
                        print("Introuvable - "+filename)
                    system("pause")
                elif choix == "0":
                    break
        else:
            print("Privilege insuffisant !!! Reessayer.")
            system("pause")