import string
import random
import requests
a = [i for i in range(10)]
b = list(string.ascii_letters)
data = {"t1":1,"t2":1,"t3":1}
for n in range(10):
    for i in data.keys():
        d = random.choice([[i for i in range(10)],list(string.ascii_letters)][random.randint(0,1)])
        data[i] = d
    result = requests.post("http://47.98.155.208:5000/rule",json = data).text
    print(data)
    print(result)
