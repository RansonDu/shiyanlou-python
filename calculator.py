#!/usr/bin/env python3


import sys


def get_income(salary):
    insurance = salary * (0.08 + 0.02 + 0.005 + 0.06)
    salary_tax = salary - insurance - 3500
    tax = 0
    if 0 <= salary_tax < 1500:
        tax = salary_tax * 0.03
    elif 1500 <= salary_tax < 4500:
        tax = salary_tax * 0.1 - 105
    elif 4500 <= salary_tax < 9000:
        tax = salary_tax * 0.2 - 555
    elif 9000 <= salary_tax < 35000:
        tax = salary_tax * 0.25 - 1005
    elif 35000 <= salary_tax < 55000:
        tax = salary_tax * 0.3 - 2755
    elif 55000 <= salary_tax * 0.35:
        tax = salary_tax * 0.35 - 5505
    elif salary_tax > 80000:
        tax = salary_tax * 0.45 - 13505
    get_income = salary - insurance - tax
    get_income = format(get_income, ".2f")
    return get_income


ID_salary = []
for arg in sys.argv[1:]:
    i = arg.split(":")
    try:
         salary = int(i[1])
    except:
        print("Parameter Error")
    i[1] = get_income(salary)
    ID_salary.append(i)

for i in ID_salary:
    print("{0}:{1}".format(i[0], i[1]))

