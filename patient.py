import json
import os
from time import strftime
from maladie import Maladie
class Patient(object):
	"""Classe qui enrégistre tout les imformations important à savoir sur un Patient"""
	apat = []
	def __init__(self,nom="",prenom="",age=0):
		self.pat = {
			"nom": nom,
			"prenom": prenom,
			"age": age,
			"consultation": [],
			"traiter": False
		}
	def jsonSave(filePath,subject):
		"""Fonction qui permet d'enregistrer un fichier json"""
		with open(filePath,"w",encoding="utf8") as file:
			json.dump(subject,file,ensure_ascii=False,indent=4)
		print("Enregistrer avec succes")
	def exist(filename):
		"""Permet de verivier si un fichier exist ou pas"""
		if os.path.exists(filename):
			return 1
		else: return 0;
	def load(self):
		"""Fonction qui permet de charger tous les patients"""
		if Patient.exist("json/patient.json"):
			with open("json/patient.json") as file:
				Patient.apat = json.load(file)
	def desc(self):
		"""Permet de renseigner les informations concernant un Patient enregistrer"""
		choix = ""
		while choix == "":
			if self.pat["nom"] == "":
				choix = str(input("Entrer le nom patient : "))
				if choix != "": 
					self.pat["nom"], choix = choix.upper(), self.pat["nom"]
				else:
					print("Warning: Entrer les informations demandé")
			elif self.pat["prenom"] == "":
				choix = str(input("Entrer le prenom : "))
				if choix != "":
					self.pat["prenom"], choix = choix.title(), self.pat["prenom"]
				else:
					print("Warning: Entrer les informations demandé")
			elif self.pat["age"] == 0:
				choix = str(input("Entrer l'age du patient : "))
				if choix != "":
					self.pat["age"], choix = int(choix), ""
				else:
					print("Warning: Entrer les informations demandé")
			else:
				del choix
				break
	def add(self):
		"""Fonction qui permet d'ajouter un nouveau patient"""
		if self.pat["nom"] == "" or self.pat["prenom"] == "":
			Patient.desc(self)
		if Patient.apat == []:
			Patient.load(self)
		Patient.apat.append(self.pat)
		Patient.jsonSave("json/patient.json",Patient.apat)
	def list(self):
		"""Fonction qui permet de lister tout les patients enregistrer"""
		if Patient.apat == []:
			Patient.load(self)
		if Patient.apat != []:
			print("======= listes des Patients enregistrés =======")
			for i in list(range(len(Patient.apat))):
				print("		Patient n°{} : {} {}".format(i,Patient.apat[i]["nom"],Patient.apat[i]["prenom"]))
		else:
			print("Desolé il n'y a aucun patient enregistrer")
	def trueOrFalse(asert):
		if asert.strip().lower() in ["oui"]: return True
		elif asert.strip().lower() in ["non"]: return False
		return False
	def SelectMaladie():
		print("De quel maladie penser vous que ce patient souuffre ?")
		Maladie.list("")
		if Maladie.amal == []:
			print("==== creer une maladie ===")
			cmal = Maladie()
			cmal.add()
			Maladie.list("")
		if Maladie.amal != []:
			print("Entrer le numero de la maladie correspondante :",end=" ")
			ch = int(str(input()))
			while ch not in list(range(len(Maladie.amal))): 
				print("Entrer un numero correct entre {} et {}".format(list(range(len(Maladie.amal)))[0],list(range(len(Maladie.amal)))[-1]))
				ch = int(str(input("Entrer le numero de la maladie correspondante : ")))

			return Maladie.amal[ch]["nom"]
	def consultInformation():
		tab =  {
			"poid": int(input("Entrer le poids du patient : ")),
			"temp": int(input("Entrer la temperature du patient : ")),
			"glycemie": Patient.trueOrFalse(str(input("Le Patient est il glycemique ? : "))),
			"cholesterole": Patient.trueOrFalse(str(input("Le Patient a t il le cholesterole ? : "))),
			"coloration_yeux": str(input("Quelle est la couleur des yeux du Patient : ")),
			"coloration_bouche": str(input("Quelle est la couleur de la bouche du Patient : ")),
			"coloration_doigt": str(input("Quelle est la couleur des doigts du Patient : ")),
			"coloration_main": str(input("Quelle est la couleur des mains du Patient : ")),
			"blessure": Patient.trueOrFalse(str(input("Le Patient est il bleissé ? : "))),
			"choque_pointe": Patient.trueOrFalse(str(input("Le Patient a t il eu un choque ? : "))),
			"analyse": Patient.trueOrFalse(str(input("Le Patient avait deja t il subit une analye ? : "))),
			"anemie": Patient.trueOrFalse(str(input("Le Patient est il anemique ? : "))),
			"ECG": int(input("Quelle est le ECG du patient : ")),
			"diagnostic": {
				"diag": str(input("Quelles est votre diagnostic pour cet patient : ")),
				"maladie": Patient.SelectMaladie()
			},
			"date_consult": strftime("%A le %d %B %Y a %Hh:%Mm:%Ss")
		}
		return tab
	def consult(self):
		"""Fonction qui permet de faire une consultation pour un patient"""
		print("===== Demande de consultation pour un patient =====")
		Patient.list(self)
		if Patient.apat != []:
			print("Entrer le numero du patient à consulter :",end=" ")
			ch = int(str(input()))
			while ch not in list(range(len(Patient.apat))): 
				print("Entrer un numero correct entre {} et {}".format(list(range(len(Patient.apat)))[0],list(range(len(Patient.apat)))[-1]))
				ch = int(str(input("Entrer le numero du patient à consulter : ")))
			
			print("Patient n°{} nom: {} {}".format(ch,Patient.apat[ch]["nom"],Patient.apat[ch]["prenom"]))
			# choix = ""
			Patient.apat[ch]["consultation"].append(Patient.consultInformation())
			# Patient.apat[ch]["lib"], choix = choix, Patient.apat[ch]["lib"]
			# Patient.apat[ch]["desc"], choix = choix, Patient.apat[ch]["desc"]
			Patient.jsonSave("json/patient.json",Patient.apat)