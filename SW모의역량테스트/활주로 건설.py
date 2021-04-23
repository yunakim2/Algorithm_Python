

from collections import deque
if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N, K = map(int,input().split())
        maps = [list(map(int,input().split())) for _ in range(N)]

        ans = 0
        '''가로 검사'''
        for i in range(N):
            print(maps[i])
            flag = False
            for j in range(N-K):
                if j == 0:
                    re_item = maps[i][j]
                else:
                    if re_item-1 == maps[i][j]:


            if flag:
                ans += 1
            print('---ans---', ans)







        '''세로 검사'''