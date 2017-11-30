#-*-coding:utf-8-*-
def glastnie(s):
    l=['a', 'e', 'i', 'o', 'u']
    entity=0
    for i in s.lower():
        if i in l:
            entity+=1
    return entity


s = "hApPyHalLOweEn!"

print u'Гластных звуков = ',glastnie(s)

