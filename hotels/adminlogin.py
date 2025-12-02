#!C:/Users/pirat/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql,cgi,cgitb,os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="hotel")
cur = con.cursor()
print("""
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Admin Login</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<style>
  .card {
    box-shadow: 0px 0px 8px black;
    padding: 20px;
    margin-top: 20px;
    background-image: url(./media/admlog1.jpg);
    background-repeat: no-repeat;
    background-size: cover;
  }



  label {
    color: white;
    font-family: bold;
    font-size: 20px;
  }
</style>

<body class="bg-light">
  <!-- logo -->
  <div class="container-fluid" style="background-color:rgb(235, 216, 216);">
    <center>
      <img src="./media/logo.PNG" alt="logo" height="150px" width="200px">
    </center>
  </div>
  <!-- logo end -->

  <div class="container " style="margin-bottom: 150px;margin-top: 100px;">
    <div class="row">
      <div class="col-md-3"></div>
      <div class="col-md-6">
        <form method="post" enctype="Multipart/form-data">
          <div class="card bg-info">
            <div class="form-group">
              <center>
                <h2 style="color:white;font-family: bold;">Admin login </h2>
              </center>
              <label for="">User Name</label>
              <input type="text" class="form-control" name="usr" id="email">
              <label for="">Password</label>
              <input type="password" class="form-control" name="psw" id="password">
              <center>
                <input type="submit" value="login" class="btn btn-success btn-lg" style="margin-top: 20px;" name="sub">
                <input type="reset" value="cancel" class="btn btn-danger btn-lg" style="margin-top: 20px;"><br><br>
              
              </center>

            </div>
          </div>
        </form>
      </div>
      <div class="col-md-3"></div>

    </div>
  </div>
  <!-- Modal -->
  
  <!-- footer  -->
  <div class="container-fluid" style="background-color: rgb(71, 9, 14);padding-top: 40px;">
    <div class="row">
      <div class="col-sm-3"></div>
      <div class="col-md-6">
        <span class="glyphicon glyphicon-map-marker" style="font-size:44px;color: white;"></span>
        <h1 style="margin-top: -40px; margin-left: 60px;color: white;">Address</h1>
        <p style="padding-left: 40px; font-weight: bold; padding-bottom: 50px;color: white;">7,1st Floor,<br> Sri Sairam
          Tower, NSR
          Rd,<br> Nesavaalar Colony, Saibaba Koil,<br> Coimbatore, Tamil Nadu 641011</p>
      </div>
      <div class="col-md-3"></div>

    </div>

  </div>
  <!-- footer end -->

</body>

</html>""")

m=cgi.FieldStorage()
username=m.getvalue("usr")
password=m.getvalue("psw")
submit=m.getvalue("sub")
if submit !=None:
  q="""select id from adminlogin where username="%s" and password="%s" """ %(username,password)
  cur.execute(q)
  con.commit()
  print("""
  <script>
  alert("Logged In");
  location.href="admindashboard.py";
  </script>
  """)