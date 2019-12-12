from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session
from databases import *

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######

@app.route("/")
def home_page():
	return render_template ("home.html")

@app.route("/storepage")
def storepage():
	products = query_all()
	return render_template("store.html", products= products)


@app.route("/cartpage")
def cartpage():
	return render_template("cart.html")
#####################


if __name__ == '__main__':
    app.run(debug=True)