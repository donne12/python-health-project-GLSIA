from os import system
from turtle import update
from patient import *
from maladie import *

system('cls')
print("****************************************************************************")
print("*                                                                          *")
print("*                            OPHATAMOLOGIE                                 *")
print("*                                                                          *")
print("****************************************************************************")


tries = 0
tries_flag = ""
while tries_flag != "Close the program" :				
    print("--------------------------------------------------")
    print("|Entrer 1 pour  la gestion des patients			|\n|Entrer 2 pour la gestion des maladies			|")
    print("--------------------------------------------------")
    choix = int( input("Enter votre choix : "))
    if choix == 1 :																			
        print("*****************************************\n|         Gestion des patient         |\n*****************************************")
        Password = input("votre mots de passe svp : ")
        while True :
                    
            if Password == "1234" :
                
                print(" -------------------------------------------------------------------")
                print("|Pour ajouter un patient: Entrer 1	  	                           |")
                print("|Pour afficher la liste des patients: Entrer 2	  	               |")
                print("|Pour faire la consultation d'un patient  Entrer 3                  |")
                print("|Pour faire l'analyse  d'un patient  Entrer 4                       |")
                print("|Pour afficher la liste des consulatation d'un patient  Entrer 5    |")
                print("|Pour afficher la liste des analyse d'un patient  Entrer 6          |")
                print("|Pour revenir en arrière entrer E                                   |")
                print(" -------------------------------------------------------------------")
                Options = input ("Entrer votre choix : ")
                Options = Options.upper()
                        
                if Options == "1" :	 
                        _ = os.system('cls')
                        print("Enregistrons un patient...")
                        nom = input("Entrer le nom du patient: ")
                        prenom = input("Entrer le prenom du patient: ")
                        adresse = input("Entrer l'adresse du patient: ")
                        age = int (input("Entrer l'âge du patient: "))
                        try:
                            pat = patient(nom, prenom, adresse, age)
                            pat.create()
                            print("----------------------Patient ajouter avec success----------------------")
                        except :
                            print("L'id du patien doit etre un entier ")													#Admin mode --> Pateints Management
                                    
                                
                                        
                elif Options == "2" :										
                    # try :
                        _ = os.system('cls')
                        print("Liste des patient...")	
                        # patient_ID = int(input("Enter l'ID du patient: "))
                        # data = lire("fichier.json")
                        # b= data["Patient"]
                        # for pat in  b:
                        #     print("\n patient  numero             : ",pat["numero"])
                        #     print("\nnom  du  patient             : ",pat["nom"])
                        #     print("\nprenom  du  patient          : ",pat["prenom"])
                        #     print("\nage du patient               : ",pat["age"])
                        #     print("\nadress du patient            : ",pat["adresse"])
                        #     print("-----------------------------------------------------------------------")
                        patient.listPatient()
                        ans = input(
                        "Pour avoir plus de détails sur un patient, entrez le numéro de celle-ci ou son nom ...."+str('\n')+
                        "Pour revenir en arrière entrer E...\n: "
                            )
                        if ans.upper() == 'E' :
                            break
                        else:
                            try:
                                                          
                                try:
                                    int(ans)
                                    it_is = True
                                except ValueError:
                                    it_is = False

                                if(it_is== False):
                                    prenom = input("Entrer le prenom du patient: ")
                                   
                                    data = lire("fichier.json")
                                    b= data["Patient"]
                                    for pat in  b:
                                           if((pat["nom"]==ans) and(pat["prenom"]==prenom)):
                                                p1= patient( ans,prenom,pat["adresse"],pat["age"]) 
                                                p1.numero = pat["numero"]
                                                print(p1)
                                                p1.afficherConsultation()
                                                p1.afficherAnalyse(p1.nom,p1.prenom)

                                else:
                                    data = lire("fichier.json")
                                    b= data["Patient"]
                                    for pat in  b:
                                           if((pat["numero"]==int(ans))):
                                                p1= patient(pat["nom"],pat["prenom"],pat["adresse"],pat["age"]) 
                                                p1.numero = pat["numero"]
                                                print(p1)
                                                p1.afficherConsultation()
                                                p1.afficherAnalyse(p1.nom,p1.prenom)
                            except:
                                pass                    
                            ans = input("Voulez-vous modifier les informations de cet patient ? Entrez 'U'....\n Voulez-vous supprimer cet pattient ? Entrez 'D'....: \n")
                            # Choix de suppression d'une maladie
                            if ans.upper() == 'D':
                                ans = input('Voulez-vous vraiment supprimer cette maladie? O/N : ')
                                if ans.upper() == 'O':
                                    p1.delpatient()    
                                else:
                                    pass
            
                        
                            elif ans.upper() == 'U':
                                system('cls')
                                ans = input('Voulez-vous modifier le nom? O/N: ')
                                if ans.upper() == 'O':
                                    p1.nom = input('Entrez le nouveau nom du  patient: ')
                                else:
                                    pass
                                ans = input('Voulez-vous modifier le prenom? O/N: ')
                                if ans.upper() == 'O':
                                    p1.prenom = input('Entrez le nouveau prenom du  patient: ')
                                else:
                                    pass
                                ans = input('Voulez-vous modifier l age? O/N: ')
                                if ans.upper() == 'O':
                                    p1.age = input('Entrez l age du  patient: ')
                                else:
                                    pass

                                ans = input('Voulez-vous modifier l adresse? O/N: ')
                                if ans.upper() == 'O':
                                    p1.adresse = input('Entrez l adresse du  patient: ')
                                else:
                                    pass
                                
                                p1.update()

                        
                        
                    # except :
                    #     print("pas conpris")
                                
                elif Options == "3" :										
                            try :
                                _ = os.system('cls')		
                                print("Consultation...")
                                nom = input("Entrer le numero  ou  le nom du patient: ")                           
                                try:
                                    int(nom)
                                    it_is = True
                                except ValueError:
                                    it_is = False
                                if(it_is== False):
                                    prenom = input("Entrer le prenom du patient: ")
                                    p1= patient("A","z","a",18) 
                                    p1.consulter(nom,prenom)
                                else:
                                    p1.consulter( int(nom))
                            except :
                                print("patient  introuvable")
                
                elif Options == "4" :										
                            try :
                                _ = os.system('cls')	
                                print("Analyse ...")
                                nom = input("Entrer le numero  ou  le nom du patient: ")                           
                                try:
                                    int(nom)
                                    it_is = True
                                except ValueError:
                                    it_is = False
                                if(it_is== False):
                                    prenom = input("Entrer le prenom du patient: ")
                                    p1= patient("A","z","a",18) 
                                    p1.AnalyseRefractometre(nom,prenom)
                                  
                                else:
                                    p1.consulter( int(nom))
                                    p1.AnalyseRefractometre(int(nom))    
                            except :
                                print("patient  introuvable")
                                
                elif Options == "5" :										
                            try :
                                _ = os.system('cls')		
                                print("Liste  des consultation...")
                                nom = input("Entrer le numero  ou  le nom du patient: ")                           
                                try:
                                    int(nom)
                                    it_is = True
                                except ValueError:
                                    it_is = False
                                if(it_is== False):
                                    prenom = input("Entrer le prenom du patient: ")
                                    p1= patient("A","z","a",18) 
                                    p1.afficherConsultation(nom,prenom)
                                    
                                else:            
                                    p1.afficherConsultation(int(nom))
                            except :
                                print("patient  introuvable")
                                pass
                elif Options == "6" :										
                            try :	
                                _ = os.system('cls')	
                                print("Liste des analyse..")
                                nom = input("Entrer le numero  ou  le nom du patient: ")                           
                                try:
                                    int(nom)
                                    it_is = True
                                except ValueError:
                                    it_is = False
                                if(it_is== False):
                                    prenom = input("Entrer le prenom du patient: ")
                                    p1= patient("A","z","a",18) 
                                    p1.afficherAnalyse(nom,prenom)
                                   
                                else:
                                    p1.afficherAnalyse(int(nom))  
                               
                               
                            except :
                                print("patient  introuvable")
                                pass
                        
                                                    
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
                                
    if choix == 2 :																			
        print("*****************************************\n|         Gestion des Maladies         |\n*****************************************")
        Password = input("votre mots de passe svp : ")
        while True :
                    
            if Password == "123" :
                print("-------------------------------------------------------------------")
                print("|Pour ajouter une maladie: Entrer 1	  	                          |")
                print("|Pour afficher la liste des maladie: Entrer 2	  	              |")
                print("|Pour revenir en arrière entrer E                                  |")
                print("-------------------------------------------------------------------")
                Options = input ("Entrer votre choix : ")
                Options = Options.upper()
                
                # Création d'une nouvelle maladie
                if Options == "1" :	 
                        print("Enregistrons une Maladie...")
                        nom = input("Entrer le nom : ")
                        description = input("Entrer une description: ")
                        symptome = input("Entrer la liste des symptome separer par /: ")
                        
                        try:
                            listesympto= symptome.split("/")
                            maladie = Maladie(nom, description, listesympto)
                            maladie.create()
                        except :
                            print("Une erreur est survenue lors de l'enregistrement !! :-(")	
                            print('Voici vos anciennes données :\n Nom: '+str(nom)+'\nLa desciption: '+str(description)/
                                +'\n les Symptômes: '+str(listesympto)+'\n')
                
                #  Opérations sur les maladies existantes
                elif Options == "2" :
                    print("Liste des Maladies...")
                    Maladie.listMaladies()
                    ans = input(
                        "Pour avoir plus de détails sur une maladie, entrez le numéro de celle-ci ou son nom ...."+str('\n')+
                        "Pour revenir en arrière entrer E...\n: "
                    )
                    if ans.upper() == 'E' :
                        break
                    else:
                        try:
                            ans = int(ans)
                            maladie = Maladie.getMaladie(int(ans))
                        except:
                            pass         
                        maladie = Maladie.getMaladie(ans)   
                        maladie.desc()
                        ans = input("Voulez-vous modifier les informations de cette maladie ? Entrez 'U'....\n Voulez-vous supprimer cette maladie ? Entrez 'D'....: \n")
                        # Choix de suppression d'une maladie
                        if ans.upper() == 'D':
                            ans = input('Voulez-vous vraiment supprimer cette maladie? O/N : ')
                            if ans.upper() == 'O':
                                maladie.deleteMaladie()    
                            else:
                                pass
                        
                        # Choix de mise à jour d'une maladie
                        elif ans.upper() == 'U':
                            system('cls')
                            ans = input('Voulez-vous modifier le nom? O/N: ')
                            if ans.upper() == 'O':
                                maladie.nom = input('Entrez le nouveau nom de la maladie: ')
                            else:
                                pass
                            ans = input('Voulez-vous modifier la description? O/N: ')
                            if ans.upper() == 'O':
                                maladie.description = input('Entrez la nouvelle description de la maladie: ')
                            else:
                                pass
                            ans = input('Voulez-vous modifier les symptômes de cette maladie? O/N: ')
                            if ans.upper() == 'O':
                                symptome = input("Entrer la liste des symptome separer par /: ")
                            else:
                                pass
                            maladie.updateMaladie()
                        
                        else:
                            print('Choix incorrecte!!')
                            pass
                            
                elif Options == "E" :										
                    break
                
                else :
                            print("entrez un choix correct\n")
            elif Password != "123" :
                if tries < 2 :
                    Password = input("Mots de passe incorrecte !!!Ressayer SVP : ")
                    tries += 1
                else :
                    print("Mots de passe incorrecte !!!Trop  de tentative")
                    tries_flag = "Arrêt du programme"
                    break        
    
    # elif AdminOptions == "E" :															
    #     break
    
    # else :
    #     print("choix incorrect")
    

    


 