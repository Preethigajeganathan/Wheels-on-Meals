#!C:/Users/pirat/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="hotel")
cur = con.cursor()
m = cgi.FieldStorage()
b = m.getvalue("id")
s = """select * from userreg where id='%s' """ % (b)
cur.execute(s)
res = cur.fetchall()
for i in res:
    name = i[1]
    print("""
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Customer Dashboard</title>
         <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
        <style>
            /* Reset some default styles */
            body,
            ul {
                margin: 0;
                padding: 0;
            }

            /* Container for sidebar and content */
            .container {
                display: flex;
            }

            /* Sidebar styles */
            .sidebar {
                width: 250px;
                background-color: rgb(206, 186, 188);
                overflow-y: auto;
                height: 100vh;
                position: fixed;
                top: 0;
                left: 0;
            }

            .sidebar h2 {
                color: white;
                text-align: center;
                padding: 10px;
                margin: 0;
            }

            .sidebar ul {
                list-style: none;
                padding: 0;
            }

            .sidebar ul li {
                padding: 10px;
                text-align: left;
            }

            .sidebar ul li a {
                color:  rgb(71, 9, 14);
                text-decoration: none;
                display: block;
                transition: background-color 0.3s, color 0.3s;
                font-size: 20px;
                font-family:bold;
            }

            /* Hover effect for links */
            .sidebar ul li a:hover {
                background-color: #555;
                color: #fff;
            }

            /* Dropdown submenu */
            .dropdown-content {
                display: none;
                padding-left: 20px;
                font-size: 15px;
            }

            /* Show dropdown content on hover */
            .sidebar ul li:hover .dropdown-content {
                display: block;
            }

            /* Content styles */
            .content {
                flex-grow: 1;
                margin-left: 250px;
                /* Adjust this to match the sidebar width */
                padding: 16px;
                text-align: center;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <div class="sidebar">
                <h2></h2>
                <ul>

                    <li>
                        <a href="customerprofile.py?id=%s"><i class="bi bi-person-square"></i> PROFILE</a>

                    </li>""" % (b))
    print("""
                    <li>
                        <a href="restaurant.py?id=%s""><i class="bi bi-bank2"></i> RESTRAUNTS</a>

                    </li>
                     <li>
                     <a href="#"><i class="bi bi-bell-fill"></i> ORDERS</a>
                     <div class="dropdown-content">
                            <a href="userorders.py?id=%s">MY ORDERS</a>
                            <a href="usercancel.py?id=%s">CANCELED</a>
                        </div>
                     </li>
                    <li><a href="feedbackform.py?id=%s"><i class="bi bi-pencil-square"> </i> FEEDBACKS</a></li>
                    <li> <a href="homepage.py">LOG OUT</a></li>
                </ul>
            </div>""" % (b, b,b,b))
    print("""
            <div class="content">
               
  
            """)
    print("""
        <table align="left" cellpadding="20px" cellspacing="30px" style="width:300px;height:200px;">
        <form>
        <tr><img src="./regdoc/%s" class="img-circle" width="100px" height="100px" style="margin-left:-700px;" ></tr>
        <br>
        <br>
        <tr>
        <th>Name:</th>
        <td style="text-align:left;">%s</td>
        </tr>
        <tr>
        <th>Email Id:</th>
        <td style="text-align:left;">%s</td>
        </tr>
        <tr>
        <th>Password:</th>
        <td ><input type="password" style="text-align:left;border:none;" value='%s'></td>
        </tr>
        <tr>
        <th><button type="button" class="btn btn-info" data-toggle="modal" data-target="#myModal%s">Change Password</button>
        </th>
        </form>
        </tr>
         <div id="myModal%s" class="modal fade" role="dialog">
       <div class="modal-dialog">

        <!-- Modal content-->
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">&times;</button>
            <h4 class="modal-title">Change Password</h4>
          </div>
          <div class="modal-body">
            <form method="post" enctype="Multipart/form-data">
            <input type="hidden" id="usr" class="form-control" name="oid" value='%s' >
            <div class="from-group">
            <label for="psw" style="font-family:bold;font-size:20px;margin-left:-410px;">New Password</label>
            <input type="text" id="usr" class="form-control" name="newpsw" >
            </div>
            <div class="from-group">
            <label for="psw" style="font-family:bold;font-size:20px;margin-left:-380px;">confirm Password</label>
            <input type="text" id="usr" class="form-control" name="conpsw" >
            </div>
             <input type="hidden" id="usr" class="form-control" name="oldpsw"  value='%s'>
            <br>
            <div class="from-group">
            <input type="submit" class="btn btn-success" value="Update" name="sub">
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
          </div>
          </div>

          </div>
          </div>
        """ % (i[4], i[1], i[5], i[11], i[0], i[0], i[0], i[11]))
idd = m.getvalue("oid")
op = m.getvalue("oldpsw")
np = m.getvalue("newpsw")
cp = m.getvalue("conpsw")
submit = m.getvalue("sub")
if submit != None:
    if np != op:
        if np == cp:
            q = """update userreg set Password='%s' where id='%s' """ % (np, idd)
            cur.execute(q)
            con.commit()
            print("""
                            <script>
                            alert("Password Changed");
                            location.href="homepage.py"
                            </script>
                            """)
        else:
            print("""
                            <script>
                            alert("New password and Confirm password must be same");
                            location.href="customerprofile.py?id=%s"
                            </script>
                            """ % (idd))
    else:
        print("""
                        <script>
                        alert("Old password cannot be New password");
                         location.href="customerprofile.py?id=%s"
                        </script>
                        """ % (idd))

