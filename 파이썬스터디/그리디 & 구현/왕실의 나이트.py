n = input()
x = int(n[1])
y = n[0]

list_a = ['a','b','c','d','e','f','g','h']
y = list_a.index(y)+1
dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]
cnt =0
for i in range(8) :
    tempx = x
    tempy = y
    tempx +=dx[i]
    tempy +=dy[i]
    if tempx>=1 and tempx<=8 and tempy>=1 and tempy<=8 :
        cnt+=1


print(cnt)