def all_variants(text):
    k = 0
    for i in range(len(text)):
        for j in range(len(text)):
            if len(text[j:i+j+1]) >= k:
                yield (text[j:i+j+1])
            k = len(text[j:i+j+1])

########################################
a = all_variants('abcd')
for i in a:
    print(i)