from os import name
from flask import Blueprint, render_template, request , flash,session, g
from flask.helpers import url_for
from werkzeug.utils import redirect
from . import mysql
import functools
from datetime import date

views = Blueprint('views', __name__)


##### Customer #####
@views.route('/')
def home():
    return render_template("Main/index.html")

@views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user = request.form
        if(user):
            try:
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO customers(Customer_Name, DateOfBirth, City, Street , Building_Number, PhoneNumber) VALUES (%s, %s, %s, %s, %s, %s)", 
                (user['name'], user['BirthDate'], user['inputCity'], user['Address'], user['inputAddress2'],user['PhoneNumber']))
                mysql.connection.commit()

            except cur.IntegrityError:
                error = f"User {user['name']} is already registered."
                print(error)
            else:
                return render_template('login.html')
        flash(error)
    
    return render_template("register.html")

@views.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        userId = request.form['userId']
        print(userId)
        error = None
        cur = mysql.connection.cursor()
        cur.execute(
            'SELECT * FROM customers WHERE customer_Id = %s', (userId,)
        )
        
        user = cur.fetchone()
        print(user)
        if user is None:
            error = 'Incorrect userId.'

        if error is None:
            session.clear()
            session['user_id'] = user[0]
            return redirect(url_for('views.profile'))

        flash(error)

    return render_template("login.html")

@views.route('customer/profile')
def profile():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        cur = mysql.connection.cursor()
        cur.execute(
            'SELECT * FROM customers WHERE customer_Id = %s', (user_id,)
        )
        g.user =cur.fetchone()
        user= g.user

        print(user)
        age=date.today().year - user[2].year - ((date.today().month, date.today().day)<(user[2].month, user[2].day))

        cur.execute(
            'select dependants.Name from customers,dependants where customers.Customer_Id =%s and dependants.Customer_Id = customers.Customer_Id'
            ,(user_id,)
        )
        dependents = cur.fetchall()
        print(dependents)   

        cur.execute(
            'select distinct customers.Customer_Name,plans.Type from customers,`purchasd plans`,plans where customers.Customer_Id =%s and `purchasd plans`.Customer_Id = customers.Customer_Id and plans.Plan_Id=`purchasd plans`.Plan_Id;'
            ,(user_id,)
        )  
        plans = cur.fetchall()         
    return render_template("customer/profile.html", users= user , age =age, dependents =dependents, plans = plans )


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

@views.route('admin/claims')
def adminClaims():
    return render_template("admin/claims.html")

