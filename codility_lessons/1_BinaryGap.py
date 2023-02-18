# Solution to Codility Lesson problem
# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def solution(N):
    # Implement your solution here
    initial_one = False
    binary_gap = 0
    n_zero = 0

    for bit in format(N, 'b'):
        if not initial_one and bit == '1':
            initial_one = True
        elif initial_one:
            if bit == '0':
                n_zero += 1
            else:
                if n_zero > binary_gap:
                    binary_gap = n_zero
                n_zero = 0
        print("{}-{}-{}".format(bit, n_zero, binary_gap))
    return binary_gap

print(solution(1376796946))