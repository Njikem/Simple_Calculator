#function to add two numbers

def add_num1(x, y):
    return("x+y")
    
#function to subtract two numbers

def subtract_num2(x, y):
    return("x-y")

#function to multiply two numbers

def multiply_num3(x, y):
    return("x*y")


#function to divide two numbers

def divide_num4(x, y):
    return("x/y")

#Taking input for user choice
user_choice = ("User Should enter their choice(1, 2, 3, 4)")


#User input number
numb_one = float(input("Enter your number:"))
op = input("Enter operator:")
numb_two = float(input("Enter your number again:"))

result = (numb_one) + (numb_two)
result = (numb_one) - (numb_two)
result = (numb_one) * (numb_two)
result = (numb_one) / (numb_two)

