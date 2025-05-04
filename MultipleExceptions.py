try:
    num1, num2, num3 = eval(input("Please Enter two numbers separated by commas: "))
    result = (num1 / num2) * num3
    print(result)

except ZeroDivisionError:
    print("Division by 0 is not possible try again!")

except SyntaxError:
    print("Comma is missing! Please enter with commas like: 1, 2")

except:
    print("No Exceptions!")

finally:
    print("I am a politician i don't care what happens i will be executed!")