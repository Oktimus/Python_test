def variant1(s):
    text = s[::-1]
    return text

def variant2(s):
    s1=list(s)
    s1.reverse()
    text=''.join(s1)
    return text

def variant3(s):
    l=[]
    for i in s:
        l.insert(0,i)
    text=''.join(l)
    return text


def variant4(s):
    l=list(s)
    text=''.join(reversed(l))

    return text



s = "ambulance"
print variant1(s)
print variant2(s)
print variant3(s)
print variant4(s)


