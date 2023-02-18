# Solution to Codility Lesson problem
# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

def solution(X, Y, D):
    dist = Y - X
    n_jump = dist // D
    if (dist % D) != 0:
        n_jump += 1

    return n_jump

print(solution(2,20,3))