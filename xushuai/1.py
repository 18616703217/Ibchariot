def func():
    a=input("请输入变量名:")
    if a[0].isalpha() or a[0] == "_":
        if a[1::].isalnum() or a[1::] == "_":
            print("该变量名合法")
        else:
            print("该变量名中间内容不合法")
    else:
        print("该变量名开头不合法")
func()














     