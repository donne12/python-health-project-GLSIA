from operateur import *

class Maladie:
    def __init__(self, nom: str, description=" " ,sympto=[ ],id : int =0 ):
        self.nom = nom
        self.description = description  
        self.sympto =  sympto
        if id == 0:
            self.id = len(lire('fichier.json')['Maladie'])+1
        else:
            self.id = id

    # Méthode de création d'une nouvelle instance de maladie
    def create(self):
        data = lire("fichier.json")
        if(self.ifExists()==False):
            data["Maladie"].append({
                "id" : self.id,
                "nom" : self.nom,
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
            print(str(maladie['id'])+': -'+str(maladie['nom'].upper()))
            print('---------------------------------------------------------------------------------\n')
        
    # Méthode de récupération d'une maladie
    # Elle retourne une instance de Maladie
    def getMaladie(req):
        for maladie in lire('fichier.json')['Maladie']:
            if type(req) == str:
                if maladie["nom"] == req:
                    resultat = Maladie(
                        maladie['nom'],
                        maladie["description"],
                        maladie['sympto'],
                        maladie['id']
                    )
                    return resultat
            else:
                if maladie["id"] == req:
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
    
    # Petite méthode farfelue qui a été utile durant le back-end 😌😌
    # def toMaladie(args):
    #     try:
    #         maladie = Maladie() 
    #         maladie.id = args['id']
    #         maladie.nom = args['nom']       
    #         maladie.description = args['description']       
    #         maladie.sympto = args['sympto']    
    #         return maladie 
    #     except:
    #         return print("Le type de donnée n'est pas correcte")
    
    def desc(self):
        if self.ifExists() :
            print("Nom: "+str(self.nom))
            print("Description: "+str(self.description)+'\nListe des symptômes:')
            for sym in self.sympto:
                print('-'+str(sym))
            return
            # mplémenter les méthodes ou actions vers la mise à jour ou la suppression
            
        return print('Impossible d\'afficher un élément inexistant !!')
        
    # Méthode de suppresion d'une maladie 
    def deleteMaladie(self):
        if self.ifExists() :
            data = lire('fichier.json')
            try:
                for maladie in data['Maladie']:
                    if maladie['id'] == self.id:
                        del data['Maladie'][maladie['id']-1]
                        ecrire("fichier.json",data)
                        return print('Suppression effectuée avec succès !!:-)')
            except:
                return print("Une erreur est surevue durant l'opération !! :-(")
        return print('Impossible de supprimer un élément inexistant !!')
# -----------------------------------------Fin de la classe Maladie-----------------------------

# maladie = Maladie.getMaladie(6)
# if maladie.ifExists():
#     print('dfdfgfg')
#     print(maladie.nom)
# else:
#     print('boooom')