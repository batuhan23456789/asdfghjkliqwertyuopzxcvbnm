from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/info")
def info_page():
    return render_template("info.html")

@app.route("/random_fact")
def random_fact():
    return render_template("random_fact.html")
    

app.run(debug=True)