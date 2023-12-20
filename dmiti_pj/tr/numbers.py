import re

# s = 'Температура воздуха +12…+16°C.'

# an = re.findall(r'\d', s)
# for i in an:
#     if s.find(i)
# print(s[s.find(an[0]) -1])
# print(an)

def find_values(string):
    numbers = re.findall(r'\d+', string)
    for i in range(len(numbers)):
        if string[string.find(numbers[i]) - 1] == '-':
            numbers[i] = int(numbers[i]) * -1
        else:
            numbers[i] = int(numbers[i])
    return numbers

# print(find_values(s))

