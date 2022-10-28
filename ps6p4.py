f=open("data2.txt", "r")

sumextprice=0.0
c=0

item=f.readline()

while item != "":
  qty=int(f.readline())
  price=float(f.readline())

  extprice=qty*price

  sumextprice=sumextprice+extprice
  c=c+1

  print()
  print("Item: ", item)
  print("Quantity: ", qty)
  print("Price: ", price)
  print("Extended price: ", extprice)

  item=f.readline()

f.close()
avg=sumextprice/c

print() 
print("Sum of extended orders: ", sumextprice)
print("Number of orders: ", c)
print("Average orders: ", avg)