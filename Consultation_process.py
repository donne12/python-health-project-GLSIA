import cgi
import cgitb
from Models import *
from Functions import *

#Puisqu'il est utilisé pour le débogage, il n'est pas décrit dans l'environnement de production.
cgitb.enable()

#Obtenir les données du formulaire
form = cgi.FieldStorage()

print("Content-type: text/html; charset=utf-8 \n")

if form.getvalue("matricule") and form.getvalue("nomPatient") \
and form.getvalue("prenomPatient") and form.getvalue("adressePatient") \
and form.getvalue("contactPatient") and form.getvalue("poidsPatient") \
and form.getvalue("agePatient") and form.getvalue("taux_glyc") \
and form.getvalue("groupe_sanguin") and form.getvalue("symptomes") \
and form.getvalue("nomMedecin") and form.getvalue("prenomMedecin") \
and form.getvalue("contactMedecin") :
    matricule = str(form.getvalue("matricule"))
    nomPatient = str(form.getvalue("nomPatient"))
    prenomPatient = str(form.getvalue("prenomPatient"))
    adressePatient = str(form.getvalue("adressePatient"))
    contactPatient = str(form.getvalue("contactPatient"))
    poidsPatient = form.getvalue("poidsPatient")
    agePatient = form.getvalue("agePatient")
    taux_glyc = form.getvalue("taux_glyc")
    groupe_sanguin = str(form.getvalue("groupe_sanguin"))
    symptomes = str(form.getvalue("symptomes"))
    nom_medoc = str(form.getvalue("nomMedecin"))
    prenom_medoc = str(form.getvalue("prenomMedecin"))
    contact_medoc = str(form.getvalue("contactMedecin"))
    p = Patient(matricule, nomPatient, prenomPatient, agePatient, adressePatient, contactPatient, poidsPatient, taux_glyc, groupe_sanguin, symptomes)
    res = p.consult(nom_medoc, prenom_medoc, contact_medoc)
    if(res == True) :
      html = f"""
      <!DOCTYPE html>
<html>
  <head>
    <title>Traitement consultation</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta charset="UTF-8">

    <body>
       <h2 style="color: green;">Consultation enregistré avec succès</h2>
  </body>
</html>
      """
    else :
      html = """
    <!DOCTYPE html>
    <html lang="en" >
    <head>
    <meta charset="UTF-8">
    <title>Erreur</title>
    <head>

    
</head>
    <body>
<div>
  <h1>Erreur !</h1>
  <p>Erreur!</p>
      <a href="/View_Consultation.py">Revenir</a>
</div>

    </body>
    </html>
    """
    print(html)


else :
    html = """
    <!DOCTYPE html>
    <html lang="en" >
    <head>
    <meta charset="UTF-8">
    <title>Erreur</title>
    <head>

    
  </head>
    <body>
<div>
  <h1>Erreur !</h1>
  <p>Informations requises non saisies!</p>
  <div >
    <div >
      <a href="/Login.py" >Revenir</a>
    </div>
  </div>
</div>

    </body>
    </html>
    """
    print(html)


