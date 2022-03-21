# import statements
import re
import pandas

# functions

# checks that ticket name is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)
        
        # If name is not blank, program continues
        if response != "":
            return response

            # If name is blank, show error (& repeat loop)
        else:
            print(error_message)

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

# Checks number of tickets left and warns user
# if maximum is being approached
def check_tickets(tickets_sold, ticket_limit):
    # tells user how many seats are left
    if ticket_count < MAX_TICKETS - 1:
        print("You have {} seats "
            "left".format(MAX_TICKETS - ticket_count))

        # warns user that only one seat is left!
    else:
        print("*** There is ONE seat left!! ***")

# Gets ticket price based on age
def get_ticket_price():

    # Get age (between 12 and 130)
    age = int_check("age: ")

    # check that age is valid
    if age < 12:
        print("Sorry you are too young for this movie")
        return "invalid ticket price"
    elif age > 130:
        print("That is very old - it looks like a mistake")
        return "invalid ticket price"

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price

# Main Routine

# set up dictionaries / lists needed to hold data

# initialise loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# Initialise lists (to make data-frame in due course)
all_names = []
all_tickets = []

# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}


# Ask user if they have used the program before & show instructions

#Loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:


    # check numbers of ticket limit has not exceeded...
    check_tickets(ticket_count, MAX_TICKETS)

    # **** Get details for each ticket... ****

    # get name (can't be blank)
    name = not_blank("Name: ",
                     "Sorry - this can't be blank, "
                     "please enter your name")

    # End the loop if the exit code is entered
    if name == "xxx":
        break

    # Get ticket price based on age
    ticket_price = get_ticket_price()
    # If age is invalid, restart loop (and get name again)
    if ticket_price == "invalid ticket price":
        continue


    ticket_count += 1
    ticket_sales += ticket_price

    # add name and ticket price to lists
    all_names.append(name)
    all_tickets.append(ticket_price)

    # Get snacks

    # ask for payment method (and apply surcharge if necessary)

# End of tickets / snacks / payment loop

# print details...
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')
print(movie_frame)
    
# Calculate Total sales and profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# Tells user how many tickets are left
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets.  \n"
              "There are {} places still available"
              .format(ticket_count, MAX_TICKETS - ticket_count))

# Output data to text file