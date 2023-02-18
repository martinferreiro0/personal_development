# Solution to Codility Lesson problem
# https://app.codility.com/programmers/lessons/5-prefix_sums/count_div/

def solution(A, B, K):
    # 11/2  = 5
    div_B = B // K
    # (6 - 1) / 2  = 2
    div_A_1 = (A-1) // K 
    print(div_B)
    print(div_A_1)
    return div_B - div_A_1

print(solution(1, 4, 2))