# Solution to Codility Lesson problem
# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/

def solution(A):
    # Implement your solution here
    A.sort()
    max_triplet_pos = A[-1] * A[-2] * A[-3]
    max_triplet_neg = A[-1] * A[0] * A[1]
    print(A)
    if max_triplet_pos > max_triplet_neg:
        return max_triplet_pos
    else:
        return max_triplet_neg

print(solution([1,6,3]))