import cgi
from Models import *
from Functions import *


value = Maladie.read()

print("Content-type: text/html; charset=utf-8 \n")

html1 = """
<!DOCTYPE html>
<html lang="fr" >
<head>
  <meta charset="UTF-8">
  <title>Les maladies - Pédiatrie</title>
  
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
 

  </style>

</head>
"""

print(html1)

html2 = """<body>
    <table border=2 width="80%">
   <caption><h1>QUELQUES MALADIES COURANTES</h1></caption>

   <thead> 
       <tr>
           <th>Nom</th>
           <th>Symptomes</th>
           <th>Departement</th>
       </tr>
   </thead>

   <tbody> 
"""
print(html2)

for x, y in value.items() :
    print("<tr>")
    print("<td>{}</td>".format(y["nom"]))
    print("<td>{}</td>".format(listToString(y["symptomes"])))
    print("<td>{}</td>".format(y["département"]))
    print("</tr>")

print("</tbody>") 
print("</table>") 

print("<br/>")
print("<br/>")
print("<button id='log' onclick='history.back(-1)'>Retour</button>")
print("</body>") 
print("</html>") 




