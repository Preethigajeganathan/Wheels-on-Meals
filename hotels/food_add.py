#!C:/Users/pirat/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="hotel")
cur = con.cursor()
m = cgi.FieldStorage()
b = m.getvalue("id")
s = """select * from ownerreg where id='%s' """ % (b)
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
        <title>Food Add</title>
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
                        <a href="ownerprofile.py?id=%s"><i class="bi bi-person-square"></i> PROFILE</a>
                    </li>""" % (b))
    print("""
                    <li>
                        <a href="#"><i class="bi bi-cake-fill"></i> FOODS</a>
                        <div class="dropdown-content">
                            <a href="food_add.py?id=%s">ADD</a>
                            <a href="food_view.py?id=%s">VIEW</a>

                        </div>
                    </li>""" %(b,b))
    print("""
                    <li>
                        <a href="#"><i class="bi bi-bell-fill"></i> ORDERS</a>
                        <div class="dropdown-content">
                            <a href="own_allorders.py?id=%s">ALL</a>
                            <a href="own_acceptorders.py?id=%s">ACCEPTED</a>
                            <a href="own_usercancel.py?id=%s">USER CANCELED</a>
                        </div>
                    </li>""" %(b,b,b))
    print("""
                    <li>
                        <a href="customer.py"><i class="bi bi-person-fill"> </i>TABLE RESERVATION</a>
                         <div class="dropdown-content">
                            <a href="own_tableconfirm.py?id=%s">CONFIRMED</a>
                            <a href="own_tableexist.py?id=%s">EXISTING</a>
                        </div>
                    </li>
                    <li><a href="own_feedbackview.py?id=%s"><i class="bi bi-pencil-square"> </i> FEEDBACKS</a></li>
                    <li> <a href="homepage.py">LOG OUT</a></li>
                </ul>
            </div>"""%(b,b,b))

    print("""
                <div class="content">
                
                  """)
print("""
<h1 style="text-align:center;font-family:bold;color:brown">FOOD</h1> 
    <div class="container-fluid">
    <form method="post" enctype="Multipart/form-data">
    <div class="row">
  <div class="col-sm-3"></div>
    <div class="col-sm-6">
    <div class="form-group">
    <label for="" style="text-align:left">Hotel Name</label>
  
    <input type="text" class="form-control" name="honame" value='%s'>
    </div>
    
    <div class="form-group">
    <label for="">Food Name</label>
    <input type="text" class="form-control" name="foname">
    </div>
    <div class="form-group">
    <label for="">Food Image</label>
    <input type="file" class="form-control-file" name="foodimg">
    </div>
    <div class="form-group">
    <label for="">Price</label>
    <input type="text" class="form-control" name="price">
    </div>
    <input type="hidden" class="form-control" name="street" value='%s'>
    <input type="hidden" class="form-control" name="owner" value='%s'>
   <input type="hidden" class="form-control" name="city" value='%s'>
    <input type="hidden" class="form-control" name="mail" value='%s'>
    <br>
    <br>
       <div class="form-group">
        <center>
            <input type="submit" class="btn btn-success" name="sub" style="padding:6px 22px;border:none;border-radius:5px;color:white;" value="Submit" >
           
               </center>
    </div>
    </div>
    </form>
    </div>
""" %(i[4],i[8],i[1],i[9],i[6]))
if len(m) !=0:
    submit=m.getvalue("sub")
    if submit !=None:
        name=m.getvalue("foname")
        hotel=m.getvalue("honame")
        picture=m['foodimg']
        price=m.getvalue("price")
        street=m.getvalue("street")
        owner=m.getvalue("owner")
        city=m.getvalue("city")
        mailid=m.getvalue("mail")
        if picture.filename:
            fn = os.path.basename(picture.filename)
            open("regdoc/" + fn, "wb").write(picture.file.read())
            q = """insert into food (Name,Hotelname,Photo,Price,Street,Ownername,City,owneremail) values('%s','%s','%s','%s','%s','%s','%s','%s') """ % (name,hotel,fn,price,street,owner,city,mailid)
            cur.execute(q)
            con.commit()
            print("""
                   <script>
                   alert("Food Added Successfully");
                   </script>""")
