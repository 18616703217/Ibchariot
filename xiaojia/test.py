def func(a):        
    if a[0] not in  start_rule:
         return"变量名不符合开头只能用字母下划线要求"         
    for i in a[1:]:
        if i not in end_rule:
            return"变量名不符合内容值能用字母或下划线"          
    return"变量名合法"

if __name__ =="__main__":
    import string
    start_rule = string.ascii_letters+"_"
    end_rule = string.ascii_letters+"_"+"".join([str(i) for i in range(10)])
    a=input("请输入变量名: ")
    assert_rule_retsult = func(a)
    print("%s 断言规则结果为：%s" % (a,assert_rule_retsult))
      

