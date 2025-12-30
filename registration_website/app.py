from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    father = request.form["father"]
    mother = request.form["mother"]
    phone = request.form["phone"]
    email = request.form["email"]
    gender = request.form["gender"]

    file_exists = os.path.isfile("data.csv")

    with open("data.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Name", "Father", "Mother", "Phone", "Email", "Gender"])
        writer.writerow([name, father, mother, phone, email, gender])

    return redirect(url_for("success"))

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

