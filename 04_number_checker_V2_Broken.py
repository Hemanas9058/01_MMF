# function goes here


# Checks for an integer more than 0
def int_check(question):

    error="Please enter a whole number between 12 " \
        "and 130"

    valid=False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        # if an integer is not entered, display an error        
        except ValueError:
                print(error)

# main routine goes here
age = int_check("age: ")

    # check that age is valid
    if age < 12:
        print("Sorry you are too young for this movie")
        continue
    elif age > 130:
        print("That is very old - it looks like a mistake")
        continue
