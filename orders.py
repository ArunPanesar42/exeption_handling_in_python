# Dealing with files for Exception Handling in Python

# There is a built in Method in python called open("")
#file = open("orders.txt")   # looks for file called orders.txt

try:    # Keyword "try"
    file = open("orders.txt")
    print("file was found")
except FileNotFoundError as errmsg:     # We always need and except or finally for the end
    print("the above block of code was not executed ")
    print(errmsg)
    #raise
finally:
    print("Your task is to read this data and display as list")
# Second iteration
# Your task is to read this data and display as list
file = open("orders.txt")
print(file.read())

# Third iteration
def open_using_with_and_print(file):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise
    finally:
        print("\nPlease chose the items from the list  and enjoy your HAPPY MEAL")
open_using_with_and_print("orders.txt")

# add to list
def write_to_file(file, order_item):
    try:
        with open(file, "w") as file:
            file.write(order_item + '\n')
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise

write_to_file("orders.txt", "Chocolate")


