<h1 align="center"> HEALTH </h1>

![Project](https://user-images.githubusercontent.com/68168970/152428811-f9e44478-b1a2-4fae-b89c-27fcf4178317.png)


# Introduction

This is a Health Asurance  project bulit with flask framework .

- [Installation Guide](#installation-guide) - How to get started with a new Flask app

# <a name='installation-guide'>Installation Guide</a>

This project requires the following tools:

- Python - The programming language used by Flask.
- MySql - A relational database system.
- Virtualenv - A tool for creating isolated Python environments.

To get started, install Python and MySql on your local computer if you don't have them already. 

## Getting Started


**Step 1. Clone the code into a fresh folder**

```
$ git clone https://github.com/mhasabalah/Flask-Project.git
$ cd Flask-Project
```

**Step 2. Create a Virtual Environment and install Dependencies.**

Create a new Virtual Environment for the project and activate it. If you don't have the `virtualenv` command yet, you can find installation [instructions here](https://virtualenv.readthedocs.io/en/latest/). Learn more about [Virtual Environments](http://flask.pocoo.org/docs/1.0/installation/#virtual-environments).

```
$ virtualenv venv
$ source venv/bin/activate
```

Next, we need to install the project dependencies, which are listed in `requirements.txt`.

```
(venv) $ pip install -r requirements.txt
```

**Step 3: Create an app **

Name it what you like but you'll need to specify a callback URL, which should be something like:

```
http://localhost:5000/
```

The default port for Flask apps is `5000`, but you may need to update this if your setup uses a different port or if you're hosting your app somewhere besides your local machine.

**Step 4: Setup your database**

You need to be able to connect to a database either on your own computer (locally)) to provide the database for your app.

> run sql code in MySql workbench __Schema with data.sql__  in folder SQL 

**Step 5: Update environment variables and run the Server.**

Add your sql config in __sqlConfig.py__ to Health_Asurance folder
```py
HOST = 'YOUR_HOST'
DATABASE = 'YOUR_DATABASE'
USER = 'YOUR_USER'
PASSWORD = 'YOUR_PASSWORD'
```


You replace the GitHub credentials here and update the database URL. Learn more about the required [Environment Variables here](https://github.com/MLH/mlh-hackathon-flask-starter/blob/master/docs/USER_GUIDE.md#environment-variables).

Now we're ready to start our server which is as simple as:

```
(venv) $ flask run
```

Open http://localhost:5000 to view it in your browser.

The app will automatically reload if you make changes to the code.
You will see the build errors and warnings in the console.

# What's Included?

- [Flask](http://flask.pocoo.org/) - A microframework for Python web applications
- [Flask Blueprints](http://flask.pocoo.org/docs/1.0/blueprints/) - A Flask extension for making modular applications
- [Flask-mySql](http://flask-sqlalchemy.pocoo.org/2.3/) - A Flask extension that adds ORM support for your data models.
- [Werkzeug](http://werkzeug.pocoo.org/) - A Flask framework that implements WSGI for handling requests.
- [Bootstrap 5](https://getbootstrap.com/) - An open source design system for HTML, CSS, and JS.
- [Jinja2](http://jinja.pocoo.org/docs/2.10/) - A templating language for Python, used by Flask.
