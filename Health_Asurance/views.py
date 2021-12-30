from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("Main/index.html")

@views.route('/profile')
def profile():
    return render_template("customer/profile.html")

@views.route('admin/profile')
def profile():
    return render_template("admin/profile.html")
