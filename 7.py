import re

text = '@55la@22mp11ac1234kma3np88oria54'
pattern = r'\d+'

print(re.findall(pattern, text))
