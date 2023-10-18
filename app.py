from flask import Flask, render_template, request
import psutil
import pymysql

app = Flask(__name__)

# MySQL Database Configuration
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'rasheed3#'  # Replace with your actual password
app.config['MYSQL_DATABASE_DB'] = 'shop'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

def get_system_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    return {
        'CPU Usage': f'{cpu_percent}%',
        'Memory Usage': f'{memory_info.percent}%',
    }

def test_mysql_connection():
    try:
        conn = pymysql.connect(
            host=app.config['MYSQL_DATABASE_HOST'],
            user=app.config['MYSQL_DATABASE_USER'],
            password=app.config['MYSQL_DATABASE_PASSWORD'],
            database=app.config['MYSQL_DATABASE_DB']
        )
        conn.close()
        return "MySQL Database Connection Successful"
    except Exception as e:
        return f"Failed to connect to MySQL: {str(e)}"

@app.route('/')
def index():
    system_info = get_system_info()
    mysql_connection_status = test_mysql_connection()
    return render_template('index.html', system_info=system_info, mysql_connection_status=mysql_connection_status)

if __name__ == '__main__':
    app.run(debug=True)

