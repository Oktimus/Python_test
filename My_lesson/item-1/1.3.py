#-*-coding:utf-8-*-
def findstr(s):
    count=0
    for i in range(len(s)):
        text=s[i:(len(s))]
        if text.find('wow')==0:
               count+=1
    return count

s = "wowhatamanwowowpalehchewow"

print u'Строка wow входит',findstr(s),'разa'
