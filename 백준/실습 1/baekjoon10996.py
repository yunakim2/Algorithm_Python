a = int(input())

even = a//2
odd = a- a//2

for i in range(a) :
    print("* "*odd)
    print(" *"*even)