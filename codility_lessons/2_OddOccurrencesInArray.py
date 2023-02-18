# Solution to Codility Lesson problem
# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

def solution(A):
    elements_dict = {}
    
    if len(A) == 1:
        return A[0] 

    for el in A:
        if el not in elements_dict.keys():
            elements_dict[el] = 1
        else:
            elements_dict[el] += 1
    
    for el in elements_dict.keys():
        if (elements_dict[el] % 2) != 0:
            return el
    
    return -1


print(solution([2,2,3,3,9,3,3,4,5,4,5]))