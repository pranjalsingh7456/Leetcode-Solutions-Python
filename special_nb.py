def special(n):
    n1 = n

    def fact(a):
        if a == 0 or a == 1:
            return 1
        else:
            return a * fact(a-1)

    def sod_func(n):
        total = 0
        while n > 0:
            digit = n % 10
            total += fact(digit)
            n = n // 10
        return total

    s = sod_func(n1)

    if s == n1:
        return True
    else:
        return False


n1 = int(input("Enter number: "))
print(special(n1))