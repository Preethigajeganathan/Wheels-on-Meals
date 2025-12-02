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
    <title>Admin Dashboard</title>
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
                    <a href="#"><i class="bi bi-houses-fill"> </i> HOTELS</a>
                    <div class="dropdown-content">
                        <a href="ownernew.py">New</a>
                        <a href="ownerexisting.py">Existing</a>

                    </div>
                </li>
                <li>
                    <a href="customer.py"><i class="bi bi-person-fill"> </i> CUSTOMERS</a>
                    
                </li>
                <li><a href="#"><i class="bi bi-pencil-square"> </i> FEEDBACKS</a></li>
                <li> <a href="homepage.py">LOG OUT</a></li>
            </ul>
        </div>
        <div class="content">
            <header>     
    <center>
      <img src="./media/logo.PNG" alt="logo" height="150px" width="200px">
    </center>
  </div>
            </header>
        </div>
    </div>
    <script>
        document.addEventListener('contextmenu', function (e) {
            e.preventDefault();
        });
    </script>
</body>

</html>""")