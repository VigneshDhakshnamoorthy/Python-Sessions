from flask import Flask, render_template
from Sql_Testing.sql_testing_1 import sql_query

app = Flask(__name__)


@app.route('/', methods=("POST", "GET"))
def contact_page():
    return render_template("index.html", tables=[sql_query[['AFENT_FULLNAME', 'EMP_CODE', 'AGENT_USERNAME', 'AGENT_PASSWORD']].to_html(classes='table', index=False)])


if __name__ == '__main__':
    app.run(debug=True)
