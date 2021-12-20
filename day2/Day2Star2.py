
my_file = open("Day2input1.txt")
my_input = my_file.read()
direction_lines = my_input.splitlines()

print(direction_lines)

horizontal_position = 0
vertical_position = 0
aim = 0

for line in direction_lines:
    direction,num = line.split(' ')
    if (direction == "forward"):
        horizontal_position += int(num)
        vertical_position += aim*int(num)
    if (direction == "up"):
        aim -= int(num)
    if (direction == "down"):
        aim += int(num)    

print(horizontal_position)
print(vertical_position)
print(horizontal_position * vertical_position)