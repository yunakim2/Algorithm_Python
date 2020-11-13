import collections

def solution(participant, completion):
    answer=collections.Counter(participant)-collections.Counter(completion)
    return list(answer.keys())[0]


p = ["leo", "kiki", "eden"]
c = ["eden", "kiki"]

print(solution(p,c))