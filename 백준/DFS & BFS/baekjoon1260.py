def bfs(n, v) :
    l = []
    l.append(v)
    checkbfs[v] = 1
    print(v+1,end=" ")
    while(len(l)!=0) :
        n1 = l[0]
        l.remove(n1)
        for i in range(n) :
            if num[n1][i]==1 and checkbfs[i]!=1 :
                l.append(i)
                print(i+1,end =" ")
                checkbfs[i]=1
    return


def dfs(i, n, v) :
    if i == n :
        return
    if checkdfs[v] == 1 :
        return
    checkdfs[v]=1
    print(v+1,end=" ")
    for j in range(n) :
        if num[v][j]==1 and checkdfs[j]!=1 :
            dfs(i+1,n,j)





n,m,v = map(int,input().split())
checkbfs = [0 for i in range(n)]
checkdfs = [0 for i in range(n)]
num = [[0 for col in range(n)] for row in range(n)]
for i in range(m) :
    n1,m1 = map(int,input().split())
    num[n1-1][m1-1] = 1
    num[m1-1][n1-1] = 1


dfs(0,n,v-1)
print()
bfs(n,v-1)


