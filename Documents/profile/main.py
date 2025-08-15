from  flask import Flask, render_template, request, redirect, url_for, session, flash
import uuid
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/init')
def init_db():
    conn = sqlite3.connect('portfolio.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS experiences (experience_id TEXT PRIMARY KEY, position VARCHAR(255) NOT NULL,company_name VARCHAR(255) NOT NULL, company_address VARCHAR(255), start_date VARCHAR(255), end_date VARCHAR(255))''')
    conn.commit()
    return conn


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)