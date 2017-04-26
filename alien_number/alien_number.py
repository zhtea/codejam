text = open("A-large-practice.in","r")
output = open("output","w")
maxium = int(text.readline())
count_line = 1
for raw in text:
    line = raw[:-1]
    numbers = {x:-1 for x in set(line)}
#    print(raw)
#    print(set(line))
    count = 0
    base =max(len(set(line)),2)
#    print(base)
    y = 0
    for s in line:
        if numbers[s] == -1:
            if count ==0:
                numbers[s]= 1
            elif count == 1:
                numbers[s] = 0
            else:
                numbers[s] = count
            count = count + 1
        y = y*base + numbers[s]
#    print(numbers)
    if base ==1:
        y =2
    output.write("Case #{}: {}\n".format(count_line,y))
    count_line = count_line + 1
text.close()
output.close()
    
