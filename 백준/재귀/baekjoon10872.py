num = int(input())

def fac (i) :
    if(i == 1 ) : return 1
    if(i ==0) : return 1
    else :
        return i*fac(i-1)



print(fac(num))