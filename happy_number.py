
def happy(n):
    for _ in range(100):  # limit iterations
        sum_sq = 0
        while n > 0:
            digit = n % 10
            sum_sq += digit * digit
            n //= 10
        n = sum_sq
    return n == 1

print(happy(70))