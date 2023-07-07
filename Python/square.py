# Importing function from other function file

# import specific function name
# from function import square

# import the entire funtion
import function

for i in range(10):
    # print(f"The square of {i} is {square(i)}") // If used to import specific funtion name
    print(f"The square of {i} is {function.square(i)}")