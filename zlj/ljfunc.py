#encoding = utf-8

def func(var)
    if var[0].isalpha() or var[0] == "_":
        for i in var[1:]:
            if not(i.isalnum() or i == "_"):
                return("%s变量名不合法" %s)
            else:
                return("%s变量名合法" %s)
    else:
        print("%s变量名不合法" %s)

if __name__ ="__main__":
    func(judgenames)
        