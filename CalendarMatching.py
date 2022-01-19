# 1st solution
# O(n) time | O(n) space
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    possibleOne = getAvaiableTime(calendar1, dailyBounds1)
    possibleTwo = getAvaiableTime(calendar2, dailyBounds2)
    one, two = 0, 0
    ans = []
    while one < len(possibleOne) and two < len(possibleTwo):
        oneStart, oneEnd = possibleOne[one]
        if getTimeDifference(oneStart, oneEnd) < meetingDuration:
            one += 1
            continue
        twoStart, twoEnd = possibleTwo[two]
        if getTimeDifference(twoStart, twoEnd) < meetingDuration:
            two += 1
            continue
        if getTimeDifference(oneStart, twoEnd) <= 0:
            two += 1
        elif getTimeDifference(twoStart, oneEnd) <= 0:
            one += 1
        else:
            startMinutes = max(timeToMinutes(oneStart), timeToMinutes(twoStart))
            endMinutes = min(timeToMinutes(oneEnd), timeToMinutes(twoEnd))
            if endMinutes - startMinutes >= meetingDuration:
                ans.append([minutesToTime(startMinutes), minutesToTime(endMinutes)])
            one += 1
    return ans

def getAvaiableTime(calendar, dailyBounds):
    if not calendar:
        return [dailyBounds]
    ans = []
    start, end = dailyBounds
    for i in range(len(calendar)):
        startMinutes = timeToMinutes(start)
        frontMinutes = timeToMinutes(calendar[i][0])
        # backMinutes = timeToMinutes(calendar[i][1])
        if startMinutes < frontMinutes:
            ans.append([start, calendar[i][0]])
        start = calendar[i][1]
    endMinutes = timeToMinutes(end)
    backMinutes = timeToMinutes(calendar[-1][1])
    if backMinutes < endMinutes:
        ans.append([calendar[-1][1], end])
    return ans

def timeToMinutes(time):
    t = time.split(":")
    return int(t[0]) * 60 + int(t[1])

def getTimeDifference(time1, time2):
    t1, t2 = timeToMinutes(time1), timeToMinutes(time2)
    return t2 - t1

def minutesToTime(minutes):
    h = minutes // 60
    m = minutes % 60
    hour = str(h)
    minute = str(m) if m > 9 else "0" + str(m)
    return hour + ":" + minute