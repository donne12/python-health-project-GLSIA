import json
import os
class Cmaladie(object):
	"""Classe qui repertorie des description textuelle sur des categories de maladie"""
	acmal = []
	def __init__(self,lib="",desc=""):
		self.cmal = {
			"lib": lib,
			"desc": desc
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
		"""Fonction qui permet de charger tous les categories de maladie enregistrés"""
		if Cmaladie.exist("json/cmaladie.json"):
			with open("json/cmaladie.json") as file:
				Cmaladie.acmal = json.load(file)
	def desc(self):
		"""Permet de renseigner les informations concernant une categorie de maladie à enregistrer"""
		choix = ""
		while choix == "":
			if self.cmal["lib"] == "":
				choix = str(input("Entrer le nom de la categorie pour la maladie : "))
				if choix != "": 
					self.cmal["lib"], choix = choix, self.cmal["lib"]
				else:
					print("Warning: Entrer les informations demandé")
			elif self.cmal["desc"] == "":
				print("Entrer la description textule pour cette categorie")
				choix = str(input())
				if choix != "":
					self.cmal["desc"], choix = choix, self.cmal["desc"]
				else:
					print("Warning: Entrer les informations demandé")
			else:
				del choix
				break
	def add(self):
		"""Fonction qui permet d'ajouter une nouvelle categorie"""
		if self.cmal["lib"] == "" or self.cmal["desc"] == "":
			Cmaladie.desc(self)
		if Cmaladie.acmal == []:
			Cmaladie.load(self)
		Cmaladie.acmal.append(self.cmal)
		Cmaladie.jsonSave("json/cmaladie.json",Cmaladie.acmal)
	def list(self):
		"""Fonction qui permet de lister les categories de maladie"""
		if Cmaladie.acmal == []:
			Cmaladie.load(self)
		if Cmaladie.acmal != []:
			print("======= listes des categories de maladie =======")
			for i in list(range(len(Cmaladie.acmal))):
				print("		{} : {}".format(i,Cmaladie.acmal[i]["lib"]))
		else:
			print("Desolé il n'y a aucune categorie de maladie enregistrer")
	def modify(self):
		"""Fonction qui permet de modifer une categorie de maladie"""
		Cmaladie.list(self)
		if Cmaladie.acmal != []:
			print("Entrer le numero de la categorie à modifier :",end=" ")
			ch = int(str(input()))
			while ch not in list(range(len(Cmaladie.acmal))): 
				print("Entrer un numero correct entre {} et {}".format(list(range(len(Cmaladie.acmal)))[0],list(range(len(Cmaladie.acmal)))[-1]))
				ch = int(str(input("Entrer le numero de la categorie à modifier : ")))
			
			print("Pret à modifier la ligne {} ".format(Cmaladie.acmal[ch]))
			choix = ""
			Cmaladie.acmal[ch]["lib"] = Cmaladie.acmal[ch]["desc"] = ""
			while choix == "":
				if Cmaladie.acmal[ch]["lib"] == "":
					choix = str(input("Entrer le nouveau nom pour cette categorie : "))
					if choix != "": 
						Cmaladie.acmal[ch]["lib"], choix = choix, Cmaladie.acmal[ch]["lib"]
					else:
						print("Warning: Entrer les informations demandé")
				elif Cmaladie.acmal[ch]["desc"] == "":
					print("Entrer la nouvellle description textule pour cette categorie")
					choix = str(input())
					if choix != "":
						Cmaladie.acmal[ch]["desc"], choix = choix, Cmaladie.acmal[ch]["desc"]
					else:
						print("Warning: Entrer les informations demandé")
				else:
					del choix
					break
			Cmaladie.jsonSave("json/cmaladie.json",Cmaladie.acmal)
	def showDescipText(self):
		"""Fonction qui permet d'afficher la description textuelle d'un categorie"""
		Cmaladie.list(self)
		if Cmaladie.acmal != []:
			print("Entrer le numero de la categorie :",end=" ")
			ch = int(str(input()))
			while ch not in list(range(len(Cmaladie.acmal))): 
				print("Entrer un numero correct entre {} et {}".format(list(range(len(Cmaladie.acmal)))[0],list(range(len(Cmaladie.acmal)))[-1]))
				ch = int(str(input("Entrer le numero de la categorie : ")))
			print("Libelle : {}\nDescription textuellle : {}".format(Cmaladie.acmal[ch]["lib"],Cmaladie.acmal[ch]["desc"]))