
my_file = open("Day1input1.txt")
my_input = my_file.read()
numbers = [int(x) for x in my_input.split()]
increase_count = 0

for i in range(len(numbers)-3):
    firstThree = numbers[i]
    nextThree = numbers[i+3]
    if firstThree < nextThree:
        increase_count += 1

print(increase_count)