from operateur import *

class Maladie:
    def __init__(self, nom: str, description=" " ,sympto=[ ],id : int =0 ):
        self.nom = nom
        self.description = description  
        self.sympto =  sympto
        if id == 0:
            oid : str = str(len(lire('fichier.json')['Maladie']))+nom
            self.id = oid
        else:
            self.id = str(0)+nom

    # Méthode de création d'une nouvelle instance de maladie
    def create(self):
        data = lire("fichier.json")
        if(self.ifExists()==False):
            data["Maladie"].append({
                "id" : self.id,
                "nom" : self.nom.lower(),
                "description" : self.description,
                "sympto": self.sympto
            })
            ecrire("fichier.json",data)
            return print("----------------------Maladie ajoutée avec success----------------------\n")
        else:
            print("Cette maladie est déjà enregistrée!!")
            return self.desc()

    # Méthode qui vérifie si une maladie est déja repertoriée
    def ifExists(self):
        try:
            for maladie in lire("fichier.json")["Maladie"]:
                if(maladie['id'] == self.id) or (str(maladie['nom']).lower() == self.nom.lower()):
                    return True
            return False
        except :
            pass
    
    # Méthode qui retourne la liste des maladies avec leurs symptômes
    def listMaladies():
        maladies = lire('fichier.json')['Maladie']
        for maladie in maladies:
            print(str(maladie['nom']).upper())
            print('---------------------------------------------------------------------------------\n')
        
    # Méthode de récupération d'une maladie
    # Elle retourne une instance de Maladie
    def getMaladie(req):
        for maladie in lire('fichier.json')['Maladie']:
            if maladie["nom"] == req:
                resultat = Maladie(
                    maladie['nom'],
                    maladie["description"],
                    maladie['sympto'],
                    maladie['id']
                )
                return resultat
        return print("Maladie inexistante !! :-(")
    
    # Méthode de mise à jour d'une maladie
    def updateMaladie(self):
        if self.ifExists() == True:
            try:
                data = lire('fichier.json')
                maladies = data['Maladie']
                for maladie in maladies:
                    if maladie['id'] == self.id:
                        maladie['nom'] = self.nom.lower()
                        maladie['description'] = self.description
                        maladie['sympto'] = self.sympto
                ecrire('fichier.json',data)
                print('Modification appliquées avec succès :-)')
                return
            except:
                return print("Une erreur s'est produite durant l'opération :-( ")
    
    def desc(self):
        if self.ifExists() :
            print("Nom: "+str(self.nom))
            print("Description: "+str(self.description)+'\nListe des symptômes:')
            for sym in self.sympto:
                print('-'+str(sym))
            return
            
        return print('Impossible d\'afficher un élément inexistant !!')

        
        
# -----------------------------------------Fin de la classe Maladie-----------------------------
