def judgenames():
    py_word = input("请输入python变量名")
    strpun = ""
    if py_word[0].isalpha() or py_word[0] == "_":

        for i in py_word[1:]:

            if i.isalnum() or i == "_":
                strpun += "1"           
            else:
                break

        if "1" in strpun:
            print("您输入的变量名合法")
        else:
            print("您输入的变量名中间内容不合法")
   
    else:
        print("您输入的开头不满足要求，变量名不合法")

if __name__ == "__main__":
    judgenames()