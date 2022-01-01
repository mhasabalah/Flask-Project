from Health_Asurance import create_app
from flask_mysqldb import MySQL


app = create_app()

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)

if __name__ == '__main__':
    app.run(debug=True) 
