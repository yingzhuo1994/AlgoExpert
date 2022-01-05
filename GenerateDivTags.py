# 1st solution
def generateDivTags(numberOfTags):
    openingTags = "<div>"
    closingTags = "</div>"
    result = []

    def dfs(result, left, right, path):
        if left == right and right == 0:
            result.append(path)
            return 
        
        if left > right or left < 0:
            return

        dfs(result, left - 1, right, path + openingTags)
        dfs(result, left, right - 1, path + closingTags)
        
    dfs(result, numberOfTags, numberOfTags, "")
    return result

# 2nd solution
# O((2n)! / (n!((n+1)!))) time | O((2n)! / (n!((n+1)!))) space
# where n is the input number
def generateDivTags(numberOfTags):
    matchedDivTags = []
    generateDivTagsFromPrefix(numberOfTags, numberOfTags, "", matchedDivTags)
    return matchedDivTags

def generateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded, prefix, result):
    if openingTagsNeeded > 0:
        newPrefix = prefix + "<div>"
        generateDivTagsFromPrefix(openingTagsNeeded - 1, closingTagsNeeded, newPrefix, result)
    
    if openingTagsNeeded < closingTagsNeeded:
        newPrefix = prefix + "</div>"
        generateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded - 1, newPrefix, result)
    
    if closingTagsNeeded == 0:
        result.append(prefix)