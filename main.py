users = [["user1", "user1@gmail.com", "123"],
         ["user2", "user2@gmail.com", "123"],
         ["user3", "user3@gmail.com", "123"]
         ]
colpains = []


def userdashboard(useremail, username):
    print("Hello", username, "say How can i help u")
    cmpdata = input("enter yr complain")
    cmpdate = today = date.today()
    colpains.append([username, useremail, cmpdata, cmpdate])
    print("DONE.. we will work oin yr compln")
    login()


def login():
    email = input("enter email")
    password = input("enter password")
    if email == "admin@gmail.com" and password == "123":
        print("Login True")
        dashboard()


def dashboard():
    print("Welcome to dashboard...")
    for data in colpains:
        print(data)


def registration():
    username = input("enter yr name")
    useremail = input("enter email")
    userpassword = input("enter password")
    users.append([username, useremail, userpassword])
    print("REGISTRATION DONE..")
    return 1


def userlogin():
    email = input("enter email")
    password = input("enter password")
    for i in users:
        if i[1] == email and i[2] == password:
            print("Yes.. Login Now u can acess dashboard")
            userdashboard(email, i[0])
        else:
             print("Plz Check yr email and password")


def entrydata():
    print("Welcome TO AMC")
    role = int(input("1. For User and 2. For Admin"))
    if role == 1:
        clickperform = int(input("1. For Registration 2. Login 3.Exit"))
        if clickperform == 1:
            ans = registration()
            if ans == 1:
                ch = int(input("1. For Login and 2. Exit"))
                if ch == 1:
                    userlogin()
        elif clickperform == 2:
            userlogin()



    elif role == 2:
        login()


def main():
    entrydata()


main()

