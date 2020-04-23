def fibbonacci(n):
    prev= 0
    current =1
    if (n<=1):
        return n
    for i in range(2,n+1):
        prev ,current = current, prev+current
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

def last_digit_partial(m,n,k=10):
    period = pisano_period(k)
    rem1 = int(m%period)
    rem2 = int(n%period)
    current_sum = 0
    if(rem2<rem1):
        rem2 += period
    for i in range(rem1,rem2+1):
        current_sum += fibbonacci(i)
    return current_sum%10
    

if __name__=="__main__":
    [m,n] = [int(x) for x in input().split()]
    print(last_digit_partial(m,n))
