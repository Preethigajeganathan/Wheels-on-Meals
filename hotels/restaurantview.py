#!C:/Users/pirat/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="hotel")
cur = con.cursor()
m = cgi.FieldStorage()
b = m.getvalue("uid")
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
print("""
<table  class="table table-bordered" style="overflow:auto;">
    <tr>
        <th>S.NO</th>
        <th>HotelName</th>
        <th>Owner Name</th>
        <th>Street</th>
        <th>City</th>
        <th>Hotel Image</th>
        <th>Operating Hours</th>
    </tr>
""")
sid = m.getvalue("street")
cid = m.getvalue("city")
l = """select * from ownerreg where Street='%s' and City='%s' """ % (sid, cid)
cur.execute(l)
ll = cur.fetchall()
for a in ll:
    print("""
    <form method="post"  enctype="multipart/form-data">
    <tr>
    <input type="hidden" value='%s' name="kid">
    <td>%s</td>
    <td><input type="text" value='%s' name="honame" style="border:none"></td>
    <td><input type="text" value='%s' name="name" style="border:none"></td>
    <td>%s</td>
    <td>%s</td>
    <td><img src="./regdoc/%s" width="70px" height="70px"></td>
    <td>%s</td>
    <td><input type="submit" class="btn btn-info" name="view" value="View"></td>
    </tr>
    </form>

    """ % (b, a[0], a[4], a[1], a[8], a[9], a[13], a[12]))

idd = m.getvalue("kid")
hotel = m.getvalue("honame")
owner = m.getvalue("name")
sub = m.getvalue("view")
if sub != None:
    r = """select * from ownerreg where Hotelname='%s' and Name='%s' """ % (hotel, owner)
    cur.execute(r)
    o = cur.fetchall()
    for k in o:
        hotel = k[4]
        owner = k[1]
        print("""
        <script>
        location.href="restfood.py?mid=%s&hotell=%s&ownerr=%s";
        </script>
        """ % (idd, hotel, owner))
print("</table>")
print("</div></div></body></html>")
