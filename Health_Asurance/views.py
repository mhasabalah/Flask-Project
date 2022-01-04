from flask import Blueprint, render_template, request , flash
from . import mysql


views = Blueprint('views', __name__)


##### Customer #####
@views.route('/')
def home():
    return render_template("Main/index.html")

@views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user = request.form
        print(user)

        return "done"
    else:
        return render_template("register.html")

@views.route('/login')
def login():
    if request.method == "POST":
    
        return render_template("login.html")

@views.route('customer/profile')
def profile():
    return render_template("customer/profile.html")

@views.route('customer/hospitals', methods=['GET'])
def hospitals():
    cursor = mysql.connection.cursor()
    sql = "select hospitals.Name,hospitals.City,hospitals.phone, plans.Type from enrolled , hospitals ,plans where plans.plan_Id = enrolled.plan_Id and enrolled.Hospital_id =hospitals.Hospital_id"
    cursor.execute(sql)
    hospitals = cursor.fetchall()
    print (hospitals)
    return render_template("customer/hospitals.html", hospitals = hospitals)

@views.route('customer/plans')
def plans():
    return render_template("customer/PurchasedPlans.html")
    

@views.route('customer/claims')
def claims():
    return render_template("customer/claims.html")
    

@views.route('/tryy')
def tryy():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM plans''')
    resurlt = cur.fetchall()
    print (resurlt)
    return 'done'

    

##### Admin #####
@views.route('admin/profile')
def adminProfile():
    return render_template("admin/profile.html")

@views.route('admin/customer')
def admincCustomer():
    return render_template("admin/customer.html")

@views.route('admin/plans')
def admincPlans():
    return render_template("admin/plans.html")

@views.route('admin/hospitals')
def adminHospitals():
    return render_template("admin/hospitals.html")

@views.route('admin/claims')
def adminClaims():
    return render_template("admin/claims.html")

