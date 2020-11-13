str =input()
alpha = [0 for i in range(26)]
for i in range(0, len(str)) :
    c = ord(str[i])
    if(c>=97) : c = c-32
    c = c - 65
    alpha[c] = alpha[c]+1

max = 0
for i in range(len(alpha)) :
    if(alpha[max]<=alpha[i]) : max = i

temp = 0
for i in range(len(alpha)) :
        if alpha[max] == alpha[i] : temp = temp+1

if(temp>1) : print("?")
else : print(chr(max+65))
