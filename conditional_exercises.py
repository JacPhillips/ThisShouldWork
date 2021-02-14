my_pin = "1111"
number_of_attempts = 0

supplied_pin = input("Enter your PIN: \n")
number_of_attempts += 1
if supplied_pin == my_pin:
    print("PIN is correct")

else:
    number_of_attempts += 1
    supplied_pin = input("Incorrect PIN, try again \n")
    if supplied_pin == my_pin:
        print("PIN is correct")
    else:
        number_of_attempts += 1
        supplied_pin = input("Incorrect PIN, try again \n")
        if supplied_pin == my_pin:
            print("PIN is correct")
        else:
            print("Incorrect you are locked out")

print("Number of attempts: ", number_of_attempts)

# import getpass

# my_pin = "1111"
# number_of_attempts = 0

# supplied_pin = getpass.getpass(prompt= "Enter your PIN :\n")
# number_of_attempts += 1
# if supplied_pin == my_pin:
#     print("PIN is correct")

# else:
#     number_of_attempts += 1
#     supplied_pin = getpass.getpass(prompt= "Enter your PIN :\n")
#     if supplied_pin == my_pin:
#         print("PIN is correct")
#     else:
#         number_of_attempts += 1
#         supplied_pin = getpass.getpass(prompt= "Enter your PIN :\n")
#         if supplied_pin == my_pin:
#             print("PIN is correct")
#         else:
#             print("Incorrect you are locked out")

# print("Number of attempts: ", number_of_attempts)
















