#Check userid and password
userid = input("Enter userid: ")
password = input("Enter password: ")

if userid == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid userid or password")
