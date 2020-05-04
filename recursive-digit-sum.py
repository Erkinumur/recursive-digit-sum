def superDigit(n, k):
    if k == 1 and int(n) < 10:
        return int(n)
    else:
        sum_all = sum(int(i) for i in n) * k
        return superDigit(str(sum_all), 1)