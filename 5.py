import re
text = '2014-12-27'
pattern = r'-'

text = re.split(pattern, text)
out = "-".join(text[::-1])
print(out)

#
text = '2014-12-27'
match = re.search(r'(\d{4})-(\d{2})-(\d{2})', text)
result = re.sub(r'(\d{4})-(\d{2})-(\d{2})', f"{match.group(3)}-{match.group(2)}-{match.group(1)}", text)
print(result)
