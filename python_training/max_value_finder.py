Salary = {"Vignesh": 1500000, "DV": 90000, "vicky": 250000}

Max_salary = max(Salary.values())
for name, salary in Salary.items():
    if salary == Max_salary:
        txt = "Highest Paid Employee = {} : {}"
        print(txt.format(name, salary))

name, salary = zip(*Salary.items())
print(name)
print(salary)
