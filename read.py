lines = []
with open('data.txt') as f:
    line = f.readline()
    while line != '':
        space = False
        line = f.readline()
        parts = line.split("|")
        for x in parts:
            if(x.isspace()):
                space = True
        if(space == False):
            lines.append(line)
for x in lines:
    print(x)        
"""
j = 0
for x in lines:
    print(j)
    print(x)
    j = j + 1 
for i in range(len(lines)-1):
    print(i)
    remove = False
    str1 = str(lines[i])
    parts = str1.split("|")
    for x in parts:
        if(x.isspace()):
            remove = True
        if(remove == True):
            lines.pop(i)
for x in lines:
    print(x)
"""