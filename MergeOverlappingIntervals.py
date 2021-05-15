def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort()
    lst = []
    for i in range(len(intervals)):
        if not lst:
            lst.append(intervals[i])
        curInterval = intervals[i]
        lastInterval = lst[-1]
        if curInterval[0] > lastInterval[1]:
            lst.append(curInterval)
        elif curInterval[1] > lastInterval[1]:
            lastInterval[1] = curInterval[1]
    return lst
