#Grade based on 5 subject marks
m1 = int(input("Enter marks 1: "))
m2 = int(input("Enter marks 2: "))
m3 = int(input("Enter marks 3: "))
m4 = int(input("Enter marks 4: "))
m5 = int(input("Enter marks 5: "))

total = m1 + m2 + m3 + m4 + m5
per = total / 5

if per >= 60:
    print("First Class")
elif per >= 50:
    print("Second Class")
elif per >= 40:
    print("Pass")
else:
    print("Fail")
