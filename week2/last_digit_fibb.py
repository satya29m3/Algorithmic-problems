def last_digit_fibb(n):
    prev = 0
    current = 1
    if n<=1:
        return n
    for i in range(2,n+1):
        prev , current = current,(prev+current)%10
    last_digit = str(current)
    return last_digit[-1]

if __name__=="__main__":
    n = int(input())
    print(last_digit_fibb(n))