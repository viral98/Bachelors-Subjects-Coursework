import re
contents = ""
with open('dataset') as f:
    for line in f.readlines():
        contents += line
#for phone numbers
pattern1 = re.compile(r"(\d){3,4}(\.|\*|\-)+(\d){3,4}(\.|\*|\-)+(\d){3,4}")
#For names
pattern2 = re.compile(r"Mr(s)?(\.)?(\s)(\w)*")
pattern3 = re.compile(r"https?://(www\.)?(\w+\.)((\w+((\.)?)+)+)+")
matches = pattern1.finditer(contents)
print("For Phone Numbers")
for i in matches:
	print(i)
print("For names")
matches = pattern2.finditer(contents)
for i in matches:
	print(i)
matches = pattern3.finditer(contents)
print("For Domains")
for i in matches:
	#This works too
	#url = i.group(1) + i.group(2) 
	url = i.group(0)
	url2 = pattern3.sub(r'\2\3',url)
	print (url2)
print("For entire urls")
matches = pattern3.finditer(contents)
for i in matches:
	print(i)
