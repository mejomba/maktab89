import re

text = 'ali Ali Mamad ehsan Jafar'
pattern = r'\b[ae]\w*\b'

print(re.findall(pattern, text, re.I))
