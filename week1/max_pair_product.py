def maximum_pairwise_prod(numbers,n):
    # numbers = numbers.sort()
    numbers.sort()
    return numbers[-1]*numbers[-2]

def maximum_pairwise_prodFAST(numbers,n):
    index = 0
    for i in range(1,n):
        if(numbers[index]<numbers[i]):
            index = i

    temp = numbers[n-1]
    numbers[n-1] = numbers[index]
    numbers[index] = temp
    index = 0
    for i in range(1,n-1):
        if(numbers[index]<numbers[i]):
            index = i 
    return numbers[n-1]*numbers[index]   


if __name__=="__main__":
    n = int(input())
    numbers = [int(x) for x in input().split()]
    print(maximum_pairwise_prodFAST(numbers,n))
