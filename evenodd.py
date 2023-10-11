a = [4,6,7,9,8,3]
even = []
odd = []

for i in a:
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
