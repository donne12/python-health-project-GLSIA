from operateur import *


class Maladie:
    def __init__(self, nom: str, description=" " ,sympto=[ ] ):
        
            self.nom = nom
            self.description = description  
            self.sympto =  sympto
                   

    # def __str__(self):
    #     return "{0} : {1}\nSymptôme: {2}\nTraitement: {3}\n".format(self.nom, self.description, ", ".join(self.sympto) ,self.traitement)

    # def __del__(self):
    #     data = lire("fichier.json")
    #     del data["Maladie"][
    #         data["Maladie"].index({
    #             "nom" : self.nom,
    #             "description" : self.description,
    #             "traitement" : self.traitement,
    #             "sympto": self.sympto
    #         })
    #     ]
    #     ecrire("fichier.json",data)
    #     print("Patient supprimer avec succes !")

    def create(self):
        data = lire("fichier.json")
        if(self.verification()==False):
            data["Maladie"].append(
                {
                    "nom" : self.nom,
                    "description" : self.description,
                    "sympto": self.sympto
                }
            )
            ecrire("fichier.json",data)
        else:
                   print("Cette maladie existe deja, veuillez reessayer !!")

    def verification(obj):
        data = lire("fichier.json")
        b= data["Maladie"]
        for maladie in  b:
                if((maladie["nom"]==obj.nom)):
                    return True
        return False
    
    # def AddSymptome(self):
    #     print("Symptome  de :{}...".format(self.nom, ))
    #     print("\n")
    #     symptome={
                    
    #                 "sphere_loin":    int(input("Entrez la valeur de la sphère lointaine : ")),       
    #                 "cylindre_loin":   int(input("Entrez la valeur du cylindre lointain : ")),       
    #                 "axe_loin":  int(input("Entrez la valeur de l'axe lointain : ")),       
    #                 "sphere_pres": int(input("Entrez la valeur de la sphère de près : ")),       
    #                 "cylinfre_pres": int(input("Entrez la valeur du cylindre de près : ")),       
    #                 "axe_pres": int(input("Entrez la valeur de l'axe de près : ")), 

    #                }
    #     data = lire("fichier.json")
    #     b = data["Maladie"]
    #     for maladie in  b:
    #         if((maladie["nom"]== self.nom)):
    #             maladie["symptome"]=symptome          
    #     ecrire("fichier.json",data)
    #     print(self)
    
    # def ModMaladie(self, nom: str, ):
    #     self.nom = nom 
    #     data = lire("fichier.json")
    #     if(self.verification()==False):
    #         b= data["Maladie"]
    #         for maladie in b:
    #             if(maladie[])
    #         ecrire("fichier.json",data)
    #     else:
    #                print("Cette maladie existe deja, veuillez reessayer !!")


    # def find(name: str):
    #     data = lire("fichier.json")
    #     for index,maladies in enumerate(data["Patient"]):
    #         for key in maladies:
    #             if name.lower() == key.lower():
    #                 nom = data["Maladie"][index]["nom"]
    #                 description = data["Maladie"][index]["description"]
    #                 sympto = data["Maladie"][index]["sympto"]
    #                 traitement = data["Maladie"][index]["traitement"]
    #                 return Maladie(nom,description,sympto,traitement)
    #     return None

    #  def update(self):
    #     data = lire("fichier.json")
    #     data["Maladie"][
    #         data["Maladie"].index({
    #             "nom" : self.nom,
    #             "description" : self.description,
    #             "traitement" : self.traitement,
    #             "sympto": self.sympto
    #         })
    #     ] = {
    #         "nom" : self.nom,
    #         "description" : self.description,
    #         "traitement" : self.traitement,
    #         "sympto": self.sympto
    #     }
    #     ecrire("fichier.json",data)

    # def search(recherche: str=''):
    #     data = lire("fichier.json")
    #     size = len(data["Maladie"])
    #     for index in range(size):
    #         m = Maladie.find(data["Maladie"][index]["nom"])
    #         if recherche.lower() in m.nom.lower():
    #             print(m)

# p1= Maladie("abcd","") 
# p1.create()
# p1.AddSymptome()
# p1.AddSymptome()
# p1.AddSymptome()
# p1= Maladie("abcd")
# p1.AddSymptome() 