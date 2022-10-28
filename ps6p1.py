
response = str(input("Do you want to calculate interest? (Yes or No)"))

while response =="Yes":
    p = float(input("Enter principle amount"))
    i = float(input("Enter interest amount"))

    itotal = 0.0

    for count in range(1, 6, 1):
        inta = p * i
        ebal = p + inta
        print("Year", "Beg Bal", "End Bal")
        print(count, "", p, "   ", ebal)

        itotal = itotal + inta
        p = ebal

response = input("Do you want to calculate again?(Yes or No)")

print("Total interest earned: ", itotal)
