# Solution to Codility Lesson problem
# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/

def solution(A, B):
    # Implement your solution here
    downstream_fish = []
    live_fish = 0

    for pos in range(0,len(A)):
        if B[pos] == 1:
            downstream_fish.append(pos)
        else:
            if not downstream_fish:
                live_fish += 1
                continue

            eat = True

            while eat:
                if A[pos] == A[downstream_fish[-1]]:
                    live_fish += (len(downstream_fish) + 1)
                    downstream_fish = []
                    eat = False
                elif A[pos] > A[downstream_fish[-1]]:    
                    downstream_fish.pop()
                    if not downstream_fish:
                        live_fish += 1
                        eat = False
                else:
                    eat = False
        print("{}-{}".format(pos, downstream_fish))
    if downstream_fish:
        live_fish += len(downstream_fish)

    return live_fish

print(
    solution(
        A=[5,1,3,5,5],
        B=[1,1,1,1,0]
    )
)