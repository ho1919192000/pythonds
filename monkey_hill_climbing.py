
# Self Check

# Here’s a self check that really covers everything so far. 
# You may have heard of the infinite monkey theorem? The theorem 
# states that a monkey hitting keys at random on a typewriter keyboard 
# for an infinite amount of time will almost surely type a given text,
#  such as the complete works of William Shakespeare.
#   Well, suppose we replace a monkey with a Python function. 
#   How long do you think it would take for a Python function to generate just one sentence of Shakespeare?
#  The sentence we’ll shoot for is: “methinks it is like a weasel”

# You’re not going to want to run this one in the browser, so fire up your favorite Python IDE.
# The way we’ll simulate this is to write a function that generates a string that is 27 characters 
# long by choosing random letters from the 26 letters in the alphabet plus the space. 
# We’ll write another function that will score each generated string by comparing the randomly generated string to the goal.

# A third function will repeatedly call generate and score, then if 100% of 
# the letters are correct we are done. If the letters are not correct then 
# we will generate a whole new string.To make it easier to follow your program’s progress 
# this third function should print out the best string generated so far and its score every 1000 tries.

# Self Check Challenge

# See if you can improve upon the program in the self check by keeping letters 
# that are correct and only modifying one character in the best string so far. 
# This is a type of algorithm in the class of ‘hill climbing’ algorithms, 
# that is we only keep the result if it is better than the previous one.

import string
import random

# # Hill Climbing Version
def generateOne(strlen):
    alphabet = string.ascii_lowercase[:26] + " "
    res = []
    for i in range(strlen):
        res.append(alphabet[random.randrange(27)])
    return res

def score(goallist, testlist):
    numSame = 0
    for i in range(len(goallist)):
        if(goallist[i] == testlist[i]):
            numSame += 1
    return numSame / len(goallist)

def updatelist(latestlist, goallist, newlist):
    for i in range(len(goallist)):
        if goallist[i] == newlist[i]:
            latestlist[i] = newlist[i]
    return latestlist

def main():
    goallist = [i for i in "methinks it is like a weasel"]
    latestlist = ["" for i in range(len(goallist))]
    newlist = generateOne(len(goallist))
    latestscore = score(goallist, newlist)
    latestlist = updatelist(latestlist, goallist, newlist)
    count = 1

    while latestscore < 1:
        newlist = generateOne(len(goallist))
        latestlist = updatelist(latestlist, goallist, newlist)
        latestscore = score(goallist, latestlist)
        count += 1

        if count % 10:
            print(latestscore, "".join(latestlist))

    print(count)


main()


# # First Version
# words_list = string.ascii_lowercase[:26] + " "
# targetSentence = "methinks it is like a weasel"
# # num_words = 28
# score = 0
# best_string = ""
# best_record = dict()
#
#
#
# def monkey():
#     monkey_guess = ""
#     global words_list
#     for i in range(28):
#         monkey_guess += words_list[random.randint(0, 26)]
#     global score
#     return monkey_guess
#
# def compare(monkey_guess):
#     compare_score = 0
#     global score
#     global best_string
#     global best_record
#     for i in range(len(targetSentence)):
#         if monkey_guess[i] is targetSentence[i]:
#             compare_score += 1
#
#
#
#     if compare_score > score:
#         score = compare_score
#         best_string = monkey_guess
#
#     if score is 28: return True
#     return False
#
# def monkey_type():
#     done = False
#     count = 0
#     global score
#     global best_string
#     while not done:
#         done = compare(monkey())
#         if count % 1000 == 0:
#             print(score)
#             print(best_string)
#
#     print(score)
#     print(best_string)
#
# monkey_type()