import cgi

print("content-type: text/html; charset=utf-8 \n")

html = """
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Page de connexion - Pediatrie</title>

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
    width: 300px;  
    height: 30px;  
    border: none;  
    border-radius: 17px;  
    padding-left: 7px;  
    color: slateblue;  
    cursor : pointer;
  
  
}  
span{  
    color: white;  
    font-size: 17px;  
}  
a{  
    float: right;  
    background-color: grey;  
}  

  </style>
  

</head>
<body>
   
    <h2>Page de connexion - Pediatrie</h2><br>    
    <div class="login">    
      <form id="login" method="post" action="Dashboard.py">    
          <label><b>Nom d'utilisateur </b></label>    
          <input type="text" name="username" id="Uname" placeholder="nom d'utilisateur">    
          <br><br>    
          <label><b>Mot de passe  </b> </label>    
          <input type="password" name="password" id="Pass" placeholder="mot de passe">    
          <br><br>    
          <input type="submit" name="log" id="log" value="Connexion">       
      </form>     
    </div>  
</body>
</html>
  
</body>
</html>
"""

print(html)
