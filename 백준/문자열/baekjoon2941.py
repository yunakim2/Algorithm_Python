str = input()

croatia = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in range(len(croatia)) :
    str = str.replace(croatia[i],"a")


print(len(str))
