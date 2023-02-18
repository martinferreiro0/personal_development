# Solution to Codility Lesson problem
# https://app.codility.com/programmers/lessons/6-sorting/triangle/

def solution(A):

    A.sort()
    
    if len(A) < 3:
        return 0
    
    for pos in range(0, (len(A)-2)):
        if A[pos] + A[pos+1] > A[pos+2]:
            return 1
    return 0