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
    <title>User Registeration Form</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<style>
    .card {
        box-shadow: 4px 4px 8px black;
        padding: 20px;
        margin-top: 20px;

    }

    body {
        background-image: url(./media/back3.jpg);
        background-repeat: no-repeat;
        background-size: cover;
    }

    label {
        font-family: bold;
        color: white;
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

    <div class="container " style="margin-bottom: 100px;">
        <div class="row">
            <div class="col-md-3"></div>
            <div class="col-md-6">
                <form method="post" enctype="Multipart/form-data">
                    <div class="card">
                        <h2 style="text-align: center;font-family: bold;color:white">User Registration Form
                        </h2>
                        <div class="form-group">
                            <label for="">Name:</label>
                            <input type="text" class="form-control" name="name" id="name">
                        </div>
                        <div class="form-group">
                            <label for="gender">Gender</label>
                            <br>
                            <input type="radio" class="form-control-radio" name="gender" value="Male">
                            <label for="male">Male</label>
                            <input type="radio" class="form-control-radio" name="gender" value="Female">
                            <label for="female">Female</label>
                        </div>
                        <div class="form-group">
                            <label for="">DOB:</label>
                            <input type="date" class="form-control" name="DOB" id="DOB">
                        </div>
                        <div class="form-group">
                            <label for="">Profile Image:</label>
                            <input type="file" class="form-control-file" name="photo" id="profile">
                        </div>
                        <div class="form-group">
                            <label for="">Email id:</label>
                            <input type="email" class="form-control" name="email" id="email">
                        </div>
                        <div class="form-group">
                            <label for="">Phone No:</label>
                            <input type="text" class="form-control" name="phone" id="phone">
                        </div>
                        <div class="form-group">
                            <label for="address">Address</label>
                            <br>
                            <div class="row">
                                <div class="col-md-6">
                                    <input type="text" class="form-control" placeholder="Enter Street" name="street"
                                        autofocus required>
                                </div>
                                <div class="col-md-6">
                                    <input type="text" class="form-control" placeholder="Enter City" name="city"
                                        autofocus required>
                                </div>
                            </div>
                            <br>
                            <div class="row">
                             <div class="col-md-6">
                                    <select class="form-control" name="state" style="margin-top:5px;">
                                        <option>Select State</option>
                                        <option>Tamil Nadu</option>
                                    </select>
                                </div>
                                <div class="col-md-6">
                                    <select class="form-control" name="country" style="margin-top:5px;">
                                        <option>Select Country</option>
                                        <option>India</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="">Password:</label>
                            <input type="text" class="form-control" name="psw" id="phone">
                        </div>
                        <div class="form-group">
                        <center>
                             <input type="submit" class="btn btn-success" name="reg" style="padding:6px 22px;border:none;border-radius:5px;color:white;" value="Register" >
               <button type="button" class="btn btn-danger ml-2" id="cancel-button" > <a href="homepage.py" style="color:white;">Cancel</a></button>
               </center>
                       <p style="color:white;text-align:center;">Already have an account <a href="#">login here</a></p>
                        </div>
                    </div>
                </form>
            </div>
            <div class="col-md-3"></div>

        </div>
    </div>
    <!-- footer  -->
    <div class="container-fluid" style="background-color: rgb(71, 9, 14);padding-top: 40px;">
        <div class="row">
            <div class="col-sm-3"></div>
            <div class="col-md-6">
                <span class="glyphicon glyphicon-map-marker" style="font-size:44px;color: white;"></span>
                <h1 style="margin-top: -40px; margin-left: 60px;color: white;">Address</h1>
                <p style="padding-left: 40px; font-weight: bold; padding-bottom: 50px;color: white;">7,1st Floor,<br>
                    Sri Sairam
                    Tower, NSR Rd,<br> Nesavaalar Colony, Saibaba Koil,<br> Coimbatore, Tamil Nadu 641011</p>
            </div>
            <div class="col-md-3"></div>

        </div>

    </div>
    <!-- footer end -->

</body>

</html>""")
m=cgi.FieldStorage()
if len(m)!= 0:
    submit = m.getvalue("reg")
    if submit !=None:
        name=m.getvalue("name")
        gender=m.getvalue("gender")
        dob=m.getvalue("DOB")
        profile=m['photo']
        mail=m.getvalue("email")
        phoneno=m.getvalue("phone")
        street=m.getvalue("street")
        city=m.getvalue("city")
        state=m.getvalue("state")
        country=m.getvalue("country")
        password=m.getvalue("psw")
        if profile.filename:
            fn = os.path.basename(profile.filename)
            open("regdoc/" + fn, "wb").write(profile.file.read())
            q="""insert into userreg (Name,Gender,Dob,Profile,Emailid,Phoneno,Street,City,State,Country,Password) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') """ %(name,gender,dob,fn,mail,phoneno,street,city,state,country,password)
            cur.execute(q)
            con.commit()
            print("""
            <script>
            alert("Registred Successfully");
            </script>""")

