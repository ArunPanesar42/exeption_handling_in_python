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
def read_file(filename):
    try:
        file = open(filename)
        print("File has been opened")
    except FileNotFoundError as errormsg:
        print(f"File not found, error code is:  {errormsg}")
    finally:
        print(filename)
        print(file.read())


read_file("orders.txt")

