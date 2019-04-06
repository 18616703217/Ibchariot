#encoding utf-8
def func(a):
    while 1:
        if a[0] in b or a[0] == "_":
            print("您输入的变量名合法")
            
        else:
            print("您输入的变量名不合法")
        break

if __name__=="__main__":
    import string
    b=string.ascii_letters
    c=str(input("请输入变量名: "))
    func(c)