from flask import Flask, render_template, request
import sqlite3

flask6 = Flask(__name__, template_folder='template')

@flask6.route('/')
def index():
    return render_template('index.html')

@flask6.route('/add')
def add():
    return render_template('add.html')    

@flask6.route("/savedetails", methods = ["POST", "GET"])
def saveDetails():
    msg ="msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            #address = request.form["address"]
            with sqlite3.connect("employee.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Empl1(name, email) values (?,?) ", (name, email))
                con.commit()
                msg= "Employee successfully added"

        except:
            con.rollback()
            msg = "we cannot add the employee to the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()

@flask6.route("/view")
def view():
    con = sqlite3.connect("employee.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from Empl1")
    rows = cur.fetchall()
    return render_template("view.html",rows= rows)                 


@flask6.route("/delete")
def delete():
    return render_template("delete.html")

@flask6.route("/deleterecord", methods = ["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("employee.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from Empl1 where id= ?", id)
            msg = "record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html", msg = msg)            

#con = sqlite3.connect("employee.db")
#print("Database created successfully")

#con.execute("create table Empl1 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL)")
#print("table created success")

if __name__ == "__main__":
    flask6.run(debug= True)
