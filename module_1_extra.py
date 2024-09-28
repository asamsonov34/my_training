students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
avg = {} # define avg as dictionary, empty so far.

stu_list=list(students) # make a list out of the set
stu_list.sort() # sort the list alphabetically

# Now that we have sorted stu_list, the names in it are in the same order
# as in the grades list, as per the task specs.

# In the cycle below, each iteration updates the dictionary with a pair
# {student: avg_grade}
for i in range(len(students)):
    avg.update({stu_list[i]: sum(grades[i])/len(grades[i])})

# The dictionary has been compiled, and we can output it to console:
print(avg)

# Let us try to use the dictionary to make sure it is actually a dictionary,
# and not something that just looks like one in the console output. We will
# attempt to get the values by the keys with the get() method:
for i in range(len(students)):
    print(stu_list[i], avg.get(stu_list[i]))