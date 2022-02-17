import json

# convertir une liste en chaine
def listToString(s): 
    
    str1 = ", " 

    return (str1.join(s))

        


def autoIncrement(fichier:str, pas: int, key : str) :
    with open("Database/"+fichier,"r", encoding="utf8") as file:
        j = json.load(file)
        if len(j[key]) != 0 :
           id = j[key][-1]["id"] + pas
        else :
           id = 0
        return id


# charger les données du fichier json authusers
def loadAuthUsersStore() :
    data = open("Database/AuthUsers.json","r", encoding="utf8")
    store = json.loads(data.read())
    data.close()
    return store




# enregistrer les données dans le fichier json patient
def addNewInPatientStore(data):
    with open("Database/Patient.json","r+", encoding="utf8") as file:
        j = json.load(file)
        for v in data :
            j['patient'].append(v)
        file.seek(0)
        json.dump(j,file,indent=4,ensure_ascii=False)


# charger les données dans le fichier json maladie
def loadPatientStore() :
    data = open("Database/Patient.json","r", encoding="utf8")
    store = json.loads(data.read())
    data.close()
    return store


def editNewInPatientStore(data, id):
    with open("Database/Patient.json","r+", encoding="utf8") as f:
        j= json.load(f)
        y = next((x for x in j['patient'] if x["id"] == id), None)
        if not y == None : 
            j['patient'][id]["nom"] = data[0]["nom"] 
            j['patient'][id]["prenom"] = data[0]["prenom"] 
            j['patient'][id]["age"] = data[0]["age"] 
            j['patient'][id]["adresse"] = data[0]["adresse"] 
            j['patient'][id]["contact"] = data[0]["contact"] 
            j['patient'][id]["poids"] = data[0]["poids"] 
            j['patient'][id]["taux_glycémie"] = data[0]["taux_glycémie"] 
            j['patient'][id]["groupe_sanguin"] = data[0]["groupe_sanguin"] 
            j['patient'][id]["symptomes"] = data[0]["symptomes"] 
            f.seek(0)        
            json.dump(j, f, indent=4, ensure_ascii=False)
            f.truncate()     
            print("\033[92m"+"Patient modifié avec succès!!"+"\033[0m")
        else :
            print("\033[91m"+"Aucun patient ayant cet identifiant.. !!!!!!!!!!!!!!"+"\033[0m")


def deleteNewInPatientStore(id) :
    with open("Database/Patient.json","r+", encoding="utf8") as f:
        j= json.load(f)
        y = next((x for x in j['patient'] if x["id"] == id), None)
        if not y == None : 
            del j['patient'][id]
            f.seek(0)        
            json.dump(j, f, indent=4, ensure_ascii=False)
            f.truncate()     
            print("\033[92m"+"Patient supprimé avec succès!!"+"\033[0m")
        else :
            print("\033[91m"+"Aucun patient ayant cet identifiant.. !!!!!!!!!!!!!!"+"\033[0m")


def addConsultationInPatientStore(data, id) :
    with open("Database/Patient.json","r+", encoding="utf8") as file:
        j = json.load(file)
        y = next((x for x in j['patient'] if x["id"] == id), None)
        if not y == None : 
            for v in data :
                j['patient'][id]["consultations"].append(v)
            file.seek(0)
            json.dump(j,file,indent=4,ensure_ascii=False)
            file.truncate()
            print("\033[92m"+"Consultation ajouté avec succès!!"+"\033[0m")
        else :
            print("\033[91m"+"Aucun patient ayant cet identifiant.. !!!!!!!!!!!!!!"+"\033[0m")


def addResultatInPatientStore(data, id) :
    with open("Database/Patient.json","r+", encoding="utf8") as file:
        j = json.load(file)
        y = next((x for x in j['patient'] if x["id"] == id), None)
        if not y == None : 
            for v in data :
                j['patient'][id]["resultats"].append(v)
            file.seek(0)
            json.dump(j,file,indent=4,ensure_ascii=False)
            file.truncate()
            print("\033[92m"+"Résultat ajouté avec succès!!"+"\033[0m")
        else :
            print("\033[91m"+"Aucun patient ayant cet identifiant.. !!!!!!!!!!!!!!"+"\033[0m")
    


# charger les données dans le fichier json maladie
def loadMaladieStore() :
    data = open("Database/Maladie.json","r", encoding="utf8")
    store = json.loads(data.read())
    data.close()
    return store
   
    

# enregistrer les données dans le fichier json maladie
def addNewInMaladieStore(data):
    with open("Database/Maladie.json","r+", encoding="utf8") as file:
        j = json.load(file)
        for v in data :
            j['maladie'].append(v)
        file.seek(0)
        json.dump(j,file,indent=4,ensure_ascii=False)


def editNewInMaladieStore(data, id):
    with open("Database/Maladie.json","r+", encoding="utf8") as f:
        j= json.load(f)
        y = next((x for x in j['maladie'] if x["id"] == id), None)
        if not y == None : 
            j['maladie'][id]["nom"] = data[0]["nom"] 
            j['maladie'][id]["département"] = data[0]["département"] 
            j['maladie'][id]["symptomes"] = data[0]["symptomes"] 
            f.seek(0)        
            json.dump(j, f, indent=4, ensure_ascii=False)
            f.truncate()     
            print("\033[92m"+"Maladie modifié avec succès!!"+"\033[0m")
        else :
            print("\033[91m"+"Aucune maladie ayant cet identifiant.. !!!!!!!!!!!!!!"+"\033[0m")


def deleteNewInMaladieStore(id) :
    with open("Database/Maladie.json","r+", encoding="utf8") as f:
        j= json.load(f)
        y = next((x for x in j['maladie'] if x["id"] == id), None)
        if not y == None : 
            del j['maladie'][id]
            f.seek(0)        
            json.dump(j, f, indent=4, ensure_ascii=False)
            f.truncate()     
            print("\033[92m"+"Maladie supprimé avec succès!!"+"\033[0m")
        else :
            print("\033[91m"+"Aucune maladie ayant cet identifiant.. !!!!!!!!!!!!!!"+"\033[0m")
    
    


    


