from flask import Flask, render_template, url_for, send_file

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")