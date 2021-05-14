print("""
****************************
Welcome To My Blog
***************************
""")



name = "hakan"
password = "hakan12345!"
counter = 0

while True:
    user_name = input("Please enter your username: ")
    keyword = input("Please enter your password: ")
    if counter == 3:
        print("3 attempt is used.Your right is up")
        break
    elif name == user_name and password == keyword:
        print("Welcome!!!")
        break
    elif name != user_name and password != keyword:
        print("Username or password is wrong.Please try again!")
        counter += 1 