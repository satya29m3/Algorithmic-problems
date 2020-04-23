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



def fibbonacci_again(n,m):
    period = pisano_period(m)
    remainder = int(n%period)

    return fibbonacci(remainder)%m

if __name__=="__main__":
    [n,m] = [int(x) for x in input().split()]
    print(fibbonacci_again(n,m))