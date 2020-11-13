s = input()

alpha = []
cnt =0
for i in s :
    if i>='A' and i <='Z' :
        alpha.append(i)
    else :
        cnt += int(i)
alpha.sort()
if cnt!=0 :
    alpha.append(str(cnt))

print(''.join(alpha),end='')