from flask import Flask, render_template, redirect, request

app = Flask(__name__)
file_loc = "Login_App/datebase/user_details.txt"


@app.route("/", methods=("POST", "GET"))
def main_page():
    if request.method == 'POST':
        u_name = request.form['u_name']
        u_pass = request.form['u_pass']
        return login_old(u_name, u_pass)

    else:
        return render_template("login.html")


def login_old(name, password):
    success = False
    with open(file_loc, 'r') as file:
        for i in file:
            a, b = i.split(",")
            b = b.strip()
            if a == name and b == password:
                success = True
                break
    if success:
        return render_template("login_success.html", name=name)
    else:
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
