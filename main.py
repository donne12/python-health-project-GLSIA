from patient import *
from maladie import *

_ = os.system('cls')
print("****************************************************************************")
print("*                                                                          *")
print("*             OPHATAMOLOGIE                                                *")
print("*                                                                          *")
print("****************************************************************************")


tries = 0
tries_flag = ""
while tries_flag != "Close the program" :				
        print("--------------------------------------------------")
        print("|Entrer 1 pour  la gestion des patients			|\n|Entrer 2 pour la gestion des maladies			|")
        print("--------------------------------------------------")
        choix = int( input("Enter votre choix : "))
        if choix == 1 :																			#Admin mode
            print("*****************************************\n|         Gestion des patient         |\n*****************************************")
            Password = input("votre mots de passe svp : ")
            while True :
                        
                if Password == "1234" :
                    print("------------------------------------------------------------------")
                    print("|POur ajouter un patient: Entrer 1	  	                          |")
                    print("|POur afficher la liste des patients: Entrer 2	  	              |")
                    print("|POur faire la consultation d'un patient  Entrer 3                 |")
                    print("|POur faire l'analyse  d'un patient  Entrer 4                      |")
                    print("|POur afficher la liste des consulatation d'un patient  Entrer 5   |")
                    print("|POur afficher la liste des analyse d'un patient  Entrer 6         |")
                    print("|pour revenir en arrière entrer E                                  |")
                    print("-------------------------------------------------------------------")
                    Options = input ("Entrer votre choix : ")
                    Options = Options.upper()
                            
                    if Options == "1" :	 
                            print("Enregistrons un patient...")
                            nom = input("Entrer le nom du patient: ")
                            prenom = input("Entrer le prenom du patient: ")
                            adresse = input("Entrer l'adresse du patient: ")
                            age = int (input("Entrer l'âge du patient: "))
                            try:
                                patient = patient(nom, prenom, adresse, age)
                                patient.create()
                                print("----------------------Patient ajouter avec success----------------------")
                            except :
                                print("L'id du patien doit etre un entier ")													#Admin mode --> Pateints Management
                                        
                                    
                                            
                    elif Options == "2" :										
                        # try :
                            print("Liste des patient...")	
                            # patient_ID = int(input("Enter l'ID du patient: "))
                            data = lire("fichier.json")
                            b= data["Patient"]
                            for pat in  b:
                                print("\n patient  numero             : ",pat["numero"])
                                print("\nnom  du  patient             : ",pat["nom"])
                                print("\nprenom  du  patient          : ",pat["prenom"])
                                print("\nage du patient               : ",pat["age"])
                                print("\nadress du patient            : ",pat["adresse"])
                                print("---------------------------------------")
                            
                        # except :
                        #     print("pas conpris")
                                    
                    elif Options == "3" :										
                                try :		
                                    print("Consultation...")
                                    nom = input("Entrer le nom du patient: ")
                                    prenom = input("Entrer le prenom du patient: ")
                                    p1= patient("A","z","a",18) 
                                    p1.consulter(nom,prenom)
                                except :
                                    print("patient  introuvable")
                    
                    elif Options == "4" :										
                                try :		
                                    print("Analyse ...")
                                    nom = input("Entrer le nom du patient: ")
                                    prenom = input("Entrer le prenom du patient: ")
                                    p1= patient("A","z","a",18) 
                                    p1.AnalyseRefractometre(nom,prenom)
                                except :
                                    print("patient  introuvable")
                    elif Options == "5" :										
                                try :		
                                    print("Liste  des consultation...")
                                    nom = input("Entrer le nom du patient: ")
                                    prenom = input("Entrer le prenom du patient: ")
                                    p1= patient("A","z","a",18) 
                                    p1.afficherConsultation(nom,prenom)
                                except :
                                    print("patient  introuvable")
                    elif Options == "6" :										
                                try :		
                                    print("Liste des analyse..")
                                    nom = input("Entrer le nom du patient: ")
                                    prenom = input("Entrer le prenom du patient: ")
                                    p1= patient("A","z","a",18) 
                                    p1.afficherAnalyse(nom,prenom)
                                except :
                                    print("patient  introuvable")
                            
                                                        
                    elif Options == "E" :										
                                break
                    
                    else :
                                print("entrer un choix correct\n")
                elif Password != "1234" :
                    if tries < 2 :
                        Password = input("Mots de passe incorrecte !!!Ressayer SVP : ")
                        tries += 1
                    else :
                        print("Mots de passe incorrecte !!!Trop  de tentative")
                        tries_flag = "Arrêt du programme"
                        break
                                    
        if choix == 2 :																			#Admin mode
            print("*****************************************\n|         Gestion des Maladies         |\n*****************************************")
            Password = input("votre mots de passe svp : ")
            while True :
                        
                if Password == "123" :
                    print("------------------------------------------------------------------")
                    print("|POur ajouter une maladie: Entrer 1	  	                          |")
                    print("|POur afficher la liste des maladie: Entrer 2	  	              |")
                    print("|pour revenir en arrière entrer E                                  |")
                    print("-------------------------------------------------------------------")
                    Options = input ("Entrer votre choix : ")
                    Options = Options.upper()
                    if Options == "1" :	 
                            print("Enregistrons une Maladie...")
                            nom = input("Entrer le nom : ")
                            description = input("Entrer une description: ")
                            symptome = input("Entrer la liste des symptome separer par /: ")
                            
                            try:
                                listesympto= symptome.split("/")
                                maladie = Maladie(nom, description, listesympto)
                                maladie.create()
                                print("----------------------Maladie ajouter avec success----------------------")
                            except :
                                print("L'id du patien doit etre un entier ")	
                    elif Options == "2" :										
                        # try :
                            print("Liste des patient...")	
                            # patient_ID = int(input("Enter l'ID du patient: "))
                            data = lire("fichier.json")
                            b= data["Patient"]
                            for pat in  b:
                                print("\n patient  numero             : ",pat["numero"])
                                print("\nnom  du  patient             : ",pat["nom"])
                                print("\nprenom  du  patient          : ",pat["prenom"])
                                print("\nage du patient               : ",pat["age"])
                                print("\nadress du patient            : ",pat["adresse"])
                                print("---------------------------------------")
                    elif Options == "E" :										
                                break
                    
                    else :
                                print("entrer un choix correct\n")
                elif Password != "123" :
                    if tries < 2 :
                        Password = input("Mots de passe incorrecte !!!Ressayer SVP : ")
                        tries += 1
                    else :
                        print("Mots de passe incorrecte !!!Trop  de tentative")
                        tries_flag = "Arrêt du programme"
                        break        
        
        # elif AdminOptions == "E" :															#Back
        #     break
        
        # else :
        #     print("choix incorrect")
    

    


#p2 = Patient.find(2)
#p2.consulter()


#print("\nLes resultats de la consultation de {} {}...".format(p2.nom, p2.prenom))
#print(p2.listConslutation())
"""print("Trouvons les gens\n")
p = Patient.find(1)
print(p)

print(p2)
pr = Patient.find(15)
print(pr)"""
# print("Faisons une recherche....\n")
# recherche = input("Recherche: ")
