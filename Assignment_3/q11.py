#Ticket calculation
total = 0
ticket = int(input("Enter ticket amount per person: "))

for i in range(5):
    age = int(input("Enter age: "))

    if age < 12:
        total = total + ticket * 0.7
    elif age > 59:
        total = total + ticket * 0.5
    else:
        total = total + ticket

print("Total ticket amount =", total)
