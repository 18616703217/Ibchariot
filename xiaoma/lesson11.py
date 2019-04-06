"""
create_name:xiaoma
create_time:2019/04/06
discription::python变量名合法化
"""

def judgenames():
    py_word = input("请输入python变量名")
    strpun = ""
    if py_word[0].isalpha() or py_word[0] == "_":

        for i in py_word[1:]:

            if i.isalnum() or i == "_":
                strpun += "1"           
            else:
                strpun += "2"               

        if "1" in strpun:
            return "您输入的变量名合法"
        elif "2" in strpun:
            return "您输入的变量名中间内容不合法"
   
    else:
        return "您输入的开头不满足要求，变量名不合法"

if __name__ == "__main__":
    result = judgenames()
    print(result)