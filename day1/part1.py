with open('test.txt') as file:
    depths = file.read().splitlines()

increases = 0

for i in range(1,len(depths)):
        if depths[i] > depths[i-1] :
            increases += 1

count = sum(y>x for x,y in zip(depths, depths[1:]))
print(count)

print(increases)

list_comp = len([depths[i] for i in range(1,len(depths)) if depths[i] > depths[i-1]])
print(list_comp)