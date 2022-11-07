def compt(code,credits):
  if code=="I":
    cpc=250
  else:
    cpc=500
  t=cpc*credits
  return t

name=input("Enter the last name ")
code=input("Enter disctrict code I or O")
crehours=float(input("Enter credit hours"))

t=compt(code,crehours)

print("The last name: ", name)
print("The tuition: ", t)
