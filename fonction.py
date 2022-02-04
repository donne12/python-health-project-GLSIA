from cmaladie import Cmaladie
from maladie import Maladie
from traitement import Traitement
from patient import Patient

def gererCategorieMaladie():
	print("===== Gerer les categories de maladies ====== ")
	print("Taper 1 pour affichier tous les categories de maladie")
	print("Taper 2 pour affichier les descriptions textuelle pour une categorie de maladie specifique")
	print("Taper 3 pour ajouter une categories de maladie")
	print("Taper 4 pour modifier une categorie de maladie")
	print("Taper 0 pour sortir du programme")
	choix = str(input("Quelle est votre choix : "))
	if choix == "0":
		exit()
	elif choix == "1":
		Cmaladie.list("")
	elif choix == "2":
		Cmaladie.showDescipText("")
	elif choix == "3":
		c = Cmaladie()
		c.add()
	elif choix == "4":
		Cmaladie.modify("")
	else:
		print("Votre choix est erroné")
def gererMaladies():
	print("===== Gerer les maladies ====== ")
	print("Taper 1 pour affichier tous les maladies enregistrés")
	print("Taper 2 pour affichier les descriptions textuelle pour une maladie specifique")
	print("Taper 3 pour ajouter une maladie")
	print("Taper 4 pour modifier une maladie")
	print("Taper 0 pour sortir du programme")
	choix = str(input("Quelle est votre choix : "))
	if choix == "0":
		exit()
	elif choix == "1":
		Maladie.list("")
	elif choix == "2":
		Maladie.showDescipText("")
	elif choix == "3":
		c = Maladie()
		c.add()
	elif choix == "4":
		Maladie.modify("")
	else:
		print("Votre choix est erroné")
def gererTraitementsMaladies():
	print("===== Gerer les traitements de maladies ====== ")
	print("Taper 1 pour affichier tous les maladies qui ont un traitement")
	print("Taper 2 pour affichier les descriptions textuelle des traitements pour les maladies enregistrés")
	print("Taper 3 pour ajouter un traitement pour une maladie")
	print("Taper 4 pour modifier un traitement d'une maladie enregistré")
	print("Taper 0 pour sortir du programme")
	choix = str(input("Quelle est votre choix : "))
	if choix == "0":
		exit()
	elif choix == "1":
		Traitement.list("")
	elif choix == "2":
		Traitement.showDescipText("")
	elif choix == "3":
		c = Traitement()
		c.add()
	elif choix == "4":
		Traitement.modify("")
	else:
		print("Votre choix est erroné")
def gererPatients():
	print("===== Gerer les Patients ====== ")
	print("Taper 1 pour affichier tous les patients")
	print("Taper 2 pour ajouter un nouveau patient")
	print("Taper 3 pour effectuer une consultation pour un patient")
	print("Taper 0 pour sortir du programme")
	choix = str(input("Quelle est votre choix : "))
	if choix == "0":
		exit()
	elif choix == "1":
		Patient.list("")
	elif choix == "2":
		c = Patient()
		c.add()
	elif choix == "3":
		Patient.consult("")
	else:
		print("Votre choix est erroné")
