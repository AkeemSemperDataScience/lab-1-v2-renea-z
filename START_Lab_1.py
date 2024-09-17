def lab1Question1(input_gb):
    # Convert the input of a number of gigabytes to the number of bytes
    num_bytes = input_gb * 1024**3
    return num_bytes

# Testing 
input_gb = 5
calculated_bytes= 5 * 1024**3
expected_bytes = lab1Question1(input_gb)
print("Input gygabytes: ", input_gb)
print("Expected bytes: ", expected_bytes)
print("Calculated bytes: ", calculated_bytes)
if expected_bytes == calculated_bytes:
   print("Test passed")
else: 
   print("Test failed")




def lab1Question2(name):
    # Take an input of a name, return True if there is an odd number of characters in the name, False otherwise
    # Return None if the input is not a string
    is_odd = None
    if type(name) != str:
        return is_odd
    if len(name) % 2 == 1:
        is_odd = True
    else:
        is_odd = False
    return is_odd
   
# Testing different names
test_names = ['Renea','Rita', 12]
for name in test_names:
   result = lab1Question2(name)
   if result is True:
       print(f"{name}: passed because it has an odd number of characters.")
   elif result is False:
       print(f"{name}: failed because it has an even number of characters.")
   elif result is None:
       print(f"{name}: failed because it is not a string.")




def lab1Question3(input_string, input_number):
    # Take in two inputs - a string and a number
    # Return the character of the string in the index given by number.  If this index does not exist, then return -1.
    character_at = -1
    if type(input_string) != str or input_number not in range(len(input_string)):
        return character_at
    else:
        return input_string[input_number]
    
#Test case 1
input_string = "My name is Renea"
input_number = 1
outcome = lab1Question3(input_string, input_number)
print(f"\nTest case 1: Expected 'y', got {outcome}")
assert outcome == "y"

#Test case 2
input_string = 2
input_number = 1
outcome = lab1Question3(input_string, input_number)
assert outcome == -1
print(f"Test case 2: Expected -1, got {outcome}")

#Test case 3
input_string = "R"
input_number = 1
outcome = lab1Question3(input_string, input_number)
print(f"Test case 3: Expected -1, got {outcome}")
assert outcome == -1




def lab1Question4(file_name):
    # Take an input of a file name. 
    # Read that file and return a list of all numbers in that file
    list_of_nums = []
    return list_of_nums

 


def lab1Question5(list_numbers):
    # Take an input of a list of numbers
    # Return the mode from that list. 
    mode_of_list = None
    mode_count = 0
    number_count = {}
    if len(list_numbers) == 0:
        return None
    for number in list_numbers:
        if number not in number_count:
            number_count[number]= 0
        number_count[number] += 1
        if number_count[number] > mode_count:
            mode_of_list = number
            mode_count = number_count[number]
    return mode_of_list

# Test case 1
list_numbers = [1, 8, 7, 4, 5, 8, 2, 2, 1, 8]
expected_mode = 8
result = lab1Question5 (list_numbers)
print(f"From the list {list_numbers} the expected mode is: {expected_mode} and the result is: {result}")
assert lab1Question5(list_numbers) == 8




def lab1Question6(quarters, dimes, nickels, pennies):
    # Take in 4 inputs - the number of quarters, dimes, nickels, and pennies in a handful
    # Return the total amount in dollars
    # For example, if the handful contains 4 quarters, 3 dimes, 2 nickels, and 1 penny, the function should return 1.41.
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total

# Test case 1
quarters = 4
dimes = 3
nickels = 2
pennies = 1
expected_value = 1.41
result = lab1Question6(quarters, dimes, nickels, pennies)
print(f"Test case 1: Expected {expected_value}, got {result}")
assert abs(expected_value-result) < 0.001

#Test case 2
quarters = 1
dimes = 10
nickels = 3
pennies = 50
expected_value = 1.90
result = lab1Question6(quarters, dimes, nickels, pennies)
print(f"Test case 2: Expected {expected_value}, got {result}")
assert abs(expected_value-result) < 0.001
