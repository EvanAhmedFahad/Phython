names=['fahad','sipa','fahmida','khan']
print(names[-1])
numbers = [3,4,5,7,1]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number

print(max)
#two dimenstion list
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[0][0]=40
print(matrix[0][0])
for row in matrix:
    for item in row:
        print(item)
print()

n = input("enter a text of number : ")
list=n.split()
sum=0

for num in list:
    sum=sum+int (num)
print(sum)