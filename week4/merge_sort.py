def merge_array(left,right):

    val = []
    i = 0
    j = 0
    len_l = len(left)
    len_r = len(right)
    while(i<len_l and j<len_r):
        if(left[i]<=right[j]):
            val.append(left[i])
            i+=1
        else:
            val.append(right[j])
            j+=1

    while(i<len_l):
        val.append(left[i])
        i+=1

    while(j<len_r):
        val.append(right[j])
        j+=1

    return val

def merge_sort_array(elems,low,high):

    if(high<=low):
        return [elems[low]]
    mid = int(low + (high-low)/2)
    left = merge_sort_array(elems,low,mid)
    right = merge_sort_array(elems,mid + 1,high)
    val = merge_array(left,right)
    return val

if __name__=="__main__":
    n = int(input())
    elems = [int(x) for x in input().split()]
    val = merge_sort_array(elems,0,n-1)
    print(' '.join([str(x) for x in val]))

