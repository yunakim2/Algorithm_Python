str = input()
cnt = 0
for i in range(len(str)) :
    if(str[i]=='A' or str[i]=='B' or str[i]=='C') :
        cnt = cnt+3
    elif(str[i]=='D' or str[i]=='E' or str[i]=='F') :
        cnt = cnt+4
    elif (str[i] == 'G' or str[i] == 'H' or str[i] == 'I'):
        cnt = cnt+5
    elif(str[i]=='J' or str[i]=='K' or str[i]=='L') :
        cnt = cnt+6
    elif (str[i] == 'M' or str[i] == 'N' or str[i] == 'O'):
        cnt = cnt+7
    elif (str[i] == 'P' or str[i] == 'Q' or str[i] == 'R' or str[i]=='S'):
        cnt = cnt+8
    elif (str[i] == 'T' or str[i] == 'U' or str[i] == 'V'):
        cnt = cnt+9
    elif (str[i] == 'W' or str[i] == 'X' or str[i] == 'Y' or str[i]=='Z'):
        cnt = cnt+10
    else : cnt = cnt +2


print(cnt)


