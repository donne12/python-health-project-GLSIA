
from Id_generate import UniqueId
from Functions import *
import bcrypt
import datetime



class Auth:
    username: str
    password : str

    def __init__(self, username, password):
        self.username = username
        self.password = password

    


    def checkUser(self):
        data = loadAuthUsersStore()
        for k, v in data.items():
            for m, n in v.items():
                n["password"].encode('utf-8')
                if n["username"] == self.username and bcrypt.checkpw(self.password, str(n["password"]).encode('utf-8')) :
                    return True
                else :
                    return False
    

    
        



class Personne:
    id: str
    nom: str
    prenom: str
    age: int
    adresse: str
    contact: str

    def __init__(self, nom, prenom, age, adresse, contact):
        g = UniqueId()
        self.id = g.generate_id_formated()
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse
        self.contact = contact



class Patient(Personne):
    id: str
    matricule: str
    poids: float
    taux_glycémie: float
    groupe_sanguin: str
    symptomes: list


    def __init__(self, matricule, nom, prenom, age, adresse, contact, poids, taux_glycémie, groupe_sanguin, symptomes):
        super().__init__(nom, prenom, age, adresse, contact)
        g = UniqueId()
        self.id= g.generate_id_formated()
        self.matricule = matricule
        self.poids = poids
        self.taux_glycémie = taux_glycémie
        self.groupe_sanguin =groupe_sanguin
        self.symptomes = symptomes.split(",")
    

    def __str__(self):
        return f"id: {self.id} \n nom: {self.nom} \n prenom: {self.prenom} \n taille: {self.taille} \n poids: {self.poids} \n taux_glycémie: {self.taux_glycémie}\n groupe sanguin: {self.groupe_sanguin} \n symtomes: {self.symptomes}"


    # afficher la liste des patients
    @classmethod
    def read(self):
       data = loadConsultation()
       
       for key, value in data.items():
           print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________")
           print("nom | prenom | age | adresse | contact | taille | poids | taux_glycemie | groupe_sanguin | symptomes")
           print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
           for x, y in value.items():
                print(y["nom"]," | ",y["prenom"], " | ", y["age"], " | ", y["adresse"], " | ", y["contact"], " | ", y["taille"], " | ", y["poids"], " | ", y["taux_glycémie"], " | ", y["groupe_sanguin"], " | ", listToString(y["symp"]) )
                print("___________________________________________________________________________________________________________________________________________________________________________________________________________________")

        
    # consulter les patients
    def consult(self, nom_medoc, prenom_medoc, contact_medoc) : 
        g = UniqueId()
        code = g.generate_id_formated()
        date = datetime.datetime.now()
        obj = {
            code : {
                "patient" : {
                    "nom" : self.nom,
                    "prenom" : self.prenom,
                    "age" : self.age,
                    "adresse" : self.adresse,
                    "contact" : self.contact,
                    "poids" : self.poids,
                    "taux_glycemie" : self.taux_glycémie,
                    "groupe_sanguin" : self.groupe_sanguin,
                    "symp" : self.symptomes
                },
                "date_consult": date.date,
                "medecin" : {
                    "nom" : nom_medoc,
                    "prenom" : prenom_medoc,
                    "contact" : contact_medoc
                },
                "resultats" : {
                    "libelle" : "",
                    "date_result" : ""
                }
            }
        }
        addNewConsultation(obj)
        return True
    
    # afficher la liste des consultations
    @classmethod
    def listConsult(self):
        data = loadConsultation()

        for key, value in data.items():
           print("__________________________________________________________________________________________________________________________________________________")
           print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PATIENT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|~~~~~~~~~~MEDECIN~~~~~~")
           print("nom | prenom | age | adresse | contact | taille | poids | taux_glycemie | groupe_sanguin | symptomes | nom | prenom | contact | date | traitements")
           print("--------------------------------------------------------------------------------------------------------------------------------------------------")
           for x, y in value.items():
                print(y["patient"]["nom"]," | ",y["patient"]["prenom"], " | ",y["patient"]["age"]," | ",y["patient"]["adresse"]," | ",y["patient"]["contact"]," | ",y["patient"]["taille"]," | ",y["patient"]["poids"]," | ",y["patient"]["taux_glycemie"], " | ",y["patient"]["groupe_sanguin"]," | ",listToString(y["patient"]["symp"])," | ",y["medecin"]["nom"]," | ",y["medecin"]["prenom"]," | ",y["medecin"]["contact"]," | ",y["date"]," | ", listToString(y["traitements"]) )
                print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")



    # rechercher un patient
    @classmethod
    def search(self):
        data = loadConsultation()

        rch = str(input("Entrer l'id du patient :"))
        
        for key, value in data.items():
           print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________")
           print("nom | prenom | age | adresse | contact | taille | poids | taux_glycemie | groupe_sanguin | symptomes")
           print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
           resultat = False
           for x in value :
               if x == rch :
                    resultat = True
                    print(value[x]["nom"]," | ",value[x]["prenom"], " | ", value[x]["age"], " | ", value[x]["adresse"], " | ", value[x]["contact"], " | ", value[x]["taille"], " | ", value[x]["poids"], " | ", value[x]["taux_glycémie"], " | ", value[x]["groupe_sanguin"], " | ", listToString(value[x]["symp"]) )
                    print("___________________________________________________________________________________________________________________________________________________________________________________________________________________")
               elif resultat == False  :
                    print("\033[91m"+"Oups !!!! Nous n'avons trouvé aucun patient ayant cet id."+"\033[0m")
                    break

    
    # etablir un diagnostic
    @classmethod
    def diagnostic(self) :

        g = UniqueId()
        code = g.generate_id_formated()
        nom = str(input("Saisir le nom du patient:"))
        prenom = str(input("Saisir le prenom du patient:"))
        poids = float(input("Saisir le poids du patient:"))
        taux_glycémie = float(input("Saisir le taux de glycémie du patient:"))
        groupe_sanguin = str(input("Saisir le groupe sanguin du patient:"))
        print("................................................................")
        print("Veuillez saisir les symptomes séparés par des virgules!!")
        symptomes = str(input("Saisir les symptomes du patient:"))
        symp=symptomes.split(",")
        nom_medoc = str(input("Entrer le nom du médecin : "))
        prenom_medoc = str(input("Entrer le prenom du médecin : "))
        contact_medoc = str(input("Entrer le contact du médecin : "))
        date_diag = str(input("Entrer la date de consultation :"))
        print("................................................................")
        print("Veuillez saisir les traitements séparés par des virgules!!")
        traitements = str(input("Saisir les traitements :"))
        traits=traitements.split(",")
        dec = str(input("Cet traitement a t-il fonctionné pour ce patient ? : oui/non :"))
        obj = {
            code : {
                "patient" : {
                    "nom" : nom,
                    "prenom" : prenom,
                    "poids" : poids,
                    "taux_glycemie" : taux_glycémie,
                    "groupe_sanguin" : groupe_sanguin,
                    "symp" : symp
                },
                "date": date_diag,
                "medecin" : {
                    "nom" : nom_medoc,
                    "prenom" : prenom_medoc,
                    "contact" : contact_medoc
                },
                "traitements" : {
                    "libelle" : traits,
                    "decision" : dec
                }
            }
        }
        addNewDiagnostic(obj)
        print("\033[92m"+"Diagnostic établi avec succès!!"+"\033[0m")
                    







        
class Maladie:
    id : str
    nom: str
    symptomes: list
    departement: str


    def __init__(self, nom, symptomes, departement):
        g = UniqueId()
        self.id = g.generate_id_formated()
        self.nom = nom
        self.symptomes = symptomes
        self.departement = departement

    

    def __str__(self):
        return f"id: {self.id} \n nom: {self.nom} \n symptomes: {self.symptomes} \n departement: {self.departement} \n"
    
    # ajouter une nouvelle maladie
    @classmethod
    def create(self):
        g = UniqueId()
        code = g.generate_id_formated()
        nom = str(input("Saisir le nom :"))
        departement = str(input("Saisir le département :"))
        print("................................................................")
        print("Veuillez saisir les symptomes séparés par des virgules!!")
        symptomes = str(input("Saisir les symptomes :"))
        symp=symptomes.split(",")
        m = Maladie(nom, symp, departement)
        obj = {
            code : {
                "nom" : m.nom,
                "symptomes" : symp,
                "département" : m.departement
            }
        }
        addNewInMaladieStore(obj)
        print("\033[92m"+"Maladie enregistré avec succès!!"+"\033[0m")
        
    
    

    # afficher la liste des maladies
    @classmethod
    def read(self):
        data = loadMaladieStore()

        for key, value in data.items():
            print("_________________________________________________________________________________________________________________________________________________________________________________________________________________________")
            print("~~~~~~~~~~~~~~~~maladies~~~~~~~~~~~~~~ | symptomes")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            return value
            '''
            for x, y in value.items():
                return y
                #print(y["nom"], " | ",listToString(y["symptomes"])," | ",y["département"])
                #print("___________________________________________________________________________________________________________________________________________________________________________________________________________________")
            '''
            



