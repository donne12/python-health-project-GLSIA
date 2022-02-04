import json
import os
from maladie import Maladie
class Traitement(object):
	"""Classe qui s'occupe de repertorier tous les types de traitements pour une maladie spécifique"""
	atrt = []
	def __init__(self,maladie="",desc=""):
		self.trt = {
			"maladie": maladie,
			"desc": desc
		}
	def jsonSave(filePath,subject):
		"""Fonction qui permet d'enregistrer un fichier json"""
		with open(filePath,"w",encoding="utf8") as file:
			json.dump(subject,file,ensure_ascii=False,indent=4)
		print("Enregistrer avec succes")
	def exist(filename):
		"""Permet de verifier si un fichier exist ou pas"""
		if os.path.exists(filename):
			return 1
		else: return 0;
	def load(self):
		"""Fonction qui permet de charger tous les types de traitements pour une maladie"""
		if Traitement.exist("json/traitement.json"):
			with open("json/traitement.json") as file:
				Traitement.atrt = json.load(file)
	def desc(self):
		"""Permet de renseigner les informations concernant les traitements pour une maladie"""
		choix = ""
		while choix == "":
			if self.trt["maladie"] == "":
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
					
					choix = Maladie.amal[ch]["nom"]
				if choix != "": 
					self.trt["maladie"], choix = choix, self.trt["maladie"]
				else:
					print("Warning: Entrer les informations demandé")
			elif self.trt["desc"] == "":
				print("Entrer les traitements à suivre pour cette maladie")
				choix = str(input())
				if choix != "":
					self.trt["desc"], choix = choix, self.trt["desc"]
				else:
					print("Warning: Entrer les informations demandé")
			else:
				del choix
				break
	def add(self):
		"""Fonction qui permet d'ajouter un traitement pour une maladie"""
		if self.trt["maladie"] == "" or self.trt["desc"] == "":
			Traitement.desc(self)
		if Traitement.atrt == []:
			Traitement.load(self)
		Traitement.atrt.append(self.trt)
		Traitement.jsonSave("json/traitement.json",Traitement.atrt)
	def list(self):
		"""Fonction qui permet de lister les traitements pour une maladie"""
		if Traitement.atrt == []:
			Traitement.load(self)
		if Traitement.atrt != []:
			print("======= listes des maladie qui ont un traitement =======")
			for i in list(range(len(Traitement.atrt))):
				print("		{} : {}".format(i,Traitement.atrt[i]["maladie"]))
		else:
			print("Desolé il n'y a aucun traitement pour des maladies enregistrer")
	def modify(self):
		"""Fonction qui permet de modifer les traitment pour une maladie"""
		Traitement.list(self)
		if Traitement.atrt != []:
			print("Entrer le numero de la maladie dont vous souhaiter modifier le traitemet:",end=" ")
			ch = int(str(input()))
			while ch not in list(range(len(Traitement.atrt))): 
				print("Entrer un numero correct entre {} et {}".format(list(range(len(Traitement.atrt)))[0],list(range(len(Traitement.atrt)))[-1]))
				ch = int(str(input("Entrer le numero de la categorie à modifier : ")))
			
			print("Pret à modifier la ligne {} ".format(Traitement.atrt[ch]))
			choix = ""
			Traitement.atrt[ch]["desc"] = ""
			while choix == "":
				if Traitement.atrt[ch]["desc"] == "":
					print("Entrer les nouveaux traitements à suivre pour cette maladie")
					choix = str(input())
					if choix != "":
						Traitement.atrt[ch]["desc"], choix = choix, Traitement.atrt[ch]["desc"]
					else:
						print("Warning: Entrer les informations demandé")
				else:
					del choix
					break
			Traitement.jsonSave("json/traitement.json",Traitement.atrt)
	def showDescipText(self):
		"""Fonction qui permet d'afficher la description textuelle d'un categorie"""
		Traitement.list(self)
		if Traitement.atrt != []:
			print("Entrer le numero de la maladie dont vous souhaiter afficher les traitements :",end=" ")
			ch = int(str(input()))
			while ch not in list(range(len(Traitement.atrt))): 
				print("Entrer un numero correct entre {} et {}".format(list(range(len(Traitement.atrt)))[0],list(range(len(Traitement.atrt)))[-1]))
				ch = int(str(input("Entrer le numero de la maladie dont vous souhaiter afficher les traitements :")))
			print("Maladie : {}\nTraitements : {}".format(Traitement.atrt[ch]["maladie"],Traitement.atrt[ch]["desc"]))