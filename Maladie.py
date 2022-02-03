from genericpath import exists
import json
from os import path, system
from Personne import authentication

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
    #Debut de la transaction
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

#La classe Maladie, qui contient tout ce qui peut se faire sur les maladies
class Maladie:
    #Le constructeur
    def __init__(self, nom: str, description: str,sympto: list, traitement: str):
        self.nom = nom
        self.description = description
        self.traitement = traitement
        self.sympto = sympto

    def __str__(self):
        return "Nom: {0}\nDescription: {1}\nSymptôme: {2}\nTraitement: {3}\n".format(self.nom, self.description, ", ".join(self.sympto) ,self.traitement)

    #Supprimer la maladie de la base
    def delete(self):
        data = lire("fichier.json")
        del data["Maladie"][
            data["Maladie"].index({
                "nom" : self.nom,
                "description" : self.description,
                "traitement" : self.traitement,
                "sympto": self.sympto
            })
        ]
        ecrire("fichier.json",data)
        print("Maladie supprimer avec succes !")

    #Enregistrer la maladie dans la base de données
    def create(self):
        data = lire("fichier.json")
        tr = False
        for maladie in data["Maladie"]:
            if maladie["nom"] == self.nom:
                tr = True
        if not tr:
            data["Maladie"].append(
                {
                    "nom" : self.nom,
                    "description" : self.description,
                    "traitement" : self.traitement,
                    "sympto": self.sympto
                }
            )
            ecrire("fichier.json",data)

    #Retrouver une maladie par son nom pour modifier
    def find(name: str):
        data = lire("fichier.json")
        for maladie in data["Maladie"]:
            if name.lower() == maladie["nom"].lower():
                nom = maladie["nom"]
                description = maladie["description"]
                sympto = maladie["sympto"]
                traitement = maladie["traitement"]
                return Maladie(nom,description,sympto,traitement)
        return None

    #Mettre à jour la maladie dans la base de données
    def update(self, nom: str, description: str, traitement: str,sympto: list):
        data = lire("fichier.json")
        data["Maladie"][
            data["Maladie"].index({
                "nom" : self.nom,
                "description" : self.description,
                "traitement" : self.traitement,
                "sympto": self.sympto
            })
        ] = {
            "nom" : nom,
            "description" : description,
            "traitement" : traitement,
            "sympto": sympto
        }
        ecrire("fichier.json",data)

    #Rechercher une maladie par son nom
    def search(recherche: str=''):
        data = lire("fichier.json")
        for maladie in data["Maladie"]:
            m = Maladie.find(maladie["nom"])
            if recherche.lower() in m.nom.lower():
                print(m)

    #Lister les maladies
    def toList():
        data = lire("fichier.json")
        print("\n--------------------Liste des maladies-------------------------")
        if len(data["Maladie"]) > 0:
            for maladie in data["Maladie"]:
                print(Maladie.find(maladie["nom"]))
        else:
            print("Pas de maladie enregisté !")
        print("-----------------------------------------------------------------\n")
    
    #pour importation ou exportation
    def exist(value):
        data = lire("fichier.json")["Maladie"]
        for m in data:
            if (m["nom"] == value["nom"]) and (m["description"] == value["description"]) \
                and (m["traitement"] == value["traitement"]) and (m["sympto"] == value["sympto"]):
                return True
        return False

    def importation(filename):
        try:
            f = open(filename, "r", encoding="utf8")
            data_in = json.load(f)
            f.close()
            data = lire("fichier.json")
            rollback = lire("fichier.json")
            
            for maladie in data_in:
                if not Maladie.exist(maladie):
                    data["Maladie"].append(
                        {
                            "nom": maladie["nom"],
                            "description": maladie["description"],
                            "traitement": maladie["traitement"],
                            "sympto": maladie["sympto"]
                        }
                    )
            print("Importation effectuée avec succes ...")
        except:
            data = rollback
            print("Erreur survenue lors de l'importation")
        ecrire("fichier.json", data)

    #Les options avancées des maladies
    def advanced():
        if authentication():
            while True:
                system("cls")
                print("++++++++++++++ Option avancée des maladies ++++++++++++++++")
                print("\t1- Modifier les informations d'une maladie")
                print("\t2- Supprimer une maladie !")
                print("\t3- Importer des données en json sur des maladies")
                print("\t4- Exporter des données en json sur des maladies")
                print("\t0- Revenir au menu principal")
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                choix = input("Faites votre choix: ")
                while choix not in ("0","1","2","3","4"):
                    system("cls")
                    print("Erreur - Saisie incorrect !")
                    system("pause")
                    system("cls")
                    print("++++++++++++++ Option avancée des maladies ++++++++++++++++")
                    print("\t1- Modifier les informations d'une maladie")
                    print("\t2- Supprimer une maladie !")
                    print("\t3- Importer des données en json sur des patients")
                    print("\t4- Exporter des données en json sur des patients")
                    print("\t0- Revenir au menu principal")
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    choix = input("Faites votre choix: ")
                if choix == "1":
                    Maladie.toList()
                    if verifier(input("Un peu d'aide pour trouver la maladie ?[O/N]: ")):
                        print("Faisons une recherche....\n")
                        recherche = input("Recherche: ")
                        Maladie.search(recherche)
                    try:
                        maladie = Maladie.find(input("Entrer le nom de la maladie: "))
                    except:
                        print("Entrer invalide -- Retour aux options")
                        system("pause")
                        continue
                    if maladie is None:
                        print("Maladie introuvable, reéssayez !")
                        continue
                    try:
                        if verifier(input("Voulez-vous changer le nom ?[O/N]: ")):
                            nom = input("Entrer le nouveau nom: ")
                        if verifier(input("Voulez-vous changer la description ?[O/N]: ")):
                            description = input("Entrer le nouveau prenom: ")
                        if verifier(input("Voulez-vous changer l'adresse ?[O/N]: ")):
                            sympto = input("Entrer la nouvelle liste des symptomes avec ',' pour les séparer: ").split(",")
                        if verifier(input("Voulez-vous changer l'âge ?[O/N]: ")):
                            traitement = input("Entrer le nouveau traitement: ")
                        maladie.update(nom, description, sympto, traitement)
                    except:
                        print("Erreur survenue lors de la mise à jour -- Retour aux options")
                        system("pause")
                        continue
                    system("pause")
                if choix == "2":
                    Maladie.toList()
                    if verifier(input("Un peu d'aide pour trouver la maladie ?[O/N]: ")):
                        print("Faisons une recherche....\n")
                        recherche = input("Recherche: ")
                        Maladie.search(recherche)
                    try:
                        maladie = Maladie.find(input("Entrer le nom de la maladie: "))
                    except:
                        print("Entrer invalide -- Retour aux options")
                        system("pause")
                        continue
                    if maladie is not None:
                        maladie.delete()
                    system("pause")
                elif choix == "3":
                    system("cls")
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Importation des donnees de maladie <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
                    filename = input("Entrer le chemin absolu du fichier: ")
                    if path.exists(filename):
                        Maladie.importation(filename)
                    else:
                        print("Introuvable - "+filename)
                    system("pause")
                elif choix == "4":
                    system("cls")
                    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Exportation des donnees de maladie <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
                    chemin = input("Entrer l'emplacement du fichier: ")
                    if path.exists(chemin):
                        fichier = input("Entrer le nom du fichier exporté: ")
                        if fichier.strip() == "":
                            fichier = "Export_Maladie"
                        else:
                            fichier = fichier.strip()
                        try:
                            fichier = fichier.removesuffix(".json")+".json"
                            f = open("%s\\%s"%(chemin, fichier), "w+", encoding="utf8")
                            json.dump(lire("fichier.json")["Maladie"], f, indent=4, ensure_ascii=False)
                            f.close()
                            print("%s exporté avec succes sur le %s"%(fichier, chemin))
                        except:
                            print("Erreur survenu lors de l'exportation !")
                    else:
                        print("Introuvable - "+chemin)
                    system("pause")
                elif choix == "0":
                    break
        else:
            print("Privilege insuffisant !!! Reessayer.")
            system("pause")