def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    # print("i",i)
    for j in range(i):
        # print("j",j)
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n):
    if len(perm) == n:
        print(perm)
        exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)
            # print("1   ",perm)
            if can_be_extended_to_solution(perm):
                extend(perm, n)

            # print("2   ", perm)
            perm.pop()
            # print("3   ",perm)

extend(perm = [], n = 4)