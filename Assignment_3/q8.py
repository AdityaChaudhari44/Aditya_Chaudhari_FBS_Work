#Simple captcha
userid = input("Enter userid: ")
password = input("Enter password: ")

if userid == "admin" and password == "1234":
    captcha = 4567   # fixed number (no random library)
    print("Captcha:", captcha)
    user_cap = int(input("Enter captcha: "))

    if user_cap == captcha:
        print("Success")
    else:
        print("Failed")
else:
    print("Invalid login")
