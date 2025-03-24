from flask import Flask, request, render_template, redirect, jsonify
from Database.Manage_database import Manage_db



app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e)
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        mangae_db = Manage_db("Sampledatabase")
        client = mangae_db.get_client()
        db = client["Sampledatabase"]
        collection = db["RawData"]
        data = list(collection.find({}, {"_id": 0}))
        return jsonify(data)
    
    except Exception as e:
        return str(e)
    

if __name__ == "__main__":
    app.run(debug=True)