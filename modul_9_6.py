def all_variants(text):
    j = 0
    while j <= len(text):
        for k in range(j):
            yield text[k:j]
        j += 1


a = all_variants('abc')
for i in a:
    print(i)
