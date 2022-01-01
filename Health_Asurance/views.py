from flask import Blueprint, render_template

views = Blueprint('views', __name__)


##### Customer #####
@views.route('/')
def home():
    return render_template("Main/index.html")

@views.route('customer/profile')
def profile():
    return render_template("customer/profile.html")

@views.route('customer/hospitals')
def hospitals():
    return render_template("customer/hospitals.html")

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

@views.route('admin/customer')
def admincCustomer():
    return render_template("admin/customer.html")

@views.route('admin/plans')
def admincPlans():
    return render_template("admin/plans.html")

@views.route('admin/hospitals')
def adminhospitals():
    return render_template("admin/hospitals.html")

