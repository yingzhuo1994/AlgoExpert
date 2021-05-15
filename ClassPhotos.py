def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	if redShirtHeights[0] > blueShirtHeights[0]:
		front = blueShirtHeights
		back = redShirtHeights
	else:
		front = redShirtHeights
		back = blueShirtHeights
	for i in range(len(front)):
		if back[i] <= front[i]:
			return False
	return True
