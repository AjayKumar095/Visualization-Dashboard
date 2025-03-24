from flask import Flask, request, render_template, redirect
from Database.Manage_database import Manage_db



app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)