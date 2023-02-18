# Solution to Codility Lesson problem
# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

def solution(A):
    permutation = [False] * len(A)
    for el in A: 
        if el <= len(A):
            permutation[el-1] = True
    print(permutation)
    if all(permutation):
        return 1
    else:
        return 0

print(solution([2,3,4,1,1,2]))

def solution(A):
    if len(A) == max(A)
    permutation = [False] * len(A)
    for el in A: 
        if el <= len(A):
            permutation[el-1] = True
    print(permutation)
    if all(permutation):
        return 1
    else:
        return 0
