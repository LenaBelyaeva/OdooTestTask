def bad_way_N(n,k):
    if n == 1:
        if k >= 0 and k <= 9:
            return 1
        else:
            return 0
    summ = 0
    for l in range(10):
        summ += N(n-1,k-l)
    return summ

def N(n,k):
    first = [1]*10 + [0]*(k-9)
    last = [0]*(k+1)

    for i in range(n-1):
        index = k
        start = index - 9
        if (start < 0): start = 0
        last[index] = sum(first[start:index+1])
        while (index > 0):
            index -= 1
            start = index - 9
            if (start < 0): start = 0
            last[index] = sum(first[start:index+1])
        first = last

    return first[k]
    

def happy_tickets(length, summ):
    if (summ%2):
        return 0
    return N(length, int(summ/2))**2

i = input("input N and sum: ").split()
n = int(i[0])
k = int(i[1])
print(happy_tickets(n, k))
