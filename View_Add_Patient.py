import cgi

print("content-type: text/html; charset=utf-8 \n")

html = """
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Ajouter un patient - Pediatrie</title>

  <style>

  body  
{  
    margin: 0;  
    padding: 0;  
    background-color:white;  
    font-family: 'Arial';  
}  
.login{  
        width: 800px;  
        overflow: hidden; 
        margin: auto; 
        margin: 20 20 0 450px;  
        padding: 80px;  
        background: #23463f;  
        border-radius: 20px ;  
          
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
    height: 60px;  
    border: none;   
    padding-left: 7px;  
    color: white;  
    cursor : pointer;
    float : right;
    background-color: #277582;
    box-sizing: border-box;
    border-style: groove;
}  

span{  
    color: white;  
    font-size: 17px;  
}  
a{  
    float: right;  
    background-color: grey;  
}  
.reg{
   display: inline-block;
    align-items: flex-start;
 }

 .regl{
     float:left ;   width:50% ; margin-left: auto;	margin-right: auto;
 }

 .regr{
      float:right; width:50%  ;	margin-right: auto; margin-left: auto;
 }

  </style>
  

</head>
<body>
   
    <h2>Ajouter un patient </h2><br>    
    <div class="login">    
      <form id="login" method="post" action="Dashboard.py">    
        <div class="regl">
          <label><b>Matricule du patient </b></label>    
          <input type="text" name="matricule" id="Uname" placeholder="matricule">  
        </div>   
          
        <div class="regr"> 
          <label><b>Nom du patient  </b></label>    
          <input type="text" name="nom" id="Pass" placeholder="nom">  
        </div>   

          <br><br>    
          <br><br>   

        <div class="regl">
          <label><b>Prenom du patient  </b></label>    
          <input type="text" name="prenom" id="Pass" placeholder="prenom">  
        </div>  

        <div class="regr">
          <label><b>Age du patient  </b></label>    
          <input type="number" name="age" id="Pass" >  
        </div>  

          <br><br>    
          <br><br>   
          <br><br>
          <input type="submit" name="log" id="log" value="Ajouter">       
      </form>     
    </div>  
</body>
</html>
  
</body>
</html>
"""

print(html)
