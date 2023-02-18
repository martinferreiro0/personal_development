import sys

def solution(A):
    
    min_diff = sys.maxsize
    total_count = sum(A)
    first_part = 0

    for el in A[:-1]:
        first_part += el
        second_part = total_count - first_part
        value = abs(first_part - second_part)
        if value < min_diff:
            min_diff = value     
    return min_diff

print(solution([1, 3, 4,8]))