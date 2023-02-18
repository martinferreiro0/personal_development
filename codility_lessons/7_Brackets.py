# Solution to Codility Lesson problem
# https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/

def solution(S):
    # Implement your solution here
    values = {"{": "}", "(":")", "[":"]"}

    stack = []

    for el in S: 
        if el in values.keys():
            stack.append(el)
        else:
            if not stack:
                return 0
            else:
                if values[stack[-1]] == el:
                    stack.pop()
                else:
                    return 0
    
    if not stack:
        return 1
    else: 
        return 0

print(solution("{}{}{}{}"))