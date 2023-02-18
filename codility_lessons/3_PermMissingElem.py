# Solution to Codility Lesson problem
# https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

def solution(A):

    total_n = len(A)+1
    expected_value = total_n * (total_n+1) // 2
    add_list = sum(A)
    return expected_value - add_list

print(solution([2,3]))
