a = input()
a = int(a)
b = input()
b = int(b)

b1 = (int)(b/100)
b2 = (int)((b - (b1*100))/10)
b3 = (int)(b-(b1*100)-b2*10)

print(a*b3)
print(a*b2)
print(a*b1)
print(a*b)