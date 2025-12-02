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
name=""
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
            </div>""" % (b,b,b,b))
    print("""
            <div class="content">
               
        <script>
            document.addEventListener('contextmenu', function (e) {
                e.preventDefault();
            });
        </script>
    </body>

    </html>""")

print("""
<h1 style="text-align:center;font-family:bold;color:brown">FOOD</h1> 
    <div class="container-fluid">
    <form method="post" enctype="Multipart/form-data">
    <div class="row">
    <div class="col-sm-3"></div>
    <div class="col-sm-6">
    <div class="form-group">
    <input type="hidden" class="form-control" name="user" value='%s'>
    </div>
    
    <div class="form-group">
    <input type="text" class="form-control" name="honame" placeholder="Hotel Name">
    </div>
    <div class="form-group">
    <select class="form-control" name="rating" style="margin-top:5px;">
                                        <option>Rating</option>
                                        <option value="1">1</option>
                                         <option value="2">2</option>
                                          <option value="3">3</option>
                                           <option value="4">4</option>
                                            <option value="5">5</option>
    </select>
    </div>
    <div class="form-group">
    <textarea rows="5" cols="5" class="form-control" Placeholder="Description" name="description"></textarea>
    </div>
   
    <br>
    <br>
       <div class="form-group">
        <center>
            <input type="submit" class="btn btn-success" name="sub" style="padding:6px 22px;border:none;border-radius:5px;color:white;" value="Submit">
           
               </center>
    </div>
    </div>
    </form>
    </div>""" %(name))
uname=m.getvalue("user")
hotel=m.getvalue("honame")
rate=m.getvalue("rating")
desc=m.getvalue("description")
submit=m.getvalue("sub")
if submit !=None:
    sp="""insert into feedback (Username,Hotelname,rating,description) value('%s','%s','%s','%s')""" %(uname,hotel,rate,desc)
    cur.execute(sp)
    con.commit()
    print("""
    <script>
    alert("Feedback Submitted");
    </script>
    """)
