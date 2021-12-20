
my_file = open("Day3input1.txt")
my_input = my_file.read()
binary_lines = my_input.splitlines()
#print(binary_lines)
digit_count = [0,0,0,0,0,0,0,0,0,0,0,0]

def binary2decimal(binary_list):
    decimal = 0
    for i in range(len(binary_list)):
        decimal += int(binary_list[i])*(2**(len(binary_list)-i-1))
    return decimal

for line in binary_lines:
    for i in range(len(line)):
        if (line[i] == '1'):
            digit_count[i] += 1
print(len(binary_lines))
gamma_rate = [1 if x > len(binary_lines)/2 else 0 for x in digit_count]
epsilon_rate = [1 if x < len(binary_lines)/2 else 0 for x in digit_count]
gamma_number = binary2decimal(gamma_rate)
epsilon_number = binary2decimal(epsilon_rate)
print(gamma_rate)
print(epsilon_rate)
print(gamma_number)
print(epsilon_number)
print(gamma_number*epsilon_number)

#[f(x) if condition else g(x) for x in sequence]