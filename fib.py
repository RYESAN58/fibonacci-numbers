


# SLOWWWW
def fibRecurs(n):
    if(n <= 1):
        return n
    else:
        return fibRecurs(n-1) + fibRecurs(n-2)

print(fibRecurs(6))

#Fast!!!
def fibLoop(n):
    x = []
    for i in range(n+1):
        if i > 1:
            x.append(x[i-1] + x[i-2])
        elif i == 1:
            x.append(1)
        else:
            x.append(0)
    return x[n]


print(fibLoop(400))