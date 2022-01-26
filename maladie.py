from operateur import *


class Maladie:
    def __init__(self, nom: str, description=" " ,sympto=[ ],id : int =0 ):
        self.nom = nom
        self.description = description  
        self.sympto =  sympto
        if id == 0:
            self.id = lire('fichier.json')['Maladie'][-1]['numero']+1
        self.id = 1
        
    def __init__(self):
        self.nom = ''
        self.description = ''
        self.sympto = ''
        self.id = 0

    def create(self):
        data = lire("fichier.json")
        if(self.ifExists()==False):
            data["Maladie"].append(
                {
                    "nom" : self.nom,
                    "description" : self.description,
                    "sympto": self.sympto
                }
            )
            ecrire("fichier.json",data)
        else:
            print("Cette maladie existe déjà, veuillez reessayer !!")

    # Méthode qui vérifie si une maladie est déjç repertoriée
    def ifExists(self):
        for maladie in  lire("fichier.json")["Maladie"]:
            if(maladie["id"] == self.id):
                return True
        return False
    
    # Méthode qui retourne la liste des maladies avec leurs symptômes
    def listMaladies():
        maladies = lire('fichier.json')['Maladie']
        for maladie in maladies:
            print(str(maladie['nom'].upper()))
            print('Ses symptômes sont: ')
            for symptome in maladie["sympto"]:
                print("\t-"+str(symptome))
            print('---------------------------------------------------------------------------------\n')
        
    # Méthode de récupération d'une maladie
    # Elle retourne un dictionnaire
    def getMaladie(id : int):
        maladies = lire('fichier.json')['Maladie']
        for maladie in maladies:
            if maladie["id"] == id:
                return maladie
        return None
    
        
    def updateMaladie(self):
        if self.ifExists() == True:
            try:
                data = lire('fichier.json')
                maladies = data['Maladie']
                for maladie in maladies:
                    if maladie['id'] == self.id:
                        print(str(maladie['id']))
                        maladie['nom'] = self.nom
                        maladie['description'] = self.description
                        maladie['sympto'] = self.sympto
                ecrire('fichier.json',data)
                print('Modification appliquées avec succès :-)')
            except:
                return print("Une erreur s'est produite durant l'opération :-( ")
        
    def toMaladie(args):
        try:
            maladie = Maladie() 
            maladie.id = args['id']
            maladie.nom = args['nom']       
            maladie.description = args['description']       
            maladie.sympto = args['sympto']    
            return maladie 
        except:
            return print("Le type de donnée n'est pas correcte")
                
        
maladie = Maladie.toMaladie(Maladie.getMaladie(1))
maladie.nom = "hypermétropie"
# maladie.nom = input("Entrez le nouveau nom de la maladie: ")
maladie.updateMaladie()

if not maladie.ifExists():
    print('dfdfgfg')
else:
    print('boooom')