def solution(s):
    def is_palindrome(word):
        return word == word[::-1]

    for idx in range(len(s), 0, -1):
        for start in range(0, len(s)):
            word = s[start:start + idx]
            if is_palindrome(word):
                return len(word)
            if start + idx >= len(s):
                break
    return 0


if __name__ == "__main__":
    print(solution("abcdcba"))
    print(solution("abacde"))
