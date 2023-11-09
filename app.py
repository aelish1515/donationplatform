from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime
import psycopg2
import os

# Get the Heroku PostgreSQL database URL from Config Vars
DATABASE_URL = os.environ['DATABASE_URL']

app = Flask(__name__, static_url_path='/assets', static_folder='assets', template_folder='./')

# Function to connect to the PostgreSQL database
def connect_to_db():
    return psycopg2.connect(DATABASE_URL, sslmode='require')

# Create Database Tables if they don't exist
def create_tables():
    con = connect_to_db()
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Donors (
            id SERIAL PRIMARY KEY,
            Name TEXT NOT NULL,
            Amount INTEGER NOT NULL,
            Email TEXT NOT NULL,
            timestamp TIMESTAMP
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id SERIAL PRIMARY KEY,
            Name TEXT NOT NULL,
            Email TEXT NOT NULL,
            Password TEXT NOT NULL,
            Contact INTEGER NOT NULL
        )
    ''')
    con.commit()
    con.close()

create_tables()  # Ensures tables are created

@app.route('/')
def root():
    session['logged_out'] = 1
    return render_template('index.html')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Handle user registration logic
    if request.method == 'POST':
        # Process user registration form data and insert into the 'Users' table
        pass
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Handle user login logic
    if request.method == 'POST':
        # Process user login credentials and authenticate from the 'Users' table
        pass
    return render_template('login.html')

# Route for user donation
@app.route('/donate', methods=['GET', 'POST'])
def donate():
    # Handle donation form logic
    if request.method == 'POST':
        # Process donation data and insert into the 'Donors' table
        pass
    return render_template('donate.html')

# Route for displaying list of donations
@app.route('/list1')
def list1():
    # Retrieve data from the 'Donors' table and render the list of donations
    return render_template('list1.html')

# Route for user profile
@app.route('/profile')
def profile():
    # Fetch user details from the 'Users' table and render user profile
    return render_template('profile.html')

if __name__ == '__main__':
    app.secret_key = "supersecretkey"  # Update this secret key
    app.run()
