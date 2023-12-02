import re

def spelled_num_to_digit(digit_string):
    digit_string = digit_string.lower()
    if digit_string == 'one':
        return '1'
    elif digit_string == 'two':
        return '2'
    elif digit_string == 'three':
        return '3'
    elif digit_string == 'four':
        return '4'
    elif digit_string == 'five':
        return '5'
    elif digit_string == 'six':
        return '6'
    elif digit_string == 'seven':
        return '7'
    elif digit_string == 'eight':
        return '8'
    elif digit_string == 'nine':
        return '9'

    return digit_string

def part1(file_name):
    print('---- PART 1 ----')
    pattern = r'\d'
    try:
        with open(file_name, 'r') as calibration_doc:
            running_sum = 0
            for line in calibration_doc:
                matches = re.findall(pattern, line)
                first_num = matches[0]
                last_num = matches[-1]
                running_sum += int(first_num + last_num)
            print(f'Sum of all calibration values: {running_sum}')
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

def part2(file_name):
    print('---- PART 2 ----')
    pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'

    try:
        with open(file_name, 'r') as calibration_doc:
            running_sum = 0
            for line in calibration_doc:
                matches = re.findall(pattern, line)
                first_num = spelled_num_to_digit(matches[0])
                last_num = spelled_num_to_digit(matches[-1])
                running_sum += int(first_num + last_num)

            print(f'Sum of all calibration values: {running_sum}')
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    part1('input.txt')
    part2('input.txt')
