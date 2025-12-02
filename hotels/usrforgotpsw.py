#!C:/Users/pirat/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql, cgi, cgitb, os, smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="hotel")
cur = con.cursor()
print("""
<!DOCTYPE html>
<html>
<head>
    <title>User Forgot Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
          
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .registration-container {
            background-image:url("./media/forgotbg.jpg");
            background-repeat:no repeat;
            backgroud-size:cover;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            padding: 40px;
            width: 350px;
            text-align: center;
        }

        .registration-container h2 {
            margin: 0 0 20px;
            color: #007BFF;
        }

        .form-group {
            margin: 0 0 20px;
        }

        .form-group label {
            display: block;
            font-weight: bold;
            color: #333;
        }

        .form-group input {
            width: 70%;
            padding: 10px;
            border: 2px solid #ccc;
            border-radius: 3px;
            margin-top:10px;
            font-size:20px;
        }


    </style>
</head>
<body>
    <div class="registration-container">
        <h2 style="color:white;font-family:bold">Recover Password</h2>
        <form method="post" autocomplete="off">
            <div class="form-group">
                <input type="text" id="email" name="mail" placeholder="Enter your email">
            </div>
            <div class="form-group">
                           <input type="submit"  name="sub" style="margin-top:5px;border:none;padding:10px 6px;width:100px;background-color:lightgreen;color:white;border-radius:5px" value="Submit">
            </div>
        </form>
    </div>
    <script>
  document.addEventListener('contextmenu', function (e) {
    e.preventDefault();
  });
</script>
</body>
</html>
""")
p = cgi.FieldStorage()
email = p.getvalue("mail")
submit = p.getvalue("sub")

if submit != None:
    q = """select * from userreg where Emailid='%s' """ % (email)
    cur.execute(q)
    rec = cur.fetchall()
    for i in rec:
        Email = i[5]
        Pass = i[11]
        fromadd = 'techvolt.pirathima@gmail.com'
        password = 'mnow lklm ycuy luid'
        toadd = email
        subject = "Regarding Forgot Password"
        body = "Email:{} \n\nPassword:{}".format(Email, Pass)
        msg = """subject: {} \n\n{}""".format(subject, body)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(fromadd, password)
        server.sendmail(fromadd, toadd, msg)
        server.quit()
        print("""
                                            <script>
                                            alert('mail send successfully');
                                            location.href="homepage.py"
                                            </script>
                                            """)
        con.close()



