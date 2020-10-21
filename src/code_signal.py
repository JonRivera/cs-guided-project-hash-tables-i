# given non-empty [] of integers

# You are given a non-empty array of integers.
#
# Every element appears in the array three times except for one, which appears exactly once.
#
# Write a function that can find and return the element that appears exactly once.
#
# Example 1:
#
# Input: [1,1,2,1]
# Output: 2
# Example 2:
#
# Input: [1,2,1,2,1,2,80]
# Output: 80

# want
# element that appears once in array
# plan
# construct a counter
# constuct a {}
# iterate over nums
# add num in nums to dict, set equal to 1,
# if num in dict then dict[num]+=1
# return element with count of 1
def csFindTheSingleNumber(nums):
    counter = {}
    for num in nums:
        if num not in counter:
            counter[num] = 1
        else:
            counter[num] += 1
    for num in counter:
        if counter[num] == 1:
            return num
# TEST
# csAverageOfTopFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])
# given text
# want
# form as many "lambda" instances from text
# plan
# have some sort of while loop
# remove the letters in text  that are in list1

def csAverageOfTopFive(scores):
    averages = {}
    for student, score in scores:
        if student in averages:
            averages[student].append(score)
            print(averages)
        else:
            averages[student] = [score]
    final = []
    for student in averages.keys():
        print(student)
        averages[student].sort(reverse=True)
        top5 = averages[student][:5]
        final.append([student, sum(top5) // len(top5)])
    return final

"""SOL#6, long run time"""

def csMaxNumberOfLambdas(text):
    instance = list("lambda")
    max_length = len(instance)
    count = 0
    list1 = list(text)
    while instance it not None:
        for char in list1:
            if char in instance:
                print(char)
                instance.remove(char)
                list1.remove(char)
                print(instance)
            if len(instance) == 0:
                count += 1
                print(count)
                instance = list("lambda")
    return count

"""OTHER SOL"""
def csMaxNumberOfLambdas(text):
    instance = {char:text.count(char) for char in text}
    check = {char for char in "lambda"}
    count = 0
    list1 = list(text)
    list2 = []
    while instance["l"] >=1 and instance["a"] >=2 and instance["m"] >=1 and instance["b"] >=1 and instance["d"] >=1 :
        instance["l"]-= 1
        instance['a']-=1
        instance['m']-=1
        instance['b']-=1
        instance['d']-=1
        instance['a']-=1
        count += 1

    return count
