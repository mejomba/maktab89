import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = r'exercises'

for match in re.finditer(pattern, text):
    print(f'{match.group()} in {match.span()}')
