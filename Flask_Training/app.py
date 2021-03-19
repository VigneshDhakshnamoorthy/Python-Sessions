from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    name = "Home Page"
    return render_template("index.html", name=name)


@app.route('/contact')
def contact_page():
    name = "Contact Page"
    return render_template("contact.html", name=name)


if __name__ == '__main__':
    app.run(debug=True)
