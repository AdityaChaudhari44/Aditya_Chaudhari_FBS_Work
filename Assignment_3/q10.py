#Marriage eligibility
gender = input("Enter gender (M/F): ")
age = int(input("Enter age: "))

if gender == 'M' and age >= 21:
    print("Eligible to marry")
elif gender == 'F' and age >= 18:
    print("Eligible to marry")
else:
    print("Not eligible")
