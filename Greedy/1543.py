doc = input()
search = input()

j = 0
doc = doc.replace(search, '.')
print(doc)

print(doc.count('.'))