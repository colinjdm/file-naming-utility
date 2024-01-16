import csv
import sqlite3

from flask import Flask, redirect, render_template, request


app = Flask(__name__)

# Configure SQLite database
db = sqlite3.connect("filenaming.db")


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("index.html")

    # Show the filing page, but with pre-loaded values from sites.html
    if request.method == "POST":
        name = request.form.get('name') # This isn't used currently, but may be added
        masterid = request.form.get('masterid')
        # Get rid of "None" values so that they don't enter the form
        if masterid == "None":
            masterid = ""
        # Get rid of "None" values so that they don't enter the form
        permit = request.form.get('permit')
        if permit == "None":
            permit = ""
        # Get rid of "None" values so that they don't enter the form
        county = request.form.get('county')
        if county == "None":
            county = ""
        return render_template("indexed.html",
                               name=name,
                               masterid=masterid,
                               permit=permit,
                               county=county)

@app.route("/sites", methods=["GET", "POST"])
def sites():
    # SELECT all sites in the database to be displayed on sites.html
    if request.method == "GET":
        sites = db.execute("SELECT * FROM facilities ORDER BY name")
        return render_template("sites.html",
                            sites=sites)

    # SELECT only those sites whose "masterid"s partially match the search term
    if request.method == "POST":
        search = request.form.get("search")
        sites = db.execute("SELECT * FROM facilities WHERE name LIKE ? ORDER BY name", ('%' + search + '%'))
        return render_template("sites.html",
                            sites=sites)

@app.route("/counties")
def counties():
    # Initialize an empty list where each row of the CSV can be saved as a dictionary
    counties = []
    # County codes obtained from https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt
    with open('static/ALcounties.csv', 'r', newline='') as csvfile:
        ALcounties = csv.reader(csvfile)
        for row in ALcounties:
            # Strip blank spaces from CSV row (thanks CS50.ai duck debugger!)
            row = [field.strip() for field in row]
            # Save each line in the CSV as a dictionary
            dict = {'state':row[0], "code":row[1], "name":row[2]}
            counties.append(dict)
    print(counties)
    return render_template("counties.html",
                           counties=counties)

