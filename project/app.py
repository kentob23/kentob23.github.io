from flask import Flask, flash, redirect, render_template, request, url_for

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded <-- Basically, changes are updated in real time
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", title="home")

@app.route("/members", methods=["GET", "POST"])
def members():
    return render_template("members.html", title="members")

@app.route("/reid", methods=["GET", "POST"])
def reid():
    return render_template("reid.html", title="members")

@app.route("/gorilla", methods=["GET", "POST"])
def gorilla():
    return render_template("gorilla.html", title="members")

@app.route("/bora", methods=["GET", "POST"])
def bora():
    return render_template("bora.html", title="members")

@app.route("/noah", methods=["GET", "POST"])
def noah():
    return render_template("noah.html", title="members")

@app.route("/lisa", methods=["GET", "POST"])
def lisa():
    return render_template("lisa.html", title="members")

@app.route("/hendy", methods=["GET", "POST"])
def hendy():
    return render_template("hendy.html", title="members")

@app.route("/hinano", methods=["GET", "POST"])
def hinano():
    return render_template("hinano.html", title="members")

@app.route("/gil", methods=["GET", "POST"])
def gil():
    return render_template("gil.html", title="members")

@app.route("/kamito", methods=["GET", "POST"])
def kamito():
    return render_template("kamito.html", title="members")

@app.route("/met", methods=["GET", "POST"])
def met():
    return render_template("met.html", title="members")

@app.route("/kanae", methods=["GET", "POST"])
def kanae():
    return render_template("kanae.html", title="members")

@app.route("/faq", methods=["GET", "POST"])
def faq():
    return render_template("faq.html", title="faq")

@app.route("/clippers", methods=["GET", "POST"])
def clippers():
    return render_template("clippers.html", title="clippers")