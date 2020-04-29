import numpy as np

def edit_distance(A,B):
    D = np.zeros((len(A),len(B)))

    for i in range(len(A)):
        D[i,0] = i

    for j in range(len(B)):
        D[0,j] = j

    for i in range(1,len(A)):
        for j in range(1,len(B)):
            insertion = D[i,j-1] + 1
            deletion = D[i-1,j] +1
            match = D[i-1,j-1]
            mismatch = D[i-1,j-1] +1

            if(A[i] == B[j]):
                D[i,j] = min(insertion,deletion,match)
            else:
                D[i,j] = min(insertion,deletion,mismatch)
    return D

def outputAlignmnet(D,i,j,new_A,new_B,A,B):
    if i==0 and j==0:
        return new_A,new_B
    if (i>0 and D[i,j] == D[i-1,j] + 1):
        outputAlignmnet(D,i-1,j,new_A,new_B,A,B)
        new_A.append(A[i])
        new_B.append('-')

    elif (j>0 and D[i,j] == D[i,j-1] +1):
        outputAlignmnet(D,i,j-1,new_A,new_B,A,B)
        new_A.append('-')
        new_B.append(B[j])

    else:

        outputAlignmnet(D,i-1,j-1,new_A,new_B,A,B)
        new_A.append(A[i])
        new_B.append(B[j])
        
    return new_A,new_B

def LCS(A,B,x,y):
    if(x==-1 or y==-1):
        return 0
    elif(A[x]==B[y]):
        return 1+(LCS(A,B,x-1,y-1))
    else:
        return max(LCS(A,B,x-1,y),LCS(A,B,x,y-1))


if __name__=="__main__":
    n =int(input())
    A = [0]+[int(x) for x in input().split()]
    m = int(input())
    B = [0]+[int(x) for x in input().split()]

    print(LCS(A,B,n-1,m-1))
    # truthval = 0
    # for i in range(1,n+1):
    #     if(A[i] in B[1:]):
    #         truthval=1
    #         break

    # if(truthval):
    #     D = edit_distance(A,B)
    #     new_A , new_B = outputAlignmnet(D,len(A)-1,len(B)-1,[],[],A,B)
    #     new_A.append(0)
    #     new_B.append(1)
    #     seq = []
    #     for i in range(len(new_A)):
    #         if(new_A[i]==new_B[i]):
    #             seq.append(new_A[i])
    #     print(len(seq))
    #     print(new_A)
    #     print(new_B)
    # else:
    #     print(0)