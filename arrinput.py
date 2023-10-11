n = int(input("Enter the number of elements : "))

even = []
odd = []
number = []

for i in range(n):
    num = int(input("Enter a Number : "))
    number.append(num)
    if(num%2==0):
        even.append(num)
    else:
        odd.append(num)

print(even)
print(odd)
