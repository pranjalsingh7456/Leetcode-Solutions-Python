def neon(n):
    n1 = n
    square = n1 * n1

    def sod(square):
        total = 0
        while square > 0:
            digit = square % 10
            total = total + digit
            square = square // 10
        return total

    s = sod(square)

    if s == n1:
        return True
    else:
        return False