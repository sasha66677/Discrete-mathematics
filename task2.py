def countDecodings(S):
    if not S or S[0] == '0':
        return 0

    length = len(S)
    prev = 1
    curr = 1

    for i in range(2, length + 1):
        next_val = 0

        # Расшифровка текущей цифры отдельно
        if S[i - 1] != '0':
            next_val = curr

        # Расшифровка пары цифр вместе, если возможно
        two_digit = int(S[i - 2:i])
        if 10 <= two_digit <= 26:
            next_val = (next_val + prev)

        prev = curr
        curr = next_val

    return curr % 1000000007


S = input()
result = countDecodings(S)
print(result)
