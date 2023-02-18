# Solution to Codility Lesson problem
# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/


def solution(A, K):
    final_list = A

    if len(A) == 0 or len(A) == 1:
        return A

    for i in range(K):
        initial_value = final_list[0]
        for pos in range(len(A)-1):
            final_list[0-pos] = final_list[-1-pos]
        final_list[1] = initial_value

    return final_list