#Profit or loss
cp = int(input("Enter cost price: "))
sp = int(input("Enter selling price: "))

if sp > cp:
    print("Profit =", sp - cp)
else:
    print("Loss =", cp - sp)

