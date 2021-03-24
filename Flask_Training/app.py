from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    name = "Home Page"
    return render_template("index.html", name=name)


@app.route('/contact')
def contact_page():
    details = {"Name" : "KMDV", "Location" : "International", "Type":"Private Limited"}
    return render_template("contact.html", details=details)


if __name__ == '__main__':
    app.run(debug=True)
