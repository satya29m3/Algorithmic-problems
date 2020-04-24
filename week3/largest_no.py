def largest_number(numbers,n):
    for k in reversed(range(n)):
        index = 0
        for i in range(k+1):
            x = numbers[index]
            y = numbers[i]
            val1 = int(str(x) + str(y))
            val2 = int(str(y) + str(x))
            if(val1>val2):
                index = i
        temp = numbers[index]
        numbers[index] = numbers[k]
        numbers[k] = temp
        del temp
    return ''.join([str(x) for x in numbers])



            

if __name__=="__main__":
    n = int(input())
    numbers = [int(x) for x in input().split()]
    print(largest_number(numbers,n))