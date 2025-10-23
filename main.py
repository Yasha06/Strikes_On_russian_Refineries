from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "123"
Bootstrap5(app)

@app.route('/')
def home():
    return render_template("home_page.html")


@app.route('/analytics', methods=["GET", "POST"])
def analytics():
        return render_template("analytics.html")


@app.route('/search', methods=["GET", "POST"])
def map():
        return render_template("map.html")


if __name__ == "__main__":
    app.run(debug=False)

