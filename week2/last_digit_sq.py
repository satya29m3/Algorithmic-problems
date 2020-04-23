def fibbonacci(n):
    prev= 0
    current =1
    if (n<=1):
        return n
    for i in range(2,n+1):
        prev ,current = current, (prev+current)%10
    return current

def pisano_period(m):
    prev = 0
    current = 1
    i=2
    while True:
        prev , current = current, fibbonacci(i)%m
        i+=1
        if(prev==0 and current==1):
            return i-2

def last_digit_square(n):
    period = pisano_period(10)
    rem = int(n%period)
    current_sum = fibbonacci(rem) * fibbonacci(rem+1)
    return current_sum%10
if __name__=="__main__":
    n = int(input())
    print(last_digit_square(n))