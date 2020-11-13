a,b = input().split()
a = int(a)
b = int(b)

if b>=45 :
    print(a,(b-45)," ")
else :
    if a==0 : print(23,(b+60-45)," ")
    else : print((a-1),(b+60-45)," ")
