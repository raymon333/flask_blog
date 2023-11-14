System Information Web App
This is a simple web application built using Flask that displays system information and tests a connection to a MySQL database.
# Prerequisites
Python 3.x
Flask (pip install Flask)
psutil (pip install psutil)
pymysql (pip install pymysql)
MySQL Server
# installation
pip install
flask
# usage

Run the Flask application by executing python app.py in your terminal.
Open a web browser and go to http://localhost:5000/ to view the application.
The homepage will display system information including CPU usage and memory usage.
It will also show the status of the MySQL database connection. If the connection is successful, it will display "MySQL Database Connection Successful"

# Files
app.py: Contains the Flask application code.
index.html: HTML template to display system information.

# Important Note
Ensure your MySQL server is running and accessible with the provided configurations.
Replace the database password (rasheed3#) in the app.py file with your actual password for security.

# Contribution
Feel free to contribute to improve this application by creating pull requests.