import cgi
from Models import *
from Functions import *

print("Content-type: text/html; charset=utf-8 \n")


html = """
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Consultation - Pédiatrie</title>
  

  
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
    color: black;  
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
  <div class="login">   
    <form method="post" action="Consultation_process.py">
        <h1>Faire une consultation</h1>

        <label for="matricule">Matricule :</label>
        <input type="text" placeholder="matricule" id="matricule" name="matricule" >


        <label for="nomPatient">Nom du patient :</label>
        <input type="text" placeholder="nom du patient" id="nomPatient" name="nomPatient">

        <br/>
        <br/>

        <label for="prenomPatient">Prenom du patient :</label>
        <input type="text" placeholder="prenom du patient" id="prenomPatient" name="prenomPatient">

        <label for="adressePatient">Adresse du patient :</label>
        <input type="text" placeholder="adresse du patient" id="adressePatient" name="adressePatient">

        <br/>
        <br/>

        <label for="contactPatient">Contact du patient :</label>
        <input type="text" placeholder="contact du patient" id="contactPatient" name="contactPatient">

        <label for="poids">Poids du patient :</label>
        <input type="number" placeholder="poids du patient" id="poidsPatient" name="poidsPatient">

        <label for="age">Age du patient :</label>
        <input type="number" placeholder="age du patient" id="agePatient" name="agePatient">

        <br/>
        <br/>

        <label for="taux_glyc">Taux de glycemie du patient :</label>
        <input type="number" placeholder="taux de glycemie du patient" id="taux_glyc" name="taux_glyc">

        <label for="groupe_sanguin">Groupe sanguin du patient :</label>
        <input type="text" placeholder="groupe sanguin du patient" id="groupe_sanguin" name="groupe_sanguin">

        <br/>
        <br/>

        <label for="taux_glyc">Symptomes du patient separe par des virgules:</label>
        <Textarea name="symptomes" rows=6 cols=20></textarea>

        <label for="nomMedecin">Nom du medecin traitant :</label>
        <input type="text" placeholder="nom du medecin traitant" id="nomMedecin" name="nomMedecin">

        <br/>
        <br/>
        
        <label for="prenomMedecin">Prenom du medecin traitant :</label>
        <input type="text" placeholder="prenom du medecin traitant" id="prenomMedecin" name="prenomMedecin">

        <label for="contactMedecin">Contact du medecin traitant :</label>
        <input type="text" placeholder="contact du medecin traitant" id="contactMedecin" name="contactMedecin">



        <br/>
        <br/>
        <br/>
        <br/>

        <center><button type='submit'>Enregistrer</button></center>
    </form>
    </div>  

    <br/>
    <br/>

    <button onclick="history.back(-1)">Retour</button>
</body>
</html>
  
</body>
</html>
"""

print(html)