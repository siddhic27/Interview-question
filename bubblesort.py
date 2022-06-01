A = [64, 34, 25, 12, 22, 11, 90]

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if A[j] > A[j + 1] :
                A[j], A[j + 1] = A[j + 1], A[j]

bubbleSort(A)

print ("Sorted array is:")
for i in range(len(A)):
    print ("% d" % A[i],end=" ")
