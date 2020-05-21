# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    for i in range(0,len(q)):
        if i<q[i]-3:
            print("Too chaotic")
            return
        for j in range(i+1,len(q)):
            if q[i]>q[j]:
                count = count+1
    print(count)

    return

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)