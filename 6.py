import re

text = ['salam', 'pride', 'jafar', 'paria', 'kazem', 'packman', 'poria']
pattern = r'^p'

counter = 0
for item in text:
    if counter == 2:
        break
    if re.search(pattern, item):
        print(item)
        counter += 1
