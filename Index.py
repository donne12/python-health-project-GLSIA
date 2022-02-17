from os import system
import sys
sys.path.append(r"C:\pediatrie")
from Models import Auth
from Interfaces import MaladieInterface, PatientInterface


system("cls")
print("\033[108m"+"==============  PYTHON HEALTH PROJECT  ============="+"\033[0m")
print("................................................................")
system("pause")
system("cls")




print("********************************************************************")
print("*                                                                  *")
print("*             Bienvenue sur le module de la pédiatrie              *")
print("*                                                                  *")
print("********************************************************************")

nbEssaies = 0
essaie_text = ""
nbTotalEssaies = 2

while essaie_text != "Fermer le programme" :
    print("-----------------------------------------")
    print("|Mode Sécurisé (Tapez 1)			|\n|Mode simple (Tapez 2)			|\n|Quitter le programme (Tapez E)")
    print("-----------------------------------------")
    Admin_user_mode = input("Entrer le mode : ") 

    #Admin mode
    if Admin_user_mode == "1" :	
        print("*****************************************\n|         Bienvenue dans le mode Admin         |\n*****************************************")
        username = str(input("Veuillez saisir votre nom d'utilisateur : "))
        password = str(input("Veuillez saisir votre mot de passe : ")).encode('utf-8')

        while True :
            a = Auth.Authenticate(username, password)
            res = a.checkUser()
            if res == True :
                print("-----------------------------------------")
                print("|Gérer les maladies (Tapez 1) 		|\n|Gérer les consultations (Tapez 2) 	 	|\n|Gérer les patients (Tapez 3) 	|\n|Revenir au menu précédent (Tapez E)			|")
                print("-----------------------------------------")
                AdminOptions = input ("Entrer votre choix : ")
                AdminOptions = AdminOptions.upper()


                #Admin mode --> Gestion des patients
                if AdminOptions == "1" :
                    print("-----------------------------------------")
                    print("|Ajouter une nouvelle maladie  (Tapez 1)	  	|")
                    print("|Afficher des informations sur une maladie (Tapez 2) 	  	|")
                    print("|Afficher la liste des maladies (Tapez 3)		|")
                    print("|Modifier les informations d'une maladie (Tapez 4)    	|")
                    print("|Revenir au menu précédent (Tapez E)	     			|")
                    print("-----------------------------------------")
                    Admin_choice = input ("Entrer votre choix : ")
                    Admin_choice = Admin_choice.upper()


                    if Admin_choice == "1" : 	
                        MaladieInterface.addMaladie()
                    elif Admin_choice == "2" :	
                        MaladieInterface.displayOne()
                    elif Admin_choice == "3" :	
                        MaladieInterface.listMaladie()
                    elif Admin_choice == "4" :
                        MaladieInterface.updateOne()
                    elif Admin_choice == "E" :
                        break
                    else :
                        print("\033[91m"+"Choix incorrecte !!!!!!!!!!!!!!"+"\033[0m")
    
                elif AdminOptions == "2" :
                    print("-----------------------------------------")
                    print("|Ajouter une consultation  (Tapez 1)	  	|")
                    print("|Afficher les resultats pour un patient (Tapez 2) 	  	|")
                    print("|Afficher la liste des consultations pour un patient(Tapez 3)		|")
                    print("|Enregistrer les resultats pour un patient (Tapez 4)    	|")
                    print("|Revenir au menu précédent (Tapez E)	     			|")
                    print("-----------------------------------------")
                    Admin_choice = input("Entrer votre choix : ")
                    Admin_choice = Admin_choice.upper()

                    if Admin_choice == "1" : 	
                        PatientInterface.consult()
                    elif Admin_choice == "2" :	
                        PatientInterface.listResult()
                    elif Admin_choice == "3" :	
                        PatientInterface.listConsult()
                    elif Admin_choice == "4" :
                        PatientInterface.saveResult()
                    elif Admin_choice == "E" :
                        break
                    else :
                        print("\033[91m"+"Choix incorrecte !!!!!!!!!!!!!!"+"\033[0m")

                elif AdminOptions == "3" :
                    print("-----------------------------------------")
                    print("|Ajouter un nouveau patient  (Tapez 1)	  	|")
                    print("|Afficher des informations sur un patient (Tapez 2) 	  	|")
                    print("|Afficher la liste des patients (Tapez 3)		|")
                    print("|Modifier les informations d'un patient (Tapez 4)    	|")
                    print("|Revenir au menu précédent (Tapez E)	     			|")
                    print("-----------------------------------------")
                    Admin_choice = input("Entrer votre choix : ")
                    Admin_choice = Admin_choice.upper()

                    if Admin_choice == "1" : 	
                        PatientInterface.addPatient()
                    elif Admin_choice == "2" :	
                        PatientInterface.displayOne()
                    elif Admin_choice == "3" :	
                        PatientInterface.listPatient()
                    elif Admin_choice == "4" :
                        PatientInterface.updateOne()
                    elif Admin_choice == "E" :
                        break
                    else :
                        print("\033[91m"+"Choix incorrecte !!!!!!!!!!!!!!"+"\033[0m")
                elif AdminOptions == "E" :
                    break
                else :
                    print("\033[91m"+"Choix incorrecte !!!!!!!!!!!!!!"+"\033[0m")
            elif res == False :
                if nbEssaies < nbTotalEssaies :
                    print("\033[91m"+f"Nom d'utilisateur ou mot de passe incorrecte, réessayez !!!! Vous avez encore {format(nbTotalEssaies - nbEssaies)} essaies."+"\033[0m")
                    username = str(input("Veuillez saisir votre nom d'utilisateur : "))
                    password = str(input("Veuillez saisir votre mot de passe : ")).encode('utf-8')
                    nbEssaies += 1
                else :
                    print("\033[94m"+"Votre nombre d'essaie est atteint !!! veuillez réessayer une prochaine fois!!!!!!!!"+"\033[0m")
                    essaie_text = "Fermer le programme"
                    break
    

    # user mode
    elif Admin_user_mode == "2" :
        print("*****************************************\n|         Bienvenue dans le mode Utilisateur         |\n*****************************************")
        while True :
            print("|Gérer les maladies (Tapez 1)  	|\n|Revenir au menu précédent (Tapez E)			|")
            print("-----------------------------------------")
            UserOptions = input ("Entrer votre choix : ")
            UserOptions = UserOptions.upper()

            if UserOptions == "1" :
                print("-----------------------------------------")
                print("|Liste des maladies  (Tapez 1)	  	|")
                print("|Revenir au menu précédent (Tapez E)	     			|")
                print("-----------------------------------------")
                User_choice = input ("Entrer votre choix : ")
                User_choice = User_choice.upper()

                if User_choice == "1" :
                    MaladieInterface.listMaladie()
                elif User_choice == "E" :
                    break
                else :
                    print("\033[91m"+"Choix incorrecte !!!!!!!!!!!!!!"+"\033[0m")
            elif UserOptions == "E" :
                break
            else :
                print("\033[91m"+"Choix incorrecte !!!!!!!!!!!!!!"+"\033[0m")

    elif Admin_user_mode == "E" :
        break
    else :
        print("\033[91m"+"Vous devez choisir entre 1 et 2 !!!!!!!!!!!!!!"+"\033[0m")


	   
