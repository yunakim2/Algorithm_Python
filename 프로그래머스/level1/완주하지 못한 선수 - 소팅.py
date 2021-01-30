def solution(participant, completion):
    participant.sort()
    completion.sort()
    for c_mem, p_mem in zip(completion, participant):
        if p_mem != c_mem:
            return p_mem
    else:
        return participant[-1]


if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
    print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
