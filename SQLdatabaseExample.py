import sqlite3 #to do anything with databases import this
from bottle import template, run, get, post, route, request

"""
The purpose of this program is to register new users into a database of ALT enthusiasts. 
The opening page of the web interface has an html page with the following fields: 
a name field, that takes a name for the user; an email address field that takes an email address; 
an interests field - that takes a comma seperated string of the research interests of the user. 
When someone reaches the interface, they are prompted them to enter these details. 
Once they click on submit, they are added to the database, and:
a) If someone with that name already exists in the database, the program gives a message 
to the user that they need to use some other name, as someone with that name already exists.
b) If a new user (with a new name) arrives, their details are added to the database and 
gives them a confirmation message.
"""


def createDatabase():
    conn = sqlite3.connect('ALTEnthusiasts.sqlite3')
    cur = conn.cursor()
    cur.execute('CREATE TABLE ALTEnthusiasts (Name STRING, Email STRING, Interests STRING)')

    conn.commit() #This line is important if you want your database to actually change!

@route("/add", method="POST")
def add_user():
    new1 = request.forms.get('Name')
    new2 = request.forms.get('Email')
    new3 = request.forms.get('Interests')
    conn = sqlite3.connect('ALTEnthusiasts.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT Name FROM ALTEnthusiasts WHERE Name=?", (new1,))
    data = cur.fetchall()
    if not data:
        cur.execute("INSERT INTO ALTEnthusiasts (Name, Email, Interests) VALUES (?,?,?)", (new1, new2, new3))
        conn.commit()
        result1 = '<p><center><b><font size="14" color="purple"><body bgcolor="#D7BDE2">Congrats! You are now a part of our super awesome database!</b></center</p>'
    else:
        result1 = '<p><center><b><font size="14" color="purple"><body bgcolor="#D7BDE2">Sorry, but someone with that name is already in the database, you might want to call yourself differently.</b></center</p>'

    return result1
    #conn.close()
    #cur.close()

@route('/')
@route('/enterinfo')
@route("/add", method="get")
def first_page():
    conn = sqlite3.connect('ALTEnthusiasts.sqlite3')
    cur = conn.cursor()
    return'''

<html>
<body bgcolor="#D7BDE2">
<head>
<title>ALT Enthusiasts</title>
</head>
<body>


<h1><center><font color="purple">Welcome to the Applied Linguistics & Technology Enthusiasts Database!</center</h1>
<p>To join other cool people, please enter your information below, and click "submit":</p>

<form action="/add" method="post">
        Name: <input type="text" name="Name"> <br>
        Email: <input type="text" name="Email"><br>
        <p><font color="purple">Tell us what your research interests are:</p>
        <p><textarea name="Interests" rows="10" cols="70"> </textarea></font></p>
        <p><br><input type="submit" value="Submit">
        </form></p>


</body>
</html>
'''


run(reloader=True)

#createDatabase()
add_user()