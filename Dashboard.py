#import requests

import cgi
import cgitb
from Models import Auth

#Puisqu'il est utilisé pour le débogage, il n'est pas décrit dans l'environnement de production.
cgitb.enable()

#Obtenir les données du formulaire
form = cgi.FieldStorage()

print("Content-Type: text/html; charset=UTF-8") #En-tête pour écrire du HTML
print("")

if form.getvalue("username") and form.getvalue("password"):
    username = str(form.getvalue("username"))
    password = str(form.getvalue("password")).encode('utf-8')
    a = Auth(username, password)
    res = a.checkUser()
    if(res == True) :
      #webbrowser.open('localhost/login.py', new=0, autoraise=True)
      html = """
      <!DOCTYPE html>
<html>
  <head>
    <title>Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta charset="UTF-8">

<style>

  body  
{  
    margin: 0;  
    padding: 0;  
    background-color:white;  
    font-family: 'Arial';  
}  
.login{  
        width: 382px;  
        overflow: hidden;  
        margin: auto;  
        margin: 20 0 0 450px;  
        padding: 80px;  
        background: #23463f;  
        border-radius: 15px ;  
          
}  
h2{  
    text-align: center;  
    color: #277582;  
    padding: 5px;  
}  
label{  
    color: #08ffd1;  
    font-size: 17px;  
}  
#Uname{  
    width: 300px;  
    height: 30px;  
    border: none;  
    border-radius: 3px;  
    padding-left: 8px;  
}  
#Pass{  
    width: 300px;  
    height: 30px;  
    border: none;  
    border-radius: 3px;  
    padding-left: 8px;  
      
}  
#log{  
    width: 100px;  
    height: 30px;  
    border: none;  
    border-radius: 30px;  
    padding-left: 7px;  
    color: red;  
    cursor : pointer;
}  

span{  
    color: white;  
    font-size: 17px;  
}  
 
 a{
   color : black;
 }
 a:visited {
   color : black;
 }

  </style>

     
</head>
"""
      print(html)

      html2 = f"""
          <body>
            <h2>Vous etes connectes.. {username}!!</h2>
            <h2><a href="/Login.py" >Se deconnecter</a></h2>
            <br/>
            <hr/>
            <h3>Bienvenue sur notre API. </h3>
            <h2>Vous pouvez : </h2>
            <ul>
              <li><h2><a href="/View_Maladie.py">Voir les maladies courantes en pediatrie</a></h2></li>
              <li><h2><a href="/View_Add_Patient.py">Enregistrer un nouveau patient</a></h2></li>
              <li><h2><a href="/View_Consultation.py">Consulter un patient</a></h2></li>
              <li><h2><a href="/View_Ajouter_Maladie.py">Enregistrer une nouvelle pathologie</a></h2></li>
              <li><h2><a href="/View_Liste_Consultation.py">Liste des patients consultes</a></h2></li>
              <li><h2><a href="/View_Resultat_Traitement.py">Voir les resultats des traitements sur un patient</a></h2></li>
            </ul>
        </body>
      </html>
            """
      print(html2)
    else :
      html = """
    <!DOCTYPE html>
    <html lang="en" >
    <head>
    <meta charset="UTF-8">
    <title>Erreur</title>
    <head>

    <style>

  body  
{  
    margin: 0;  
    padding: 0;  
    background-color:white;  
    font-family: 'Arial';  
}  
.login{  
        width: 382px;  
        overflow: hidden;  
        margin: auto;  
        margin: 20 0 0 450px;  
        padding: 80px;  
        background: #23463f;  
        border-radius: 15px ;  
          
}  
h2{  
    text-align: center;  
    color: #277582;  
    padding: 20px;  
}  
label{  
    color: #08ffd1;  
    font-size: 17px;  
}  
#Uname{  
    width: 300px;  
    height: 30px;  
    border: none;  
    border-radius: 3px;  
    padding-left: 8px;  
}  
#Pass{  
    width: 300px;  
    height: 30px;  
    border: none;  
    border-radius: 3px;  
    padding-left: 8px;  
      
}  
#log{  
    width: 100px;  
    height: 30px;  
    border: none;  
    border-radius: 30px;  
    padding-left: 7px;  
    color: red;  
    cursor : pointer;
}  

span{  
    color: white;  
    font-size: 17px;  
}  
 

  </style>

    
</head>
    <body>
<div>
  <h1>Erreur !</h1>
  <p>Informations invalides!</p>
      <button id="log"><a href="/Login.py">Revenir</a></button>
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

 <style>

  body  
{  
    margin: 0;  
    padding: 0;  
    background-color:white;  
    font-family: 'Arial';  
}  
.login{  
        width: 382px;  
        overflow: hidden;  
        margin: auto;  
        margin: 20 0 0 450px;  
        padding: 80px;  
        background: #23463f;  
        border-radius: 15px ;  
          
}  
h2{  
    text-align: center;  
    color: #277582;  
    padding: 20px;  
}  
label{  
    color: #08ffd1;  
    font-size: 17px;  
}  
#Uname{  
    width: 300px;  
    height: 30px;  
    border: none;  
    border-radius: 3px;  
    padding-left: 8px;  
}  
#Pass{  
    width: 300px;  
    height: 30px;  
    border: none;  
    border-radius: 3px;  
    padding-left: 8px;  
      
}  
#log{  
    width: 100px;  
    height: 30px;  
    border: none;  
    border-radius: 30px;  
    padding-left: 7px;  
    color: red;  
    cursor : pointer;
}  

span{  
    color: white;  
    font-size: 17px;  
}  
 

  </style>
    
  </head>
    <body>
<div>
  <h1>Erreur !</h1>
  <p>Informations requises non saisies!</p>
  <div >
    <div >
      <button id="log"><a href="/Login.py" >Revenir</a></button>
    </div>
  </div>
</div>

    </body>
    </html>
    """
    print(html)
    #sys.exit()
   



