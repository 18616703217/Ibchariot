def func(variable_value):
    if variable_value[0] not in start_rule:
        return "变量名不符合开头只能用字母下划线要求"
    for i in variable_value[1:]:
        if i not in end_rule:
            return "变量名不符内容只能用字母数字下划线"
    return "变量合法" 

if __name__=="__main__":
    import string
    start_rule = string.ascii_letters+"_"
    end_rule = string.ascii_letters+"_"+"".join([str(i) for i in range(10)])
    variable_value=input("请输入变量名: ")
    assert_rule_retsult = func(variable_value)
    print("%s 断言规则结果为：%s" % (variable_value,assert_rule_retsult))
    