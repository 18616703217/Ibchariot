def func(s,a):
    i = 0
    sum = 0
    while s.find(a,i) != -1:
        i = s.find(a,i) + 1 
        sum += 1
    return sum
    

if __name__ == "__main__":
    s = "".join([str(i) for i in [1,2,3,1,1,4,4,3]])
    dict_s={}
    for i in set(s):
        dict_s[i] = func(s,i)   
    print(dict_s)        
   