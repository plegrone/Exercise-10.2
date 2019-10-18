t = [1, 2, 3, 4, 5, 6]

def cumsum(t):
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res

print(cumsum(t))

    






