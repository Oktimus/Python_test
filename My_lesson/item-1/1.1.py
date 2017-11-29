def variant1(s):
    text = s[::-1]
    return text

def variant3(s):
    s1=list(s)
    s1.reverse()
    text=''.join(s1)
    return text

def variant4():

    return text

s = "qwertyuiop"
print variant1(s)


print variant3(s)

print variant4(s)



