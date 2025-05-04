Value = False

while not Value:
    try:
        number = int(input("Please Enter A Number (If you wanna blow up your PC): "))
        while number%2 == 0:
            print("Welcome To Hell! You Died because your laptop Exploded!")
        Value = True
    except ValueError:
        print("Invalid Input!")