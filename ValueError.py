try:
    x = int(input("Please Enter A Number: "))
    print(f"The Number Entered is: {x}")
except ValueError as ex:
    print("Exception:" , ex)