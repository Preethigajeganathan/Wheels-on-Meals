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
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <title>Home Page</title>
  <style>
    #nav1:hover {
      background-color: burlywood;
    }
  </style>
</head>

<body class="bg-light">
  <!-- logo -->
  <div class="container-fluid" style="background-color:rgb(235, 216, 216);">
    <center>
      <img src="./media/logo.PNG" alt="logo" height="150px" width="200px">
    </center>
  </div>
  <!-- logo end -->
  <!-- navbar -->
  <nav class="navbar" style="background-color: rgb(71, 9, 14);">
    <div class="container-fluid">
      <div class="navbar-header">
        <a class="navbar-brand" href="#"></a>
      </div>
      <ul class="nav navbar-nav navbar-right">
        <li class="dropdown"><a href="#" style="color:white; font-size: large;" class="dropdown-toggle" id="nav1"
            data-toggle="dropdown"><span class="glyphicon glyphicon-user" style="color:white;"></span> Sign Up<span
              class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="userreg.py" style="font-weight: bolder;" id="nav1">User</a></li>
            <li><a href="ownerreg.py" style="font-weight: bolder;" id="nav1">Hotel Owner</a></li>
          </ul>
        </li>
        <li class="dropdown"><a href="#" style="color:white;font-size: large;" id="nav1" class="dropdown-toggle"
            data-toggle="dropdown"><span class="glyphicon glyphicon-log-in" style="color:white;"></span> Login<span
              class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="adminlogin.py" style="font-weight: bolder;" id="nav1">Admin</a></li>
            <li><a href="userlogin.py" style="font-weight: bolder;" id="nav1">User</a></li>
            <li><a href="ownerlogin.py" style="font-weight: bolder;" id="nav1">Hotel Owner</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </nav>
  <!-- navbar end -->
  <!-- carousel -->

  <div class="container-fluid">
    <div id="myCarousel" class="carousel slide" data-ride="carousel">
      <!-- Indicators -->
      <ol class="carousel-indicators">
        <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
        <li data-target="#myCarousel" data-slide-to="1"></li>
        <li data-target="#myCarousel" data-slide-to="2"></li>
      </ol>

      <!-- Wrapper for slides -->
      <div class="carousel-inner">
        <div class="item active">
          <img src="media/food2.jpg" alt="Los Angeles" style="width:1500px; height: 400px;">
        </div>

        <div class="item">
          <img src="media/food7.png" alt="Chicago" style="width:1500px; height: 400px;">
        </div>

        <div class="item">
          <img src="media/food5.png" alt="New york" style="width:1500px; height: 400px;">
        </div>
      </div>

      <!-- Left and right controls -->
      <a class="left carousel-control" href="#myCarousel" data-slide="prev">
        <span class="glyphicon glyphicon-chevron-left"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="right carousel-control" href="#myCarousel" data-slide="next">
        <span class="glyphicon glyphicon-chevron-right"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
  </div>
  <!-- carousel end -->
  <!-- card image -->
  <style>
    .card {
      box-shadow: 4px 4px 8px black;
      padding: 20px;
      width: 350px;

    }

    button {
      margin: 10px;
    }
  </style>
  <div class="container" style="margin-top: 100px; margin-bottom: 100px;">
    <div class="row">

      <div class="col-sm-3">
        <div class="card">
          <center>
            <img src="media/food4.jpg" alt="" style="width: 300px;height: 300px;">
          </center>
          <center>
            <a href="#"><button class="btn btn-success btn-lg">Order</button></a>
          </center>
        </div>
      </div>
      <div class="col-md-1"></div>
      <div class="col-sm-3">
        <div class="card">
          <center>
            <img src="media/food8.png" alt="" style="width: 300px;height: 300px;">
          </center>
          <center>
            <a href="#"><button class="btn btn-success btn-lg">Order</button></a>
          </center>
        </div>
      </div>
      <div>
        <div class="col-md-1"></div>
        <div class="col-sm-3">
          <div class="card">
            <center>
              <img src="media/food3.jpg" alt="" style="width: 300px;height: 300px;">
            </center>
            <center>
              <a href="#"><button class="btn btn-success btn-lg">Order</button></a>
            </center>
          </div>
        </div>
        <div class="col-md-1"></div>
      </div>

    </div>
  </div>
  <!-- card image end -->
  <!-- footer  -->
  <div class="container-fluid" style="background-color: rgb(71, 9, 14);padding-top: 40px;">
    <div class="row">
      <div class="col-sm-3"></div>
      <div class="col-md-6">
        <span class="glyphicon glyphicon-map-marker" style="font-size:44px;color:white"></span>
        <h1 style="margin-top: -40px; margin-left: 60px; color:white">Address</h1>
        <p style="padding-left: 40px; font-weight: bold; padding-bottom: 50px;color:white">7,1st Floor,<br> Sri Sairam
          Tower, NSR
          Rd,<br> Nesavaalar Colony, Saibaba Koil,<br> Coimbatore, Tamil Nadu 641011</p>
      </div>
      <div class="col-md-3"></div>

    </div>

  </div>
  <!-- footer end -->

</body>

</html>
""")