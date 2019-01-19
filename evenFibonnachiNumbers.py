def evenFibonnachiNumbers(max):
    fibonnachi = [1,2]
    for i in range(max):
        if i>1:
            fibonnachi.append((fibonnachi[i-1])+(fibonnachi[i-2]))
    count = 0
    for i in fibonnachi:
        if i%2 == 0:
            count = count+i
    return(count)
