def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def kth_permutation(n, k):
    numbers = list(range(1, n + 1))
    permutation = []
    k -= 1  # Приводим k к индексу (отсчет с нуля)

    for i in range(n, 0, -1):
        fact = factorial(i - 1)  # factorial of the current number

        index = k // fact
        permutation.append(numbers[index])  # Add an element to the permutation and remove it from the list of numbers
        numbers.pop(index)

        k %= fact  # Update k for the next iteration
    return permutation


numElementsToPermute, pos = map(int, input().split())
result = kth_permutation(numElementsToPermute, pos)
result = ''.join(str(num) for num in result)

print(result)
