import pandas as pd

# ------------------------ DAY 1 ----------------------
#convert source data into separate lists
data = pd.read_csv("input.txt", sep=" ",header=None)
list1 = data[0].to_list()
list2 = data[3].to_list()

# #sort lists
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

# new list with difference between sorted list1 and 2 and make sure the number is postive
difference_list = []
for i in range(len(sorted_list1)):
    difference = sorted_list2[i] - sorted_list1[i]
    difference_list.append(abs(difference))

# get sum of all numbers
sumlist = sum(difference_list)

# -------------------- DAY 2 --------------------------

# new occurences list
occurences = []

# loop over list one and count occurences, multiply the number with the occurences and save it in the new list
for i in range(len(list1)):
    occurencemultiplied = list1[i] * list2.count(list1[i])
    occurences.append(occurencemultiplied)

# calculate the similarity score
similarityscore = sum(occurences)
print(similarityscore)
