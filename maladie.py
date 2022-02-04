import json
import os
from cmaladie import Cmaladie
class Maladie(object):
	"""Classe qui s'occupe de repertorier les maladies"""
	amal = []
	def __init__(self,nom="",categorie="",symptome=""):
		self.mal = {
			"nom": nom,
			"categorie": categorie,
			"symptome": symptome
		}
	def jsonSave(filePath,subject):
		"""Fonction qui permet d'enregistrer un fichier json"""
		with open(filePath,"w",encoding="utf8") as file:
			json.dump(subject,file,ensure_ascii=False,indent=4)
		print("Enregistrer avec succes")
	def exist(filename):
		"""Permet de verifier si un fichier existe ou pas"""
		if os.path.exists(filename):
			return 1
		else: return 0;
	def load(self):
		"""Fonction qui permet de charger tous les maladies enregistrés"""
		if Maladie.exist("json/maladie.json"):
			with open("json/maladie.json") as file:
				Maladie.amal = json.load(file)
	def desc(self):
		"""Permet de renseigner les informations concernant une maladie à enregistrer"""
		choix = ""
		while choix == "":
			if self.mal["nom"] == "":
				choix = str(input("Entrer le nom de la maladie : "))
				if choix != "": 
					self.mal["nom"], choix = choix, self.mal["nom"]
				else:
					print("Warning: Entrer les informations demandé")
			elif self.mal["categorie"] == "":
				Cmaladie.list("")
				if Cmaladie.acmal == []:
					print("==== creer une categorie de maladie ===")
					cmal = Cmaladie()
					cmal.add()
					Cmaladie.list("")
				if Cmaladie.acmal != []:
					print("Entrer le numero de la categorie correspondante :",end=" ")
					ch = int(str(input()))
					while ch not in list(range(len(Cmaladie.acmal))): 
						print("Entrer un numero correct entre {} et {}".format(list(range(len(Cmaladie.acmal)))[0],list(range(len(Cmaladie.acmal)))[-1]))
						ch = int(str(input("Entrer le numero de la categorie correspondante : ")))
					
					choix = Cmaladie.acmal[ch]["lib"]
				if choix != "": 
					self.mal["categorie"], choix = choix, self.mal["categorie"]
				else:
					print("Warning: Entrer les informations demandé")
			elif self.mal["symptome"] == "":
				print("Entrer les symptomes pour cette maladie")
				choix = str(input())
				if choix != "":
					self.mal["symptome"], choix = choix, self.mal["symptome"]
				else:
					print("Warning: Entrer les informations demandé")
			else:
				del choix
				break
	def add(self):
		"""Fonction qui permet d'ajouter une nouvelle maladie"""
		if self.mal["nom"] == "" or self.mal["categorie"] == "" or self.mal["symptome"] == "":
			Maladie.desc(self)
		if Maladie.amal == []:
			Maladie.load(self)
		Maladie.amal.append(self.mal)
		Maladie.jsonSave("json/maladie.json",Maladie.amal)
	def list(self):
		"""Fonction qui permet de lister les maladies enregistrer"""
		if Maladie.amal == []:
			Maladie.load(self)
		if Maladie.amal != []:
			print("======= listes des maladies =======")
			for i in list(range(len(Maladie.amal))):
				print("		{} : {}".format(i,Maladie.amal[i]["nom"]))
		else:
			print("Desolé il n'y a aucune maladies enregistrer")
	def modify(self):
		"""Permet de modifer une maladie"""
		Maladie.list(self)
		print("Entrer le numero de la maladie à modifier :",end=" ")
		choi = int(str(input()))
		while choi not in list(range(len(Maladie.amal))): 
			print("Entrer un numero correct entre {} et {}".format(list(range(len(Maladie.amal)))[0],list(range(len(Maladie.amal)))[-1]))
			choi = int(str(input("Entrer le numero de la maladie à modifier : ")))
		
		print("Pret à modifier la ligne {} ".format(Maladie.amal[choi]))
		Maladie.amal[choi]["nom"] = Maladie.amal[choi]["categorie"] = Maladie.amal[choi]["symptome"] = choix = ""
		while choix == "":
			if Maladie.amal[choi]["nom"] == "":
				choix = str(input("Entrer le nouveau nom de la maladie : "))
				if choix != "": 
					Maladie.amal[choi]["nom"], choix = choix, Maladie.amal[choi]["nom"]
				else:
					print("Warning: Entrer les informations demandé")
			elif Maladie.amal[choi]["categorie"] == "":
				Cmaladie.list("")
				if Cmaladie.acmal == []:
					print("==== creer une categorie de maladie ===")
					cmal = Cmaladie()
					cmal.add()
					Cmaladie.list("")
				if Cmaladie.acmal != []:
					print("Entrer le nouveau numero de la categorie correspondante :",end=" ")
					ch = int(str(input()))
					while ch not in list(range(len(Cmaladie.acmal))): 
						print("Entrer un numero correct entre {} et {}".format(list(range(len(Cmaladie.acmal)))[0],list(range(len(Cmaladie.acmal)))[-1]))
						ch = int(str(input("Entrer le nouveau numero de la categorie correspondante : ")))
					
					choix = Cmaladie.acmal[ch]["lib"]
				if choix != "": 
					Maladie.amal[choi]["categorie"], choix = choix, Maladie.amal[choi]["categorie"]
				else:
					print("Warning: Entrer les informations demandé")
			elif Maladie.amal[choi]["symptome"] == "":
				print("Entrer les nouvelles symptomes pour cette maladie")
				choix = str(input())
				if choix != "":
					Maladie.amal[choi]["symptome"], choix = choix, Maladie.amal[choi]["symptome"]
				else:
					print("Warning: Entrer les informations demandé")
			else:
				del choix
				break
		Maladie.jsonSave("json/maladie.json",Maladie.amal)
	def showDescipText(self):
		"""Fonction qui permet d'afficher la description textuelle d'un maladie"""
		Maladie.list(self)
		if Maladie.amal != []:
			print("Entrer le numero de la maladie :",end=" ")
			ch = int(str(input()))
			while ch not in list(range(len(Maladie.amal))): 
				print("Entrer un numero correct entre {} et {}".format(list(range(len(Maladie.amal)))[0],list(range(len(Maladie.amal)))[-1]))
				ch = int(str(input("Entrer le numero de la maladie : ")))
			print("Libelle : {}\nCategorie de maladie : {}\nSymptomes : {}".format(Maladie.amal[ch]["nom"],Maladie.amal[ch]["categorie"],Maladie.amal[ch]["symptome"]))