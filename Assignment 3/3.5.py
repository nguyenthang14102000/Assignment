a = "python"
b = "rules"
n = 1
while n <=5:
    user_name = input("username:")
    password = input("password:")
    if user_name == a and password == b:
        print("Welcome")
        break
    else:
        print('wrong username or password')
        n = n + 1
else:
    print('Access Denied')


