def gcd(a,b):
    best = 0
    for i in range(1,a+b+1):
        if (a%i==0 and b%i==0):
            best = i
    return best

def EuclidGCD(a,b):
    if b==0:
        return a
    a_prime = a%b
    return EuclidGCD(b,a_prime)

if __name__=="__main__":
    [a,b] = [int(x) for x in input().split()]
    print(EuclidGCD(a,b))