import string

strings = []
for e in string.ascii_letters:
    strings.append(e)

def encode(n):
    if type(n) == str:
        n2 = n.split(" ")
        #print(n2)    
    elif type(n) == list:
        n2 = n
    else:
        return "error dataType"
    out = []
    for i in range(len(n2)):
        out1 = []
        for j in range(len(n2[i])):
            #TYPE 1
            if n2[i][j] in strings:
                k = (strings.index(n2[i][j]) + 3)%52
                out1.append(strings[k])
            else:
                out1.append(n2[i][j])
            out2 = "".join(out1)
        out.append(out2)
            #END TYPE 1
    return out
    
def decode(n):
    if type(n) == str:
        n2 = n.split(" ")
        #print(n2)
    elif type(n) == list:
        n2 = n
    else:
        return "error dataType"
    out = []
    for i in range(len(n2)):
        out1 = []
        for j in range(len(n2[i])):
            #TYPE 1
            if n2[i][j] in strings:
                k = (strings.index(n2[i][j]) - 3)%52
                out1.append(strings[k])
            else:
                out1.append(n2[i][j])
            out2 = "".join(out1)
        out.append(out2)
            #END TYPE 1
    out3 = " ".join(out)
    return out3
        
#TESTING SITE
k = "Blame Canada!!!!1!!"

print(k)
k2 = encode(k)
print(k2)
print(decode(k2))
