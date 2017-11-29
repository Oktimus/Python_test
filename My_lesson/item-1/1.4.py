def poisk(s):
    s1=[]
    s2=[]
    end=''
    for i in range(len(s)-1):
        s1.append(s[i])

        if ord(s[i])>ord(s[i+1]):
                    s2.append(''.join(s1))
                    s1=[]
    print s2
    for i1 in s2:
        if len(i1)>len(end):
            end=i1
    return (end)



s = "sabrrtuwacaddabraabcdefghtuw"

print poisk(s)