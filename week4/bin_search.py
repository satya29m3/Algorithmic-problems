# Uses python3
import sys

def binary_search(a, x, low, high):
    # write your code here
    if(high<low):
        return -1
    mid = int(low + ((high-low)/2))
    if(a[mid]==x):
        return mid
    elif(x<a[mid]):
        return binary_search(a,x,low,mid-1)
    elif(x>a[mid]):
        return binary_search(a,x,mid+1,high)

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    sorte = [int(x) for x  in input().split()]
    key_list = [int(x) for x in input().split()]
    n = sorte[0]
    m = key_list[0]
    a = sorte[1:]
    for x in key_list[1:]:
        low = 0
        high = n-1

        # replace with the call to binary_search when implemented
        print(binary_search(a, x, low, high), end = ' ')
