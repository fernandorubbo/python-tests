import re

text = "The quick brown fox jumps over the lazy dog."

# Using re.search()
search_result = re.search(r"brown\sfox", text)
if search_result:
    print("Found with re.search():", search_result.group(0)) 

# Using re.match()
match_result = re.match(r".*(brown\sfox)", text)
if match_result:
    print("Found with re.match():", match_result.group(1)) 

t = "test,test2,test3"
s = re.split(r",", t)
print(s)

s = re.sub(r',', '/', t)
print(s)


text = 'All your base are belong to us.'
pattern = re.compile(r'you[r]?\s*(\S*)\s*are belong to us')
match = pattern.search(text)
print(match.group(1))


