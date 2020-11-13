
list = []
for i in range(10) :
    num = int(input())
    num = num%42
    if(num in list) : continue
    else : list.append(num)


print(len(list))