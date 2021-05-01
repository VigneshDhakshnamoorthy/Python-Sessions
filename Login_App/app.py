from flask import Flask, render_template, redirect, request

app = Flask(__name__)
file_loc = "Login_App/datebase/user_details.txt"
error_value = True


@app.route("/", methods=("POST", "GET"))
def main_page():
    if request.method == 'POST':
        u_name = request.form['u_name']
        u_pass = request.form['u_pass']
        value_lr = request.form['submit']
        if value_lr == 'Login':
            return login_old(u_name, u_pass)
        elif value_lr == 'Register':
            return register_new(u_name,u_pass)
        else:
            return redirect("/")

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
        return render_template("login.html", error_value=error_value)


def register_new(name, password):
    if bool(name) and bool(password):
        with open(file_loc, 'a') as file:
            file.write(f'\n{name},{password}')

        print(f'Registered :  name - {name} and password - {password}') 
        login_old(name, password)
        return render_template("Register_sucees.html",name=name)
    else:
        return render_template("login.html", error_value=error_value)


if __name__ == "__main__":
    app.run(debug=True)
