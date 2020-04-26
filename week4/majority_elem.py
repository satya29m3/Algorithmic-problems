def majority_elem(n,elem):
    freq = dict()
    for i in range(n):
        if(elem[i] in freq.keys()):
            freq[elem[i]] += 1
        else:freq[elem[i]] = 1
    for val,f in freq.items():
        if(f>n/2):
            return 1
    return 0

if __name__=="__main__":
    n = int(input())
    elem = [int(x) for x in input().split()]
    print(majority_elem(n,elem))