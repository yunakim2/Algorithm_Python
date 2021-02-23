N = 5
cnt = 0

for hour in range(N+1):
    for m in range(60):
        for sec in range(60):
            if str(hour).count('3') or str(m).count('3') or str(sec).count('3'):
                cnt += 1

print(cnt)
