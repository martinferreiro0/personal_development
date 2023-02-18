# Solution to Codility Lesson problem
# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

def solution(X, A):
    leaf_pos = [False] * (X + 1)
    leaf_pos[0] = True 
    for time, el in enumerate(A):
        if el > X:
            continue
        if not leaf_pos[el]:
            leaf_pos[el] = True
            if all(leaf_pos):
                return time
    return -1

print(solution(5, [1,1,1,1,1,2,2,2,2,3,3,4,4,4,4,4,4,4,9]))