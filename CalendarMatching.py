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

# 2nd solution
# O(c1 + c2) time | O(c1 + c2) space
# where c1 and c2 are the respective numbers of meetings in calendar1 and calendar2 
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
    updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)
    mergedCalendar = mergeCalendars(updatedCalendar1, updatedCalendar2)
    flattenedCalendar = flattenCalendar(mergedCalendar)
    return getMatchingAvailabilities(flattenedCalendar, meetingDuration)

def updateCalendar(calendar, dailyBounds):
    updatedCalendar = calendar[:]
    updatedCalendar.insert(0, ["0:00", dailyBounds[0]])
    updatedCalendar.append([dailyBounds[1], "23:59"])
    return list(map( lambda m: [timeToMinutes(m[0]), timeToMinutes(m[1])], updatedCalendar))

def mergeCalendars(calendar1, calendar2):
    merged = []
    i, j = 0, 0
    while i < len(calendar1) and j < len(calendar2):
        meeting1, meeting2 = calendar1[i], calendar2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1
    
    while i < len(calendar1):
        merged.append(calendar1[i])
        i += 1
    while j < len(calendar2):
        merged.append(calendar2[j])
        j += 1
    return merged

def flattenCalendar(calendar):
    flattened = [calendar[0][:]]
    for i in range(1, len(calendar)):
        currentMeeting = calendar[i]
        previousMeeting = flattened[-1]
        currentStart, currentEnd = currentMeeting
        previousStart, previousEnd = previousMeeting
        if previousEnd >= currentStart:
            newPreviousMeeting = [previousStart, max(previousEnd, currentEnd)]
            flattened[-1] = newPreviousMeeting
        else:
            flattened.append(currentMeeting[:])
    return flattened

def getMatchingAvailabilities(calendar, meetingDuration):
    matchingAvailabilities = []
    for i in range(1, len(calendar)):
        start = calendar[i - 1][1]
        end = calendar[i][0]
        availabilityDuration = end - start
        if availabilityDuration >= meetingDuration:
            matchingAvailabilities.append([start, end])
    return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])], matchingAvailabilities))

def timeToMinutes(time):
    hours, minutes = list(map(int, time.split(":")))
    return hours * 60 + minutes

def minutesToTime(minutes):
    hours = minutes // 60
    mins = minutes % 60
    hoursString = str(hours)
    minutesString = "0" + str(mins) if mins < 10 else str(mins)
    return hoursString + ":" + minutesString