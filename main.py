from Health_Asurance import create_app
from flask_mysqldb import MySQL


app = create_app()

<<<<<<< HEAD
=======
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'

mysql = MySQL(app)

>>>>>>> e74964bf287fd32b32eee121f8904e54ed6d36cf
if __name__ == '__main__':
    app.run(debug=True) 
