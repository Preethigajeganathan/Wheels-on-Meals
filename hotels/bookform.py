#!C:/Users/pirat/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, os
import cgi
import cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="hotel")
cur = con.cursor()
m = cgi.FieldStorage()

b = m.getvalue("usid")
s = """select * from userreg where id='%s' """ % (b)
cur.execute(s)
res = cur.fetchall()
name=""
usermail=""
for i in res:
    name = i[1]
    usermail=i[5]
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
                color: rgb(71, 9, 14);
                text-decoration: none;
                display: block;
                transition: background-color 0.3s, color 0.3s;
                font-size: 20px;
                font-family: bold;
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
            }
            .card {
        box-shadow: 4px 4px 8px black;
        padding: 20px;
        height: 450px;
        width: 400px;

      }

      img {
        width: 350px;
        height: 200px;
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
                    </li>
                    <li>
                        <a href="restaurant.py?id=%s"><i class="bi bi-bank2"></i> RESTAURANTS</a>
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
            </div>""" % (b,b,b,b,b))
    print("""
            <div class="content">
                """)
foodid = m.getvalue("foid")

p = """select * from food where id='%s' """ % (foodid)
cur.execute(p)
pri = cur.fetchall()
for j in pri:
    print("""
    <div class="container-fluid" style="margin-top:50px; margin-bottom:50px;">
        <div class="row">
            <div class="col-sm-3">
                <div class="card">
                    <center>
                        <form method="post" enctype="Multipart/form-data">
                            <marquee behavior="slide" scrollamount="30px"><img src="./regdoc/%s" alt=""></marquee>
                            <input type="text" style="text-align:center;font-size:20px;color:darkblue;font-family:bold;border:none" value='%s' readonly name="fname">
                        </center>
                        <lable style="font-size:20px;color:green;font-family:bold;border:none">Price:</label>
                        <input type="text" style="font-size:20px;color:green;font-family:bold;border:none" value="%s" readonly name="price">
                        <input type="hidden" name="fid" value='%s'>
                        <div class="form-group">
                        <select class="form-control" name="booktype" style="margin-top:5px;">
                                        <option>Booking Type</option>
                                        <option value="Table Booking">Table Booking</option>
                                         <option value="Order">Order</option>
                        </select>
                        </div>
                        <div class="form-group">
                        <select class="form-control" name="quant" style="margin-top:5px;">
                                        <option>Quantity</option>
                                        <option value="1">1</option>
                                         <option value="2">2</option>
                                          <option value="3">3</option>
                                           <option value="4">4</option>
                                            <option value="5">5</option>
                        </select>
                        </div>
                         <input type="hidden" name="uname" value='%s'>
                          <input type="hidden" name="hname" value='%s'>
                          <input type="hidden" name="omail" value='%s'>
                           <input type="hidden" name="umail" value='%s'>
                           <input type="hidden" name="oname" value='%s'>
                      
                        <input type="submit" name="book" value="Book" class="btn btn-success" style="margin-left:150px;margin-top:opx;">
                     
                    </form>
                </div>
            </div>
        </div>
    </div>

    """ % (j[3], j[1], j[4], j[0],name,j[2],j[8],usermail,j[6]))
username=m.getvalue("uname")
foodname=m.getvalue("fname")
hotelname=m.getvalue("hname")
omailid=m.getvalue("omail")
umailid=m.getvalue("umail")
price=m.getvalue("price")
booking=m.getvalue("booktype")
quantity=m.getvalue("quant")
status="New"
owner=m.getvalue("oname")
submit=m.getvalue("book")
if submit !=None:
    ki="""insert into booking (Username,foodname,hotelname,foodprice,booktype,quantity,status,usermail,ownermail,Ownername) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(username,foodname,hotelname,price,booking,quantity,status,usermail,omailid,owner)
    cur.execute(ki)
    con.commit()
    print("""
    <script>
    alert("Booking Confirmed");
    </script>""")


print("</div></div></body></html>")

