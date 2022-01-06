from os import name

from flask import Blueprint, render_template, request, flash, session, g

from flask.helpers import url_for
from werkzeug.utils import redirect
from . import mysql
import functools
from datetime import date
from collections import Counter
views = Blueprint('views', __name__)

##### Customer #####


@views.route('/')
def home():
    return render_template("Main/index.html")

@views.route('/team')
def team():
    return render_template("/Team.html")


@views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        user = request.form
        if(user):
            try:
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO customers(Customer_Name, DateOfBirth, City, Street , Building_Number, PhoneNumber) VALUES (%s, %s, %s, %s, %s, %s)",
                            (user['name'], user['BirthDate'], user['inputCity'], user['Address'], user['inputAddress2'], user['PhoneNumber']))
                mysql.connection.commit()
                cur.execute("select Customer_Id from customers where Customer_Name=%s and PhoneNumber= %s;",
                            (user['name'], user['PhoneNumber']))
                customerID = cur.fetchone()
                
            except cur.IntegrityError:
                error = f"User {user['name']} is already registered."
                print(error)
            else:
                flash(f'You were successfully registered in and your CODE is {customerID[0]}')
                return redirect(url_for('views.login'))
        
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
        g.user = cur.fetchone()
        user = g.user

        age = date.today().year - \
            user[2].year - ((date.today().month, date.today().day)
                            < (user[2].month, user[2].day))

        cur.execute(
            'select dependants.Name from customers,dependants where customers.Customer_Id =%s and dependants.Customer_Id = customers.Customer_Id', (
                user_id,)
        )
        dependents = cur.fetchall()
        print(dependents)

        cur.execute(
            'select customers.Customer_Name,plans.Type from customers,`purchasd plans`,plans where customers.Customer_Id =%s and `purchasd plans`.Customer_Id = customers.Customer_Id and plans.Plan_Id=`purchasd plans`.Plan_Id;', (
                user_id,)
        )
        plan = cur.fetchall()

        plans = {}
        for item in plan:
            if (item in plans):
                plans[item] += 1
            else :
                plans[item] = 1
    return render_template("customer/profile.html", users=user, age=age, dependents=dependents, plans=plans)


@views.route('customer/hospitals', methods=['GET'])
def hospitals():
    cursor = mysql.connection.cursor()
    sql = "select hospitals.Name,hospitals.City,hospitals.phone, plans.Type from enrolled , hospitals ,plans where plans.plan_Id = enrolled.plan_Id and enrolled.Hospital_id =hospitals.Hospital_id"
    cursor.execute(sql)
    hospitals = cursor.fetchall()
    print(hospitals)
    return render_template("customer/hospitals.html", hospitals=hospitals)

@views.route('customer/plans', methods=['GET', 'POST'])
def plans():
    user_id = session.get('user_id')
    if request.method == 'POST':
        if request.form['submit_button'] == 'basic':
            cur = mysql.connection.cursor()
            cur.execute(
                'insert into `purchasd plans` (Customer_Id, Plan_Id) values (%s, %s);', (
                    user_id, 1)
            )
            mysql.connection.commit()
            flash(f'You have successfully bought A basic plan')

        elif request.form['submit_button'] == 'premuim':
            cur = mysql.connection.cursor()
            cur.execute(
                'insert into `purchasd plans` (Customer_Id, Plan_Id) values (%s, %s);', (
                    user_id, 2)
            )
            mysql.connection.commit()
            flash(f'You have successfully bought A premuim plan')

        elif request.form['submit_button'] == 'gold':
            cur = mysql.connection.cursor()
            cur.execute(
                'insert into `purchasd plans` (Customer_Id, Plan_Id) values (%s, %s);', (
                    user_id, 3)
            )
            mysql.connection.commit()
            flash(f'You have successfully bought A Golden plan')

    return render_template("customer/PurchasedPlans.html")

@views.route('/customer/benefitPlan', methods=['GET', 'POST'])
def benefit():
    user_id = session.get('user_id')
    cur = mysql.connection.cursor()
    cur.execute(
        'select `purchasd plans`.PurchasedPlanID, plans.Type from `purchasd plans`,plans,customers where `purchasd plans`.plan_Id = plans.plan_Id and customers.Customer_Id = `purchasd plans`.Customer_Id and customers.Customer_Id=%s'
         , (user_id,)
    )
    plans = cur.fetchall()
    if request.method == "POST":
        plan = request.form
        print(plan['option'])

        cur.execute(
            'update customers set customers.Beneficiary_Plan =%s where customers.Customer_Id=%s;',
            (plan['option'],user_id)
        )
        mysql.connection.commit()
        flash(f"successfully choosed {plan['option']} as your Beneficiary plan")

    return render_template("customer/selectPlan.html", plans = plans)


@views.route('customer/dependants', methods=['GET', 'POST'])
def dependants():
    user_id = session.get('user_id')
    cur = mysql.connection.cursor()
    cur.execute(
        'select `purchasd plans`.PurchasedPlanID, plans.Type from `purchasd plans`,plans,customers where `purchasd plans`.plan_Id = plans.plan_Id and customers.Customer_Id = `purchasd plans`.Customer_Id and customers.Customer_Id=%s', (
            user_id,)
    )
    plans = cur.fetchall()

    if request.method == "POST":
        try:
            dependant = request.form
            cur = mysql.connection.cursor()
            cur.execute(
                'INSERT INTO dependants(Name, DateOfBirth, RelationShip, Beneficiary_plan, Customer_Id) Values(%s , %s, %s, %s ,%s)', (
                    dependant['Name'], dependant['BirthDate'], dependant['relationShip'], dependant['option'], user_id,)
            )
            mysql.connection.commit()
            flash(f"successfully dependant added {dependant['Name']}")

        except cur.IntegrityError:
            error = "Database error"
            print(error)

    return render_template("customer/dependants.html", plans=plans)

@views.route('customer/Allclaims' , methods =['GET' , 'POST'])
def claimsCustomer():
     return render_template("customer/ALLclaims.html")

@views.route('customer/DepName' , methods =['GET' , 'POST'])
def claimsDepName():
    user_id = session.get('user_id')
    cur = mysql.connection.cursor()
    cur.execute(
        'select dependants.Name, dependants.Dep_ID from customers,dependants where customers.Customer_Id =%s and dependants.Customer_Id = customers.Customer_Id', (
            user_id,)
        )
    dependants = cur.fetchall()
    print(dependants)
    if request.method == 'POST':
        dependantID = request.form['dependent']
        print(dependantID)
        return redirect(url_for('views.Depclaims', id = dependantID))
    return render_template("customer/claimDepName.html",dependants = dependants)

@views.route('customer/depclaims/<string:id>' , methods =['GET' , 'POST'],)
def Depclaims(id):
    user_id = session.get('user_id')
    cur = mysql.connection.cursor()
    cur.execute(
        'select dependants.Name from dependants where dependants.Dep_ID =%s', (
            id,)
        )
    dependant = cur.fetchall()
    print(dependant)
    
    cur.execute(
        f'select test.Hospital_id, hospitals.Name from( SELECT dependants.Beneficiary_Plan, `purchasd plans`.Plan_Id, enrolled.Hospital_id from dependants,`purchasd plans`, enrolled where Beneficiary_Plan = `purchasd plans`.PurchasedPlanID and `purchasd plans`.Plan_Id = enrolled.Plan_Id and dependants.Dep_ID = {id}) as test, hospitals where test.Hospital_id = hospitals.Hospital_id;'
    )
    hospitals = cur.fetchall()
    print(hospitals)

    if request.method == 'POST':
        claim = request.form
        cur.execute(
            f"INSERT INTO health_insurance.claims (Customer_id,Dependant_ID , Cost ,description , Hospital_id, Status) VALUES ('{user_id}' ,'{id}', '{claim['ExpectedCost']}', '{claim['Description']}' ,'{claim['hospital']}','{0}');"
        )
        mysql.connection.commit()

    return render_template("customer/Depclaims.html", dependant = dependant, hospitals= hospitals)


@views.route('customer/claims', methods=['GET', 'POST'])
def claims():
    user_id = session.get('user_id')
    cur = mysql.connection.cursor()
    cur.execute(
        f'select test.Hospital_id, hospitals.Name from(SELECT customers.Beneficiary_Plan, `purchasd plans`.Plan_Id, enrolled.Hospital_id from customers,`purchasd plans`, enrolled where Beneficiary_Plan = `purchasd plans`.PurchasedPlanID and `purchasd plans`.Plan_Id = enrolled.Plan_Id and customers.Customer_Id = {user_id}) as test, hospitals where test.Hospital_id = hospitals.Hospital_id;'
    )
    hospitals = cur.fetchall()
    if request.method == 'POST':
        claim = request.form
        print(claim)
        cur = mysql.connection.cursor()
        cur.execute(
            f"INSERT INTO health_insurance.claims (Customer_id, Cost ,description , Hospital_id, Status) VALUES ('{user_id}' ,'{claim['ExpectedCost']}', '{claim['Description']}' ,'{claim['hospital']}','{0}');"
        )
        mysql.connection.commit()

    return render_template("customer/claims.html" , hospitals = hospitals)

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
    return render_template("admin/customer.html", customers=customers)


@views.route('admin/plans', methods=['GET', 'POST'])
def AdminPlans():
    if request.method == 'POST':
        planType = request.form["type"]
        price = request.form["price"]

        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO health_insurance.plans (Type, Price) VALUES ('{planType}','{price}');"
        cursor.execute(sql)
        mysql.connection.commit()
        cursor.close()

        flash(f'{planType} is added successfully.')

    return render_template("admin/plans.html")


@views.route('admin/hospitals', methods=['GET', 'POST'])
def AdminHospitals():
    cursor = mysql.connection.cursor()
    sql = "select * from health_insurance.plans"
    cursor.execute(sql)
    plans = cursor.fetchall()
     
    if request.method == 'POST':
        name = request.form["name"]
        city = request.form["city"]
        street = request.form["street"]
        phone = request.form["phone"]
        plan = request.form.getlist("plantype")
 

        print(plan)
        cursor = mysql.connection.cursor()
        
        sql = f"INSERT INTO health_insurance.hospitals (Name, City, Street, Phone ) VALUES ('{name}','{city}','{street}','{phone}');"
         
        cursor.execute(sql)
        mysql.connection.commit()

        cursor.execute("select Hospital_id from hospitals where Name=%s and Phone= %s;",(name,phone))
        hospitalID = cursor.fetchone()
        
        for i in range(len(plan)):
            cursor.execute(f"INSERT INTO enrolled (Hospital_id, Plan_Id) VALUES ('{hospitalID[0]}','{plan[i]}');")
        mysql.connection.commit()
        cursor.close()
        flash(f'{name} is added successfully.')
     
    return render_template("admin/hospitals.html" , plans = plans)


@views.route('edit_status/<string:id>', methods=['POST'])
def update_status(id):
    PostStatus(id, '_method')
    return redirect(url_for('views.adminClaims'))

@views.route('edit_status_dependent/<string:id>', methods=['POST'])
def update_status_depndent(id):
    PostStatus(id, '_methoddp')
    return redirect(url_for('views.adminClaimsDependent'))

def PostStatus(id, nameOfSubmit):
    cursor = mysql.connection.cursor()

    if request.form[nameOfSubmit] == 'resolved':
        sql = f"UPDATE claims SET Status = '1' where claims_Id = '{id}';"
    if request.form[nameOfSubmit] == 'unresolved':
        sql = f"UPDATE claims SET Status = '0' where claims_Id = '{id}';"

    cursor.execute(sql)
    mysql.connection.commit()
    cursor.close()

@views.route('admin/claim_details/<string:id>')
def claim_details(id):
    cursor = mysql.connection.cursor()
    sql = f"select claims.claims_Id, customers.Customer_Name , claims.Cost, claims.Description, hospitals.Name as RequiredHospital ,claims.Status from customers,claims,hospitals where claims.Customer_Id = customers.Customer_Id and claims.hospital_Id = Hospitals.Hospital_Id and claims_Id = '{id}'"
    cursor.execute(sql)
    claims = cursor.fetchone()
    return render_template("admin/ClaimsDetails.html", Claims=claims)


@views.route('admin/claim_details_dep/<string:id>')
def claim_details_dependent(id):
    cursor = mysql.connection.cursor()
    sql = f'''select claims.claims_Id, dependants.Name as dependent_Name
            ,dependants.RelationShip, dependants.Customer_Id, claims.Cost, 
            claims.Description, hospitals.Name as Required_Hospital 
            ,claims.Status from dependants,claims,hospitals 
            where claims.Dependant_ID = dependants.Dep_ID and 
            claims.hospital_Id = Hospitals.Hospital_Id and claims.claims_Id={id}'''
    cursor.execute(sql)
    claims = cursor.fetchone()
    print(claims)
    return render_template("admin/ClaimsDetailsDep.html", Claims=claims)


@views.route('admin/claims', methods=['GET', 'POST'])
def adminClaims():
    claims = AdminClaimsSql()
    return render_template("admin/claims.html", claims=claims)


@views.route('admin/claims-dependent', methods=['GET', 'POST'])
def adminClaimsDependent():
    claims = AdminClaimsDependentSql()
    return render_template("admin/ClaimsDependent.html", claims=claims)


def AdminClaimsDependentSql():
    sql = f'''select claims_Id, dependants.Dep_ID,dependants.Name as dependent_Name, claims.Cost,claims.Description,
            claims.Hospital_id,hospitals.Name as Hospital_Name,claims.Status 
            from dependants,claims,hospitals 
            where claims.Dependant_ID = dependants.Dep_ID and hospitals.Hospital_id=claims.Hospital_id '''

    if request.method == 'POST':
        if request.form['submit_button'] == 'resolved':
            sql = sql + " and claims.Status = 1"
        elif request.form['submit_button'] == 'unresolved':
            sql = sql + " and claims.Status = 0"
        else:
            pass

    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    claims = cursor.fetchall()
    return claims


def AdminClaimsSql():
    sql = f'''select claims_Id, customers.Customer_Name ,
            claims.Cost,claims.Description,claims.Hospital_id,
            claims.Status from customers,
            claims where claims.Customer_Id = customers.Customer_Id 
            and claims.Dependant_ID is null'''

    if request.method == 'POST':
        if request.form['submit_button'] == 'resolved':
            sql = sql + " and claims.Status = 1"
        elif request.form['submit_button'] == 'unresolved':
            sql = sql + " and claims.Status = 0"
        else:
            pass

    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    claims = cursor.fetchall()
    return claims
