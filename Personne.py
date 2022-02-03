#La classe Personne est la classe par défaut pour tout individu
import json
from os import path, system


def authentication():
    try:
        print("------- Veuillez vous authentifiez pour continuer -----\n")
        login = input("Login: ")
        password = input("Password: ")
        f = open("user.json", "r", encoding="utf8")
        users = json.load(f)
        f.close()
        for user in users:
            if (user["login"] == login) and (user["password"] == password):
                return True
        return False
    except:
        if not path.exists("user.json"):
            print("Système d'authentification réinstallé !")
            print("Veuillez contacter l'administrateur")
            f = open("user.json", "w+", encoding="utf8")
            json.dump(
                [
                    {
                        "login": "Admin",
                        "password": "1234"
                    }
                ],
                f, indent=4, ensure_ascii=False
            )
        else:
            print("Erreur fatal - Contacter l'administrateur")
        system("pause")
        return False
class  Personne:
    def __init__(self, nom: str, prenom: str, adresse: str, age: int):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.age = age
    def __str__(self) :
        return self.nom + " " + self.prenom + " " + str(self.age) + "ans " + self.adresse
