def combsort(a):
    shrinkFactor = 1.3
    sorted = False
    gap = len(a)
    while not sorted:
        gap = int(gap/shrinkFactor)
        if gap <= 1:
            sorted = True
            gap = 1
        for i in range(len(a)-gap):
            j = gap+i
            if a[j] < a[i]:
                a[i],a[j] = a[j], a[i]
                sorted = False