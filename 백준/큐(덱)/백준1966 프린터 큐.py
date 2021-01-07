import heapq

n = int(input())

for _ in range(n):
    _, j = map(int, input().split())
    h = list(map(int, input().split()))
    heaq = []
    for i, item in enumerate(h):
        heapq.heappush(heaq, (item, i))

    size = len(heaq)
    heaq = sorted(heaq, key = lambda item : item[1] , reverse=True)
    print(heaq)
    print(heaq.index(heaq[0]))

    # for k in range(len(heaq)):
    #     print("item :: ",item , "key :: ",k)
    #     if item[1] == j:
    #         print(k+1)
    #         break
