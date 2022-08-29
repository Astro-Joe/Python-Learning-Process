numbers = list(range(1,11)) #generates a range of numbers in a list.
print(numbers)
print('\n')

odd_numbers = list(range(1, 11, 2))# generates a list of numbers with a common difference.
print(odd_numbers)                 #range(start, stop, step)\
print('\n')
cubes = []
for number in range(1,11):
    cubes.append(number**3)
print(cubes)
print('\n')

digits = list(range(0,10))
print(min(digits))
print(max(digits))
print(sum(digits))
print('\n')

cube = [values**3 for values in range(1,11)] #List comprehension
print(cube)
