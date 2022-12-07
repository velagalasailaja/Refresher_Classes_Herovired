p1=float(input("Quantity of p1:"))
p2=float(input("Quantity of p2:"))
p3=float(input("Quantity of p3:"))
price1=int(input("price of p1:"))
price2=int(input("price of p2:"))
price3=int(input("price of p3:"))
if(p1<=0 or p2<=0 or p3<=0):
    print("Enter positive number")
else:
    total=(p1*price1)+(p2*price2)+(p3*price3)
    print("User need to pay:",total)




