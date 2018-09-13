

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        print('max_ending_here: '+str(max_ending_here))
        print('max_so_far: '+str(max_so_far))
    return max_so_far

A=[-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_subarray(A))