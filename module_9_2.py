strs1 = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
strs2 = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
dic1 = {}

res1 = [len(x) for x in strs1 if len(x) >= 5]
res2 = [(x, y) for x in strs1 for y in strs2 if len(x) == len(y)]
res3 = [dic1.update({x: len(x)}) for x in strs1 + strs2 if not len(x) % 2]
res3 = dic1

print(res1)
print(res2)
print(res3)