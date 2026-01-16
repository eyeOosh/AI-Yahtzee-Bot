import random
# nums is the list containing dice rolls
nums = [0, 0, 0, 0, 0]
#score is the total score of the AI, made as a list to be publicly accesible
score = [0]
# tracks the scores numbers (1-11) already used
trackScore = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#prints the dice
def getNums():
    lineOne = " ---  ---  ---  ---  ---"
    a,b,c,d,e = ' ', ' ', ' ', ' ', ' '

    for i in range (0, len(nums)):
        if i == 0:
            a = (int)(nums[i])
        if i == 1:
            b = (int)(nums[i])
        if i == 2:
            c = (int)(nums[i])
        if i == 3:
            d = (int)(nums[i])
        if i == 4:
            e = (int)(nums[i])
        
        
    print(lineOne)
    print(f"| {a} || {b} || {c} || {d} || {e} |")
    print(lineOne, "\n")

#helper method to get the score
def getScore():
    return score[0]

#helper method to add to the score
def addScore(s):
    score[0] += s[0]

#helper method to set the score
def setScore(s):
    score[0] = s[0]

# if nums[i] = 0, roll i'th that die
def roll():
    n = 0
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            nums[i] = random.randint(1, 6)
            print(f"...ROLLING DICE #{i + 1}...")
            n += 1
        i += 1
    
    
    getNums()

#retain nums in the list a = [i, j, k, l, m] where i,j,k,l,m are in binary (0,1)
def retain(a):
    i = 0
    while i < len(nums):
        # if a[i] = 0, reset nums[i] to 0 as well
        if a[i] == 0:
            nums[i] = 0
        i += 1
    

#get retention numbers list a from user
def getRetention():
    a = [1, 1, 1, 1, 1]
    phrase = generateRetention(nums)
    for i in range(0, 5):
            a[i] = (int)(phrase[i])
    return a

# n is the list of dice rolls, n = nums
def generateRetention(n):
    #n = [5, 4, 3, 4, 5]
    #countsList example = [0, 0, 1, 2, 2, 0]
    countsList = [counts(1), counts(2), counts(3), counts(4), counts(5), counts(6)]
    
    retainList = [0, 0, 0, 0, 0]
    maxCount = 0

    # if all numbers are unique and not a sequence
    if max(countsList) == 1 and sequence() == 0:
            for i in range(0, len(countsList)):
                if countsList[len(countsList) - 1 -i] == 1:
                    retainList[i] = 1
                    break
            return retainList
    
    # if 2 and 3
    if threeAndTwoSame() != 0:
        retainList = [1, 1, 1, 1, 1]
        return retainList

    for i in range(0, len(countsList)):
        # if all 5 the same
        if countsList[i] == 5:
            retainList = [1, 1, 1, 1, 1]
            return retainList
        # keep only dice whose count is 4
        if countsList[i] == 4 and countsList[i] > maxCount:
            for j in range(0, len(retainList)):
                if n[j] == i+1:
                    retainList[j] = 1
            maxCount = countsList[i]
        # if its three
        if countsList[i] == 3 and countsList[i] >= maxCount:
            for j in range(0, len(retainList)):
                if n[j] == i+1:
                    retainList[j] = 1
            maxCount = countsList[i]
        # if its the first two
        if countsList[i] == 2 and countsList[i] > maxCount:
            for j in range(0, len(retainList)):
                if n[j] == i+1:
                    retainList[j] = 1
            maxCount = countsList[i]
        # if its the 2nd two
        if countsList[i] == 2 and countsList[i] == maxCount:
            for j in range(0, len(retainList)):
                if n[j] == i+1:
                    retainList[j] = 1
                elif threeAndTwoSame() > 0:
                    continue
                else:
                    retainList[j] = 0
            maxCount = countsList[i]
        #if its a 1, reroll all
        if countsList[i] == 1 and countsList[i] > maxCount:
            retainList = [0, 0, 0, 0, 0]
            maxCount = countsList[i]
        # continue
        if countsList[i] == 0:
            continue

    return retainList

# count of dice with value a
def counts(a):
    count = 0
    for i in range(0, len(nums)):
        if nums[i] == a:
            count += 1
    return count

# count(a) * a, gets the score for 1s-6s
def numsOfTheSame(a):
    return counts(a) * a

# returns roll value if roll has 2 of the same, else returns 0
def twoSame():
    # example: [0, 0, 3, 4, 3, 0] = two 3's, 4's, and 5's
    countsList = [counts(1), counts(2), counts(3), counts(4), counts(5), counts(6)]
    for i in range(0, len(countsList)):
        if countsList[i] == 2:
            return i
    return 0

# 3 of the same = add total of all dice
def threeSame():
    countsList = [counts(1), counts(2), counts(3), counts(4), counts(5), counts(6)]
    
    for i in range(0, len(countsList)):
        # if 3 of the same
        if countsList[i] == 3:
            # calc total
            total = 0
            for i in range(0, len(nums)):
                total += nums[i]
            return total
    return 0

# 4 of the same = add total of dice
def fourSame():
    # example: [0, 0, 3, 0, 3, 0] = three 3's and three 5's
    countsList = [counts(1), counts(2), counts(3), counts(4), counts(5), counts(6)]
    
    for i in range(0, len(countsList)):
        # if there are 4 of the same
        if countsList[i] == 4:
            # calculate total
            total = 0
            for i in range(0, len(nums)):
                total += nums[i]
            return total
    return 0

# 3 of a kind and 2 of a kind = 25
def threeAndTwoSame():
    three = threeSame()
    two = twoSame()

    if three > 0 and two > 0:
        return 25
    return 0

# sequence of 5 = 40
def sequence():
    countsList = [counts(1), counts(2), counts(3), counts(4), counts(5), counts(6)]

    if nums == [0, 1, 1, 1, 1, 1] or countsList == [1, 1, 1, 1, 1, 0]:
        return 40
    
    return 0

# 5 of a kind = 50
def fiveSame():
    countsList = [counts(1), counts(2), counts(3), counts(4), counts(5), counts(6)]
    for i in range(0, len(countsList)):
        if countsList[i] == 5:
            return 50
    return 0

# prints the scores on the scorecard (1-11) already used
def printAlrUsed():
    for i in range(0, len(trackScore)):
        if trackScore[i] == 1:
            print("You've Used #", (i + 1))

# prints scorecard and already used scores (1-11)
def scoreCard():
    print("\n------------------------")
    print("1. Ones: ", numsOfTheSame(1))
    print("2. Twos: ", numsOfTheSame(2))
    print("3. Threes: ", numsOfTheSame(3))
    print("4. Fours: ", numsOfTheSame(4))
    print("5. Fives: ", numsOfTheSame(5))
    print("6. Sixes: ", numsOfTheSame(6))
    print("7. Three of the same: ", threeSame())
    print("8. Four of the same: ", fourSame())
    print("9. Three of the same and two of the same: ", threeAndTwoSame())
    print("10. Sequence of 5: ", sequence())
    print("11. Five of the same: ", fiveSame())
    print("Score: ", getScore())
    print("------------------------")
    printAlrUsed()
    
# AI model to get the max score from the scorecard
def getMaxScoreIndex():
    # example = [1, 2, 3, 4, 5, 0, 0, 0, 0, 40, 0]
    scoresList = [numsOfTheSame(1), numsOfTheSame(2), numsOfTheSame(3), numsOfTheSame(4), numsOfTheSame(5), numsOfTheSame(6), threeSame(), fourSame(), threeAndTwoSame(), sequence(), fiveSame()]
    # example = [40, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0]
    sortedScores = sorted(scoresList, reverse=True)
    # example trackScores = [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1]
    i = 0
    maxScoreIndex = scoresList.index(sortedScores[i])
    while i < len(scoresList):
        # If that score number (1-11) has not been used yet
        if trackScore[maxScoreIndex] == 0:
            print("You JUST USED #", maxScoreIndex + 1)
            print("Score +=", sortedScores[i])
            trackScore[maxScoreIndex] = 1
            score[0] += sortedScores[i]
            return
        # if that score number has been used
        elif trackScore[maxScoreIndex] == 1:
            if i < len(scoresList) - 1:
                i += 1
                maxScoreIndex = scoresList.index(sortedScores[i])
            else:
                i = len(scoresList) - 1
                maxScoreIndex = 0
    return

# structures one "play" of the game
def play(sc):
    roll()
    retain(getRetention())
    roll()
    retain(getRetention())
    roll()
    scoreCard()
    getMaxScoreIndex()
    print("------------------------")
    print("Total Score: ", score[0])
    print()
    
    
# BEGIN PROGRAM
print("------WELCOME TO AI GENERATED YAHTZEE!------")
print("Created by Aayush Kumar")
print("Last updated: 1/10/26")
print("Goal: To get the maximum amount of points possible in a Yahtzee game")
print("\nLet's BEGIN!\n")
for p in range(0, 5):
    play(score)
    nums = [0, 0, 0, 0, 0]
print("END SCORE: ", score[0], "\n")
print("-> INFO: This AI prioritizes dice frequency (most common number is kept), followed by dice value (higher number is kept),")
print("   and then takes the highest possible unused score from the scorecard.")
print("-> To learn more about the AI generated dice picks and score picks, see generateRetention() and getMaxScoreIndex()")
print("\n-------Thank you for playing!-------")