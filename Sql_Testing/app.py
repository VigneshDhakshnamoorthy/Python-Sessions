from flask import Flask, render_template
import pandas as pd

app=Flask(__name__)
sql_query=pd.read_csv("database.txt")

sql_query['SCHEME_NAME']=sql_query['SCHEME_NAME'].str.upper()


@app.route('/', methods=("POST", "GET"))
def database_page():
    return render_template("index.html", tables=[sql_query[['SCHEME_NAME', 'GRAND_TOTAL']].loc[sql_query['GRAND_TOTAL']
                                                                                               > 599].sort_values(
        by='GRAND_TOTAL', ascending=False).reset_index(
        drop=True).to_html(classes='table', index=True)])


@app.route('/select', methods=("POST", "GET"))
def select_page():
    product_list = sql_query['SCHEME_NAME'].loc[sql_query['GRAND_TOTAL'] > 599].sort_values(ascending=True)
    return render_template("select.html", product_list=product_list)


if __name__ == '__main__':
    app.run(debug=True)
