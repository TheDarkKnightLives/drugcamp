from flask import Flask, render_template, request, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy

import json 
import os 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # Initialize SQLAlchemy

# Define a User model with an email field
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roll_number = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

# Create the database and the User table
with app.app_context():
    db.create_all()

def check_credentials(username, password):
    return username == "chumma" and password == "ihatedrugs"

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == "chumma" and password == "ihatedrugs":
            # Load data from the JSON file
            if os.path.exists(JSON_FILE_PATH):
                with open(JSON_FILE_PATH, 'r') as file:
                    data = json.load(file)
            else:
                data = []
            
            # Get the column names dynamically
            column_names = ["roll_number", "name", "email"]

            # Render the data in the template
            return render_template('admin.html', data=data, columns=column_names)
        else:
            return "Invalid Credentials", 401
    return render_template('admin_login.html')


@app.route('/')
def index():
    return render_template('index.html')

JSON_FILE_PATH = 'users.json'

def save_to_json(new_data):
    # Check if the JSON file exists
    if os.path.exists(JSON_FILE_PATH):
        # Load existing data from the JSON file
        with open(JSON_FILE_PATH, 'r') as file:
            data = json.load(file)
    else:
        # Initialize an empty list if the file doesn't exist
        data = []
    
    # Append the new user data to the list
    data.append(new_data)
    
    # Write the updated data back to the JSON file
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/inside', methods=['GET', 'POST'])
def inside():
    if request.method == 'POST':
        roll_number = request.form['roll_number']
        name = request.form['name']
        email = request.form['email']

        # Create a dictionary for the new user
        new_user = {
            'roll_number': roll_number,
            'name': name,
            'email': email
        }
        
        # Save the new user data to the JSON file
        save_to_json(new_user)
        
        # Redirect to the leaderboard after successful submission
        return redirect(url_for('leaderboard'))

    return render_template('inside.html')


@app.route('/success')
def success():
    return "<h1>Data submitted successfully!</h1>"

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')  # Placeholder for the leaderboard

@app.route('/game1')
def game1():
    return render_template('game1.html')

@app.route('/game2')
def game2():
    return render_template('game2.html')

@app.route('/game3')
def game3():
    return render_template('game3.html')

@app.route('/game4')
def game4():
    return render_template('game4.html')

@app.route('/game5')
def game5():
    return render_template('game5.html')

@app.route('/game6')
def game6():
    return render_template('game6.html')

@app.route('/game10')
def game10():
    return render_template('game10.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
