import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

for match in re.finditer(pattern, text):
    print(f'find {match.group()}')

# OR
print(re.findall(pattern, text))
