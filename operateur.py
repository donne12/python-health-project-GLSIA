from typing import Dict

import json


def normalisation(fichier: str):
    try:
        f = open(fichier,"r", encoding="utf8")
        if f.read() == "":
            data = {
                "Patient": [],
                "Maladie": []
            }
            f.close()
            f = open(fichier, "w",encoding="utf8")
            json.dump(data, f, ensure_ascii=False, indent=4)
        f.close()
    except:
        f = open(fichier,"w+",encoding="utf8")
        data = {
                "Patient": [],
                "Maladie": []
        }
        f.close()

def ecrire(fichier: str, data):
    normalisation(fichier)
    f = open(fichier, "w", encoding="utf8")
    json.dump(data, f,indent=4,ensure_ascii=False)
    f.close()

def lire(fichier: str):
    normalisation(fichier)
    f = open(fichier, "r", encoding="utf8")
    data = json.load(f)
    f.close()
    return data

def verifier(critere: str="n"):
    if critere[0].lower() == "o":
        return True
    return False