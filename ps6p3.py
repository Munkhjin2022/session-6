f = open("data1.txt", "r")

totalbonus = 0

name = f.readline()
while name != "":
    salary = float(f.readline())

    if salary >= 100000.00:
        bonusrate = 0.20
    elif salary >= 50000.00:
        bonusrate = 0.15
    else:
        bonusrate = 0.10

    bonus = salary * bonusrate
    totalbonus = totalbonus + bonus

    print("Employee: ", name)
    print("Salary: ", salary)
    print("Bonus: ", bonus)

    name = f.readline()
f.close()

print("Total bonus: ", totalbonus)
