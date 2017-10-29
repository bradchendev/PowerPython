import sys
# data.txt is encoded in utf-8
# http://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html

print('print with for in')
fileWithPath = 'C:\Temp\data.txt';
# 最好的讀檔方式是不要去Read它
for line in open(fileWithPath, 'r', encoding="utf-8"):
    print(line, end = '')


print('print content')
file = open(fileWithPath, 'r', encoding="utf-8")
content = file.read()
file.close()
print(content)

file3 = open(fileWithPath, 'w', encoding="utf-8")
file3.write('第一行\n')
file3.write('第二行\n')
file3.close()

print('')

print('print with while')
file = open(fileWithPath, 'r', encoding="utf-8")
while True:
    line = file.readline()
    if not line: break
    print(line, end = '')
file.close()


# 可以使用Readlines一次讀取所有內容，但是回傳的是list

import sys
file = open(fileWithPath, 'r', encoding="utf-8")
for line in file.readlines():
    print(line, end = '')
file.close()
