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

if __name__=="__main__":
    A = str(0)+input()
    B = str(0)+input()
    D = edit_distance(A,B)

    new_A , new_B = outputAlignmnet(D,len(A)-1,len(B)-1,[],[],A,B)
    print(D[len(A)-1,len(B)-1])
    print(new_A)
    print(new_B)
    # new_A.append(0)
    # new_B.append(1)
    # seq = []
    # main_seq = []
    # for i in range(len(new_A)):
    #     if(new_A[i]==new_B[i]):
    #         seq.append(new_A[i])
    #     else:
    #         main_seq.append(seq)
    #         seq = []
    # print(''.join(max(main_seq,key=lambda x:len(x))))
