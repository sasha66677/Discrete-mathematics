def count_binary_strings(N, K):
    mod = 1000000007
    numerator = 1
    denominator = 1

    for i in range(K):
        numerator = numerator * (N - i)
        denominator = denominator * (i + 1)

    return (numerator // denominator) % mod


N, K = map(int, input().split())
result = count_binary_strings(N, K)
print(result)