import sys
import re
#WORD_RE = re.compile('\w+')
WORD_RE = re.compile('[A-Z]{1}[a-z]+|[a-z]+')
index = {}

#with open(sys.argv[1], encoding='utf-8') as fp:
with open(sys.argv[1]) as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            #index.setdefault(word, []).append(location) 
            index.setdefault(word, 0)
            index[word]  = index[word] + 1

# print in alphabetical order
#for word in sorted(index, key=str.upper):
# print(word, index[word])


for word in sorted(index, key=index.get, reverse=True):
 print(word, index[word])
