from collections import deque


if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N,M,K,A,B = map(int,input().split())
        A -= 1
        B -= 1

        a = list(map(int, input().split()))
        b = list(map(int,input().split()))
        t = deque(list(map(int, input().split())))

        time = 0
        id_value = 1
        result = {}
        tmp_p = deque()
        tmp_a = [[0,0] for _ in range(N)]
        tmp_b = [[0,0] for _ in range(M)]

        tmp_b2 = deque()

        while True:
            tmp_a_size = tmp_a.count([0,0])
            tmp_b_size = tmp_b.count([0,0])
            if len(t) == 0 and len(tmp_p) == 0 and tmp_a_size == N and tmp_b_size == M:
                break
            # print('*******************시작*******************',time)
            while len(t) > 0 and time == t[0]:
                    t.popleft()
                    tmp_p.append([id_value, time])
                    id_value +=1
            # print('---time 시간에 들어온 것들 --',tmp_p)
            for k, item in enumerate(tmp_b):
                # print('-- 정비 처리 중 ---')
                if item == [0,0]:
                    continue
                b_time = item[1] -1
                if b_time > 0:
                    tmp_b[k] = [item[0], b_time]
                else:
                    tmp_b[k] = [0,0]
            # print('-- 정비 처리 완료---' , tmp_b)

            for k , item in enumerate(tmp_a):
                # print('---접수 처리 중 --')
                if item == [0,0]:
                    continue
                a_time = item[1] -1
                if a_time > 0:
                    tmp_a[k] = [item[0], a_time]
                else:
                    # print('정비에 넣어주기 --')
                    ''' 정비소 처리 과정'''
                    tmp_b2.append(tmp_a[k][0])
                    tmp_a[k] = [0,0]

            size_b = tmp_b.count([0,0])
            while True:
                # print('접수 창구 --')
                # print('p--',tmp_p, 'a--',tmp_a)
                if len(tmp_b2) >= 1:
                    if size_b == 0:
                        break
                    i= tmp_b2.popleft()
                    for idx, item in enumerate(tmp_b):
                        if item == [0, 0]:
                            tmp_b[idx] = [i, b[idx]]
                            size_b -= 1
                            result[i] = result[i] + [idx]
                            break
                else:
                    break
            # print()
            # print('--- 접수 처리 완료 -- ', tmp_a)
            size = tmp_a.count([0,0])
            '''남는 창구 개수만큼 p 뽑아냄 단 tmp_p 중 time 인 것 만'''
            '''접수 창고 처리 과정'''
            while True:
                # print('접수 창구 --')
                # print('p--',tmp_p, 'a--',tmp_a)
                if len(tmp_p) >= 1:
                    if time < tmp_p[0][1] or size == 0:
                        break
                    i, _ =  tmp_p.popleft()

                    for idx, item in enumerate(tmp_a):
                        if item == [0,0]:
                            tmp_a[idx] = [i,a[idx]]
                            size -= 1
                            result[i] = [idx]
                            break
                else:
                    break
            # print('*******************처리 끝*******************')
            # print('time--',time)
            # print('result --' , result)
            # print('p--', tmp_p)
            # print('tmp-a ',tmp_a, 'tmp_b', tmp_b)
            time += 1

        ans = 0
        for idx in result.keys():
            if result[idx] == [A,B]:
                ans += idx

        if ans == 0:
            ans = -1
        print('#{} {}'.format(test_case, ans))



