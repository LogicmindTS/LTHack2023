from flask import Flask,render_template,jsonify
from database import engine 
from sqlalchemy import text

app = Flask(__name__)



   
@app.route("/")

def hello_world():
    return render_template("login.html")

if __name__ == "__main__":
 app.run(host="0.0.0.0",debug=True)