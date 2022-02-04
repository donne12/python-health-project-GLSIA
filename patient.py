from typing import Dict
from operateur import *
from datetime import datetime
from time import strftime
import os


now = datetime.now() 


class patient:
    def __init__(self, nom: str, prenom: str, adresse: str, age: int, consultations = {}, Analyse={} , numero: int=0):
        self.nom = nom.lower()
        self.prenom = prenom.lower()
        self.adresse = adresse.lower()
        self.age = age
        self.consultations = consultations
        # self.numero = numero
        if (numero == 0):
            data = lire("fichier.json")
            self.numero = data["Patient"][-1]["numero"]+1
        else:
            self.numero = numero

    def __str__(self):
        
        return self.nom + " " + self.prenom + " " + str(self.age) + " " + self.adresse+ " "

    def listPatient():
        patients = lire('fichier.json')['Patient']
        for patient in patients:
            print(str(patient['numero'])+': -'+str(patient['nom'].upper())+'  '+str(patient['prenom'].upper()))
            print('---------------------------------------------------------------------------------\n')

    def afficherConsultation(self,id = 0 , nom  =" " ,prenom= " "):
        data = lire("fichier.json")
        if( nom  !=" " and prenom != " " ):
            b= data["Patient"]
            for patient in  b:
                if((patient["nom"]==nom.lower()) and(patient["prenom"]==prenom.lower())):
                    self.numero = patient["numero"]
                    self.nom = patient["nom"]
                    self.prenom = patient["prenom"]
                    self.adresse = patient["adresse"]
                    self.age = patient["age"]
                    self.consultations = patient["consultations"]
        elif ( id != 0):
            b = data["Patient"]
            for patient in  b:
                if(patient["numero"]== id):
                    self.numero = patient["numero"]
                    self.nom = patient["nom"]
                    self.prenom = patient["prenom"]
                    self.adresse = patient["adresse"]
                    self.age = patient["age"]
                    self.consultations = patient["consultations"]
        else:
            pass

        
        print("liste des consultation de {} {}...".format(self.nom, self.prenom))
        print("\n")
        data = lire("fichier.json")
        b = data["Patient"]
        for patient in  b:
            if((patient["numero"]== self.trouver())):
                for cle, valeur in patient["consultations"].items():
                        print("----------------")
                        print("consultation du: "+cle)
                        for cle2, valeur2 in valeur.items():
                             print( cle2, "=", valeur2)
                        print("----------------")

    
    def afficherAnalyse(self,id = 0, nom  =" " ,prenom= " "):

        data = lire("fichier.json")
        if( nom  !=" " and prenom != " " ):
            b= data["Patient"]
            for patient in  b:
                    if((patient["nom"]==nom.lower()) and(patient["prenom"]==prenom.lower())):
                        self.numero = patient["numero"]
                        self.nom = patient["nom"]
                        self.prenom = patient["prenom"]
                        self.adresse = patient["adresse"]
                        self.age = patient["age"]
                        self.consultations = patient["consultations"]
        elif ( id != 0):
            b = data["Patient"]
            for patient in  b:
                if(patient["numero"]== id):
                    self.numero = patient["numero"]
                    self.nom = patient["nom"]
                    self.prenom = patient["prenom"]
                    self.adresse = patient["adresse"]
                    self.age = patient["age"]
                    self.consultations = patient["consultations"]
        else:
            pass
        print("liste des Analyse de {} {}...".format(self.nom, self.prenom))
        print("\n")
        data = lire("fichier.json")
        b = data["Patient"]
        for patient in  b:
            if((patient["numero"]== self.trouver())):
                for cle, valeur in patient["analyse"].items():
                        print("----------------")
                        print("Analyse du: "+cle)
                        for cle2, valeur2 in valeur.items():
                             print( cle2, "=", valeur2)
                        print("----------------")
    


    def consulter(self,id = 0, nom  =" " ,prenom= " "):
        
        data = lire("fichier.json")
        if( nom  !=" " and prenom != " " ):
            b= data["Patient"]
            for patient in  b:
                    if((patient["nom"]==nom.lower()) and(patient["prenom"]==prenom.lower())):
                        self.numero = patient["numero"]
                        self.nom = patient["nom"]
                        self.prenom = patient["prenom"]
                        self.adresse = patient["adresse"]
                        self.age = patient["age"]
                        self.consultations = patient["consultations"]
        elif ( id != 0):
            b = data["Patient"]
            for patient in  b:
                if(patient["numero"]== id):
                    self.numero = patient["numero"]
                    self.nom = patient["nom"]
                    self.prenom = patient["prenom"]
                    self.adresse = patient["adresse"]
                    self.age = patient["age"]
                    self.consultations = patient["consultations"]
        else:
            pass
        print("liste des consultation de {} {}...".format(self.nom, self.prenom))
        print("\n")

        consul={
                 
              "acuiteVisuelleDroite":str(input(" Acuite Visuelle de  l'oiel  gauche?: ")),
              "acuiteVisuelleGauche":str(input("Acuite Visuelle de  l'oiel  gauche?: ")),   
              "douleurGauche":verifier(input("Douleur à  l'oiel  gauche?[O/N]: ")),
              "douleurDroite":verifier(input("Douleur à  l'oiel  Droite?[O/N]: ")),
              "rougeGauche":verifier(input("l'oiel  gauche est il  rouge?[O/N]: ")),
              "rougeDroite":verifier(input("l'oiel  droite est il  rouge?[O/N]: ")),
              "gonflementGauche":verifier(input("Gonflement à  l'oiel  gauche?[O/N]: ")),
              "gouflementDroite":verifier(input("Gonflement  à  l'oiel  gauche?[O/N]: ")),
              "traitement":verifier(input("suivez vous un traitement ?[O/N]: ")),
              
            }
            
      
        data = lire("fichier.json")
        b = data["Patient"]
        for patient in  b:
            if((patient["numero"]== self.trouver())):
                cle= now.strftime("%m/%d/%Y")
                # cle= strftime( "%m/%d/%Y", datetime)
                patient["consultations"].update({cle: consul})

        consul={}
        ecrire("fichier.json",data)
        print(self)


    def  AnalyseRefractometre(self,id = 0, nom  =" " ,prenom= " "):
        
        data = lire("fichier.json")
        if( nom  !=" " and prenom != " " ):
            b= data["Patient"]
            for patient in  b:
                    if((patient["nom"]==nom.lower()) and(patient["prenom"]==prenom.lower())):
                        self.numero = patient["numero"]
                        self.nom = patient["nom"]
                        self.prenom = patient["prenom"]
                        self.adresse = patient["adresse"]
                        self.age = patient["age"]
                        self.analyse = patient["analyse"]
        elif ( id != 0):
            b = data["Patient"]
            for patient in  b:
                if(patient["numero"]== id):
                    self.numero = patient["numero"]
                    self.nom = patient["nom"]
                    self.prenom = patient["prenom"]
                    self.adresse = patient["adresse"]
                    self.age = patient["age"]
                    self.consultations = patient["consultations"]
        else:
            pass
        print("Analyse  de {} {}...".format(self.nom, self.prenom))
        print("\n")
        print("------------------------------------------------------")
        print("\n")
        print("Analyse oeil gauche ")
        print("\n")
        print("------------------------------------------------------")
        print("\n")
        consulG={
               
                        "sphere_loinG":    int(input("Entrez la valeur de la sphère lointaine : ")),       
                        "cylindre_loinG":   int(input("Entrez la valeur du cylindre lointain : ")),       
                        "axe_loinG":  int(input("Entrez la valeur de l'axe lointain : ")),       
                        "sphere_presG": int(input("Entrez la valeur de la sphère de près : ")),       
                        "cylinfre_presG": int(input("Entrez la valeur du cylindre de près : ")),       
                        "axe_presG": int(input("Entrez la valeur de l'axe de près : ")),
                  
        }

        print("------------------------------------------------------")
        print("\n")
        print("Analyse oeil Droite ")
        print("\n")
        print("------------------------------------------------------")
        print("\n")

        consulD={    
     
                
                     
                    "sphere_loinD":    int(input("Entrez la valeur de la sphère lointaine : ")),       
                    "cylindre_loinD":   int(input("Entrez la valeur du cylindre lointain : ")),       
                    "axe_loinD":  int(input("Entrez la valeur de l'axe lointain : ")),       
                    "sphere_presD": int(input("Entrez la valeur de la sphère de près : ")),       
                    "cylinfre_presD": int(input("Entrez la valeur du cylindre de près : ")),       
                    "axe_presD": int(input("Entrez la valeur de l'axe de près : ")), 
                  
        }
            
      
        data = lire("fichier.json")
        b = data["Patient"]
        for patient in  b:
            if((patient["numero"]== self.trouver())):
                cle= now.strftime("%m/%d/%Y")
                # cle= strftime( "%m/%d/%Y", datetime)
                patient["analyse"].update({cle:{"AnalyseDroite":consulD,"AnalyseGauche":consulG}})

        consulD={}
        consulG={}
        ecrire("fichier.json",data)
        print(self)
       
    
    def trouver(self):
        data = lire("fichier.json")
        b= data["Patient"]
        for patient in  b:
                if((patient["nom"]==self.nom) and(patient["prenom"]==self.prenom)):
                    return (patient["numero"])
        return None


    def verification(obj):
        data = lire("fichier.json")
        b= data["Patient"]
        for patient in  b:
                if((patient["nom"]==obj.nom) and(patient["prenom"]==obj.prenom)):
                    return True
        
        return False
                      
    
    def create(self):
            data = lire("fichier.json")
            if(self.verification()==False):
                data["Patient"].append(
                    {
                        "numero": self.numero,
                        "nom" : self.nom,
                        "prenom" : self.prenom,
                        "adresse" : self.adresse,
                        "age" : self.age,
                        "consultations": {},
                        "analyse":{},
                    }
                )
                print("patient ajouter")
                ecrire("fichier.json",data)
            else:
                   print("Erreur de creation du patient, veuillez reessayer !!")

    def update(self):      
        try:
            data = lire('fichier.json')
            patients = data['Patient']
            for patient in patients:
                if patient['id'] == self.trouver():
                    patient['nom'] = self.nom.lower()
                    patient['prenom'] = self.prenom.lower()
                    patient['adresse'] = self.adresse
                    patient['age'] = self.age
                    
            ecrire('fichier.json',data)
            print('Modification appliquées avec succès :-)')
            return
        except:
            return print("Une erreur s'est produite durant l'opération :-( ")
    
    
    def delpatient(obj):
        if obj.verification() :
            data = lire('fichier.json')
            try:
                for patient in data['Patient']:
                    if((patient["nom"]==obj.nom) and(patient["prenom"]==obj.prenom)):
                        del data['Patient'][patient['id']-1]
                        ecrire("fichier.json",data)
                        return print('Suppression effectuée avec succès !!:-)')
            except:
                return print("Une erreur est surevue durant l'opération !! :-(")
        return print('Impossible de supprimer un élément inexistant !!')
#
#p1= patient("A","z","a",18) 
# p1.create()
# #p1.consulter("Abal4o","za")
# # print(p1)
#p1.afficherConsultation(1)
# # p1.afficherConsultation()
# # p1.afficherAnalyse()
# p1.AnalyseRefractometre("Abalo","za")
# # # p1.consulter()
# # # patient.consulter("ed","ed")
