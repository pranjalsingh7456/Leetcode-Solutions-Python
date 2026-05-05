#Problem 1
def sod(n):
    r = n
    sum = 0 
    while n > 0 :
        digit = n%10
        sum =sum + digit
        n = n //10
    if r % sum == 0:
        return True
    else:
        return False

    
r = int (input("Enter the Number "))
print(sod(r))


#Problem 2
def sodc(m):
    t = m
    sum = 0
    i = len(str(m))
    while m > 0 :
        digit = (m%10)
        sum =sum + pow(digit,i)
        m = m //10
        i=i-1
    if t==sum:
        return True
    else:
        return False
    
t = int(input("Enter another number: "))
print(sodc(t))
    