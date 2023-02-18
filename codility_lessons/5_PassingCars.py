# Solution to Codility Lesson problem
# https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

def solution(A):
    mult = 0
    pairs_cars = 0

    for el in A:
        if el == 0:
            mult += 1
        else:
            pairs_cars += mult
    return pairs_cars

print(solution([1,0]))