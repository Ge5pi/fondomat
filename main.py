from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'a really really really really long secret key'


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/product")
def product():
    return render_template("product.html")


@app.route("/company")
def company():
    return render_template("company.html")


@app.route("/partners")
def partners():
    return render_template("partners.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/news")
def news():
    return render_template("news")


if __name__ == '__main__':
    app.run(debug=True)
