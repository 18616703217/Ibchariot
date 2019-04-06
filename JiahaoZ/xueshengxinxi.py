#encoding=utf-8
import time
def add_student_info(student_info_all):

    id = time.time()
    student_info={id:{"name":"","sex":"","born":"","admission_time":"",\
    "tel":"","address":""}}

    for i in range(3):
        name = input("请输入您的姓名： ")
        if name =="":
            print("您输入的姓名为空，请重新输入")
        else:
             student_info[id].update({"name":name})
             break
    else:
        print("您输入错误超过三次，请重新录入")
        return

    for i in range(3):
        sex = input("请输入您的性别(男/女)： ")
        if sex =="":
            print("您输入的性别为空，请重新输入")
        else:
            student_info[id].update({"sex":sex})
            break
    else:
        print("您输入错误超过三次，请重新录入")
        return

    for i in range(3):
        born = input("请输入出生日期，格式为：年-月-日 : ")
        born_tuple = tuple(born.split("-"))
        if len(born_tuple) == 3:
            student_info[id].update({"born":"%s年%s月%s日" % born_tuple})
            break
        else:
            print("您输入的内容 %s 格式错误，正确格式为:年-月-日" % born)
    else:
        print("您输入的出生日期错误超过三次，请重新录入")
        return

    for i in range(3):
        admission_time = input("请输入入学日期，格式为：年-月-日 : ")
        admission_time_tuple = tuple(admission_time.split("-"))
        if len(born_tuple) == 3:
            student_info[id].update({"admission_time":"%s年%s月%s日" % admission_time_tuple})
            break
        else:
            print("您输入的内容 %s 格式错误，正确格式为:年-月-日" % admission_time)
    else:
        print("您输入的入学日期错误超过三次，请重新录入")
        return

    for i in range(3):
        tel = input("请输入您的手机号码: ")
        if len(tel) == 11:
            student_info[id].update({"tel":tel})
            break
        else:
            print("您输入的内容 %s 格式错误，正确格式为:1XXXXXXXXXX" % tel)

    address = input("请输入您的家庭住址: ")
    student_info[id].update({"address":address})
    student_info_all.update(student_info)

def action():
    student_info_all ={}
    cmd = input("""请输入命令:
        输入out 退出程序
        输入add 添加学生信息: """)
    while cmd != "out":
        if cmd =="add":
            add_student_info(student_info_all)
            print(student_info_all)

    cmd = input("""请输入命令:
        输入out 退出程序
        输入add 添加学生信息: """)

if __name__ =="__main__":
    #主函数入口
    action()        

