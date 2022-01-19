import datetime
import systemd
import crypt
import json


def title(message):
    print('\n****** ****** ***** ***** *****')
    print('\t', message)
    print('****** ****** ***** ***** *****\n')

# Connexion à l'application
def login(username: str, password: str):
    online = get("users")
    for i in online:
        # recréer le mot de passe hashé existant
        b = crypt.crypt(password, i['password'])

        # Vérifier si les identifiants sont corrects
        if (b == i['password']) and (i['username'] == username):
            return True
    return False

# Ajouter un utilisateur à l'application
def add_user(data: {}):
    data["password"] = crypt.crypt(data["password"], crypt.METHOD_MD5)
    write("users", data)

# Modifier l'utilisateur connecté
def update_user(username: str, password: str):
    with open('json/data.json') as myFile:
        file_data = json.load(myFile)
    cpt = 0
    for i in file_data["users"]:
        if i["username"] == username:
            file_data["users"][cpt]["password"] = crypt.crypt(password, crypt.METHOD_MD5)
            break
        cpt += 1

    with open('json/data.json', 'w', encoding='utf-8') as myFile:
        json.dump(file_data, myFile)
    myFile.close()
    print('\nMot de passe modifié!!!')

# Fonction pour enregistrer un élement (data) d'une classe dans le fichier json
def write(classe: str, data: {}):
    with open('json/data.json') as myFile:
        file_data = json.load(myFile)

    # Ajoute la nouvelle donnée
    file_data[classe].append(data)

    with open('json/data.json', 'w', encoding='utf-8') as myFile:
        json.dump(file_data, myFile)
    myFile.close()
    print('Enregistrement réussi!!!')

# Fonction pour modifier un élement (data) d'une classe dans le fichier json
def rewrite(classe: str, data: {}):
    with open('json/data.json') as myFile:
        file_data = json.load(myFile)

    cpt = 0
    for i in file_data[classe]:
        if i["id"] == data["id"]:
            file_data[classe][cpt] = data
            break
        cpt += 1

    with open('json/data.json', 'w', encoding='utf-8') as myFile:
        json.dump(file_data, myFile)
    myFile.close()
    print('\nModification réussi!!!')

# Fonction pour afficher la liste des élements d'une classe et de retourner les données
def read(classe: str):
    with open('json/data.json') as myFile:
        file_data = json.load(myFile)
    if len(file_data) == 0:
        print("Il n'existe pas d\'enregistrement.")
    else:
        title('Liste des '+ classe)
        for elt in file_data[classe]:
            print(elt)
    return file_data[classe]

# Fonction pour retourner les données d'une classe
def get(classe: str):
    with open('json/data.json') as myFile:
        file_data = json.load(myFile)
    return file_data[classe]

# Fonction pour récupérer un élément d'une liste grace à son identifiant
def get_element(data, id: str):
    for elt in data:
        if elt['id'] == id:
            return elt
    print('Identifiant inexistant.')