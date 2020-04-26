def merge_array(left,right):
    i = 0
    j = 0
    num_com = 0
    val = []
    left_len = len(left)
    right_len = len(right)
    while(i<left_len and j<right_len):

        if(left[i]>right[j]):
            num_com+= (left_len-i)

        if(left[i]<=right[j]):
            val.append(left[i])
            i+=1
        else:
            val.append(right[j])
            j+=1


    while(i<left_len):
        val.append(left[i])
        i+=1
    
    while(j<right_len):
        val.append(right[j])
        j+=1



    return val,num_com


def merge_sort(elems,l,r):
    if(r==l):
        return [elems[l]],0

    mid = int(l + (r-l)/2)
    left, num_coml = merge_sort(elems,l,mid)
    right, num_comr = merge_sort(elems,mid+1,r)
    val, num_com = merge_array(left,right)
    return val, num_com+num_coml+num_comr


if __name__=="__main__":
    n = int(input())
    elems = [int(x) for x in input().split()]
    val, num_com = merge_sort(elems,0,n-1)
    print(num_com)