from os import name
from flask import Blueprint, render_template, request , flash
from flask.helpers import url_for
from werkzeug.utils import redirect
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
    

# @views.route('customer/claims')
# def claims():
#     return render_template("customer/claims.html")
    

@views.route('customer/claims')
def claims():
    if request.method == 'POST':
        Customer_Id = request.form["CustomerId"] 
        Dependant_ID = request.form["DependantID"]
        Cost = request.form["ExpectedCost"]
        Description = request.form["Description"]
        Hospital_name = request.form["RequiredHopsital"]
        cursor = mysql.connection.cursor()
        Hospital_id = f"select hospitals.Hospital_id from hospitals where hospitals.Name ='{Hospital_name}'"
        sql=f"INSERT INTO health_insurance.claims (Customer_id,Dependant_ID, Cost ,ddescription , Hospital_id ) VALUES ('{Customer_Id}','{Dependant_ID}' ,'{Cost}', '{Description}' ,'{Hospital_id}');"
        cursor.execute(Hospital_id)
        cursor.execute(sql)
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
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

@views.route('admin/customer', methods=['GET'])
def AdminCustomer():
    cursor = mysql.connection.cursor()
    sql = "select * from health_insurance.customers;"
    cursor.execute(sql)
    customers = cursor.fetchall()
    print (customers)
    return render_template("admin/customer.html", customers = customers)

@views.route('admin/plans',methods=['GET', 'POST'])
def AdminPlans():
    if request.method == 'POST':
        planType = request.form["type"] 
        price = request.form["price"]

        cursor = mysql.connection.cursor()
        sql=f"INSERT INTO health_insurance.plans (Type, Price) VALUES ('{planType}','{price}');"
        cursor.execute(sql)
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
    return render_template("admin/plans.html")

@views.route('admin/hospitals',methods=['GET', 'POST'])
def AdminHospitals():
    if request.method == 'POST':
        name = request.form["name"]
        city = request.form["city"]
        street = request.form["street"]
        phone = request.form["phone"]
        
        cursor = mysql.connection.cursor()
        sql=f"INSERT INTO health_insurance.hospitals (Name, City, Street, Phone ) VALUES ('{name}','{city}','{street}','{phone}');"
        cursor.execute(sql)
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
    return render_template("admin/hospitals.html")

@views.route('admin/claims', methods=['GET', 'POST'])
def adminClaims():
    cursor = mysql.connection.cursor()
    sql = "select claims_Id, customers.Customer_Name , claims.Cost,claims.Description,claims.Hospital_id,claims.Status from customers,claims where claims.Customer_Id = customers.Customer_Id"
    cursor.execute(sql)
    claims = cursor.fetchall()
    # if request.method == 'POST':
        
    #     cursor = mysql.connection.cursor()
    #     sql = f"UPDATE claims SET Status = '1' where claims_Id = '{}';"

    return render_template("admin/claims.html",claims = claims)

# @views.route('edit_status/<string:id>', methods=['POST'])
# def update_status(id):
#     cursor = mysql.connection.cursor()
#     sql = f"UPDATE claims SET Status = '1' where claims_Id = '{id}';"
#     mysql.connection.commit()
#     cursor.close()
#     return redirect(url_for('adminClaims'))