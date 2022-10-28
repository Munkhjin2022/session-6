
response = str(input("Do you want to calculate interest? (Yes or No)"))

while response =="Yes":
    p = float(input("Enter principle amount"))
    i = float(input("Enter interest amount"))

    itotal = 0.0

    for count in range(1, 6, 1):
        inta = p * i
        ebal = p + inta
        itotal = itotal + inta
        p = ebal
        
        print("Year", "Beg Bal", "End Bal")
        print(count, "", p, "   ", ebal) 
        print("Total interest earned: ", itotal)

response = input("Do you want to calculate again?(Yes or No)")
