def EuclidGCD(a,b):
    if(b==0):
        return a
    a_prime = a%b
    return EuclidGCD(b,a_prime)

def lcm(a,b):
    gcd = EuclidGCD(a,b)
    new_a = a/gcd
    new_b = b/gcd
    return int(new_a*new_b*gcd)

    
if __name__=="__main__":
    [a,b] = [int(x) for x in input().split()]
    print(lcm(a,b))
