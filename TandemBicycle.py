def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    totalSpeed = 0
    if fastest:
        for i in range(len(redShirtSpeeds)):
            totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[-i-1])
    else:
        for i in range(len(redShirtSpeeds)):
            totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return totalSpeed
