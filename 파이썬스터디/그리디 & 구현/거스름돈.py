money = int(input())
count =0
c = [500,100,50,10]
for i in c :
    count += money//i
    money %=i


print(count)