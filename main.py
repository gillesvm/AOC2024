import pandas as pd

#convert source data into separate lists
data = pd.read_csv("input.txt", sep=" ",header=None)
list1 = data[0].to_list()
list2 = data[3].to_list()
print(type(list1))


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
print(sumlist)

