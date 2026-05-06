def spy (n):

    def sod(n1):
        sum = 0
        while n1>0:
          digit = n1%10
          sum = sum + digit
          n1 = n1//10
        return sum
    def pod(n1):
        pro = 1
        while n1>0:
          digit = n1%10
          pro = pro * digit
          n1 = n1//10
        return pro
    

    if sod(n) == pod(n) :
       return True
    else:
       return False

print(spy(123))