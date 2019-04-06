print("判断密码强度：")
import string
#password =input("请输入密码：")
password_strong = 0
strpun = ""
while True:
    password =input("请输入密码：")
    if len(password) >= 6 :
        password_strong += 1

    for i in password:
        if i.isalnum():
            strpun += "1"
        elif i in string.punctuation:
            strpun += "2"
    if "1" in strpun and "2" in strpun:
        password_strong += 1

    if password_strong == 1:
        print("密码强度为低")
    elif password_strong == 2:
        print("密码强度为强")
    else:
        print("您输入的密码不符合要求")
        break
