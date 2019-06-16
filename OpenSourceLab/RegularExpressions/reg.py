import re
text="viral.tagdiwala@gmail.com https://www.milindshh.in"
#For email
pattern = re.compile(r"[a-z]+(\.)?(\w)*@(\w)*(\.)(\w)*(\.\w)?")
#For URLS
pattern2 = re.compile(r"https?://(www\.)?(\w)+\.(\w|\.)+")
matches = pattern.finditer(text)
for i in matches:
	print(i)
match2 = pattern2.finditer(text)
for i in match2:
	print(i)

'''
\d Digit
\w Word Character which includes 0-9 and _
\s Whie space, tab and newline
\b word boundry
^ Beginning of a string
$ End of the string
[] Matches all characters in the bracket
[M(r/s)] Matches Mr or Ms
() Group

* 0 or more occurances
? 0 or 1
+ 1 or more
{n} n occurances
{m,n} minimum m and maximum n
'''