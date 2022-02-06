
newLine = ''
with open('valid1.txt', 'r') as f:
    
    for i, line in enumerate(f):
        line = line.strip()
        for i in range(len(line)):
            if line[i] == ',': 
               newLine+=',\n'
            else: 
                newLine += line[i]
    f.close()
with open('valid.txt', 'w') as f:
    f.write(newLine)
    f.close()