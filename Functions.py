import json

# convertir une liste en chaine
def listToString(s): 
    
    str1 = ", " 

    return (str1.join(s))


# charger les données du fichier json authusers
def loadAuthUsersStore() :
    data = open("Data/AuthUsers.json","r", encoding="utf8")
    store = json.loads(data.read())
    data.close()
    return store

# charger les données de consultation du fichier json consultation
def loadConsultation() :
    data = open("Data/Consultation.json","r", encoding="utf8")
    store = json.loads(data.read())
    data.close()
    return store

# enregistrer les données de consultation dans le fichier json consultation
def addNewConsultation(data):
    with open("Data/Consultation.json","r+", encoding="utf8") as file:
        j = json.load(file)
        for k, v in data.items() :
            j['consultation'][k] = v
        file.seek(0)
        json.dump(j,file,indent=4,ensure_ascii=False)

def addNewDiagnostic(data):
    with open("Data/Diagnostic.json","r+", encoding="utf8") as file:
        j = json.load(file)
        for k, v in data.items() :
            j['diagnostic'][k] = v
        file.seek(0)
        json.dump(j,file,indent=4,ensure_ascii=False)

# charger les données dans le fichier json maladie
def loadMaladieStore() :
    data = open("Data/Maladie.json","r", encoding="utf8")
    store = json.loads(data.read())
    data.close()
    return store

# enregistrer les données dans le fichier json maladie
def addNewInMaladieStore(data):
    with open("Data/Maladie.json","r+", encoding="utf8") as file:
        j = json.load(file)
        for k, v in data.items() :
            j['maladie'][k] = v
        file.seek(0)
        json.dump(j,file,indent=4,ensure_ascii=False)


