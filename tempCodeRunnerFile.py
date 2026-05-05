def special(n):
    n1 = n
    def fact(a):
        if a == 1 or a == 0 :
            return 1
        else:
            return a * fact(a-1)
    def sod (n):