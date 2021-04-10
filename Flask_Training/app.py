from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route('/')
def main_page():
    name = "Home Page"
    return render_template("index.html", name=name)


@app.route('/contact')
def contact_page():
    details = {"Name": "KMDV", "Location": "International", "Type": "Private Limited"}
    return render_template("contact.html", details=details)


@app.route('/data', methods=("POST", "GET"))
def dynamic_data():
    file_loc = "Selenium_Training/Files/moneydata.xlsx"
    data_in = pd.read_excel(file_loc)
    return render_template("data.html", tables=[data_in.to_html(classes='table', index=False)])


if __name__ == '__main__':
    app.run(debug=True)
