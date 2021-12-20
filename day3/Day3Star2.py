
my_file = open("Day3input1.txt")
my_input = my_file.read()
binary_lines = my_input.splitlines()
#print(binary_lines)

def edit_list(index,value,list):
    new_list = [x for x in list if x[index]==str(value)]
    return new_list

#[f(x) if condition else g(x) for x in sequence]

def binary2decimal(binary_list):
    decimal = 0
    for i in range(len(binary_list)):
        decimal += int(binary_list[i])*(2**(len(binary_list)-i-1))
    return decimal

def most_digit(index,list):
    digit_count = 0
    for line in list:
        if (line[index] == '1'):
            digit_count += 1
    if (digit_count >= len(list)/2.):
        return 1
    else:
        return 0

def least_digit(index,list):
    digit_count = 0
    for line in list:
        if (line[index] == '1'):
            digit_count += 1
    if (digit_count < len(list)/2.):
        return 1
    else:
        return 0

oxygen_list = binary_lines
CO2_list = binary_lines

index = 0
while (len(oxygen_list) > 1):
    most_value = most_digit(index,oxygen_list)
    oxygen_list = edit_list(index,most_value,oxygen_list)
    index += 1

index = 0
while (len(CO2_list) > 2):
    least_value = least_digit(index,CO2_list)
    CO2_list = edit_list(index,least_value,CO2_list)
    index += 1

print(oxygen_list)
print(CO2_list)
print(binary2decimal(oxygen_list[0]))
print(binary2decimal(CO2_list[0]))
print(binary2decimal(oxygen_list[0])*binary2decimal(CO2_list[0]))
