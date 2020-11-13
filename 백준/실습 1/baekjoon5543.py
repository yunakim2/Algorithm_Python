bg1 = int(input())
bg2 = int(input())
bg3 = int(input())
drink1 = int(input())
drink2 = int(input())
sum = 0
if bg1 >= bg2:
    if bg2 >= bg3:
        sum += bg3
    else:
        sum += bg2
else:
    if bg1 >= bg3:
        sum += bg3
    else:
        sum += bg1


if drink1> drink2 :
    sum+= drink2
else :
    sum+= drink1

print(sum-50)
