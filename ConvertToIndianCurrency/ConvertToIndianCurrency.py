''' Question 1
Write a python code for converting integer values to Indian currency notations, without 
using the currency libraries
Example:
input: 504678
output: 5,04,678 '''

def convert_to_indian_currency(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Split the number into two parts: number before the last three digits and the last three digits
    if len(num_str) > 3:
        last_three_digits = num_str[-3:]
        remaining_digits = num_str[:-3]
    else:
        return num_str
    
    # Add commas after every two digits in the remaining part
    remaining_digits = remaining_digits[::-1]
    remaining_digits_with_commas = ','.join([remaining_digits[i:i+2] for i in range(0, len(remaining_digits), 2)])
    
    # Reverse it back to the original order and concatenate with the last three digits
    indian_currency = remaining_digits_with_commas[::-1] + ',' + last_three_digits
    
    return indian_currency


input_value = int(input('Enter integer values: '))
output_value = convert_to_indian_currency(input_value)
print(output_value)
