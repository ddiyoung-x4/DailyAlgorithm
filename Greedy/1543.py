doc = input()
search = input()

doc = doc.replace(search, '.')

print(doc.count('.'))