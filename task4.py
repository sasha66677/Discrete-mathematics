def count_binary_strings(N, K):
    mod = 1000000007

    def binomial_coefficient(n, k):
        if k > n - k:
            k = n - k
        numerator = 1
        denominator = 1
        for i in range(k):
            numerator = numerator * (n - i) % mod
            denominator = denominator * (i + 1) % mod
        return numerator * pow(denominator, mod - 2, mod) % mod

    return binomial_coefficient(N, K)


N, K = map(int, input().split())
result = count_binary_strings(N, K)
print(result)
