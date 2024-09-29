from types import NoneType # imported automatically, none of my fault.

# DICTIONARIES
print('WORKING WITH DICTIONARIES')

# Create dict {name: height in cm}
# First, create an empty dict:
my_dict = {}

# Create a list of names [nlist] and a list of their corresponding heights [hlist] in cm:
nlist = ['Oliver', 'Harry', 'Thomas', 'Arthur', 'Emma', 'Harper', 'Abigail']
hlist = [185, 191, 176, 181, 156, 174, 182]

# Fill the dictionaly with pairs [name: height] ("records"):
for i in range(len(nlist)):
    my_dict.update({nlist[i]: hlist[i]})
print(my_dict)

# Get somebody's hight by specifying their index in [nlist]:
idx = 2 # change this to get the corresponding person's height
print(nlist[idx], ": ", my_dict.get(nlist[idx]), ' cm', sep = '')

# Get somebody's height who IS or IS NOT not in [my_disc]:
anyname = 'Eva' # some name in [my_dict] or not
if type(my_dict.get(anyname)) == NoneType:
    print('Sorry,', anyname, 'is not on our roll')
else:
    print(anyname, ": ", my_dict.get(anyname), ' cm', sep='')

# Get Willam's height. William is not in [my_dict]. First, add him the easy way:
my_dict['William'] = 181
# Now we can his his height:
print('William', ": ", my_dict.get('William'), ' cm', sep = '')

# Add two more "records" to [my_dict]:
my_dict.update({'Benjamin': 179, 'Olivia': 174})
print(my_dict)

# Remove somebody from [my_dict] and get their height at the same time:
delname = 'Arthur' # change to remove various "records" from [my_dict];
                   # allow for specifying someone who IS NOT in [my_dic]
if type(my_dict.get(delname)) == NoneType:
    print('Sorry,', delname, 'is not in our roll')
else:
    print(delname, my_dict.pop(delname), 'cm.', delname, 'has now been removed from our roll.')
print(my_dict)

# SETS
print(chr(10), 'WORKING WITH SETS', sep='') # Hm, chr(13) won't work... why?

# Create a set, output it to console:
my_set = {1, 2, 3, 1, 2, 3, 'one', 'two', 'three', 'one', 'two', 'three'}
print('Original set:', my_set)

# Add 2 items to the set, output the set to console:
my_set.add(3.1415)
my_set.add((10, 20, 30))
print('Set with 2 items added:', my_set)

# Remove 1 item from the set, output the set to console
my_set.discard('three')
print('... and with 1 item removed:', my_set)
#print(chr(13))