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

def get_snack():
    # regular expression to find if item starts with a number

    number_regex = "^[1-9]"

    # valid snacks holds list of all snacks
    # Each item in valid snacks is a list with
    # valid options for each snack <full name, letter code (a - e)
    # , and possible abbreviations etc>
    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["Mms", "M&Ms", "M&M's", "m&m's", "mms", "m", "b"],  # first item is M&M
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "d"],
        ["orange juice", "oj", "o", "juice", "orange", "e"]
    ]

    # holds snack order for a single user
    snack_order = []

    # print("Check snack", check_snack)
    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

        # if item has a number, separate it into two (number / item)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        # remove white space around snack
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_choice = string_check(desired_snack, valid_snacks)

        # check snack amount is valid (less than 5)

        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "Invalid choice"

        # add snack AND amount to list..
        snack_row.append(amount)
        snack_row.append(snack_choice)

        # check that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "Invalid choice":
            snack_order.append(snack_row)

def string_check(choice, options):

    is_valid = ""
    chosen = ""

    for var_list in options:

        # if the snack is in one of the lists, return the full name
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

            # if choice is not OK, repeat question
    if is_valid == "yes":
        return chosen

    else:
        print("Please enter a valid option")
        print()
        return "invalid choice"

def yes_no(question):

    error = "Please answer yes / no"

    valid = False
    while not valid:

        # ask question and put response in lowercase
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
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

# valid options for yes / no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

# initialise loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# Initialise lists (to make data-frame in due course)
all_names = []
all_tickets = []

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, pita_chips, water, mms, orange_juice]

# store surcharge multiplier
surcharge_mult_list = []

# Lists to store summary data...
summary_headings = ["Popcorn", "Mms", "Pita Chips", "Water",
                    "Orange Juice", "Snack Profit", "Ticket Profit",
                    "Total Profit"]
summary_data = []

# Data Frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'Mms': mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_mult_list
}

# Summary Dictionary
summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}

# cost of each snack
price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'Mms': 3,
    'Orange Juice': 3.25
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
        # ask user if they want a snack
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snacks? ").lower()
        check_snack = string_check(want_snack, yes_no)

    # If they say yes, ask what snacks they want (and add to our snack order)
    if check_snack == "Yes":
        snack_order = get_snack()

    else:
        snack_order = []

    # Assume no snacks have been bought...
    for item in snack_lists:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount


            # ask for payment method (and apply surcharge if necessary)
        # Ask for payment method
    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash or credit)")
        how_pay = string_check(how_pay, pay_method)

    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

    surcharge_mult_list.append(surcharge_multiplier)

# End of tickets / snacks / payment loop

# print details...
# create dataframe and set index to name column
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

# create column called 'sub total'
# fill it price for snacks and ticket]

# create column called 'Sub Total'
# fill it price for snacks and ticket
movie_frame["Snacks"] = \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['Mms']*price_dict['Mms'] + \
    movie_frame['Orange Juice']*price_dict['Popcorn']

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Snacks']

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame['Surcharge']

movie_frame = movie_frame.reindex(columns=['Ticket', 'Mms', 'Orange Juice',
                                           'Pita Chips', 'Popcorn', 'Water', 'Sub Total'])

# Shorten column names
movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                                            'Pita Chips': 'Chips',
                                          'Surcharge_Multiplier': 'SM'})

# Set up summary dataframe
# populate snack items...
for item in snack_lists:
    # sum items in each snack list
    summary_data.append(sum(item))

# Get snack profit
# Get snack total from panda
snack_total = movie_frame['Snacks'].sum()
snack_profit = snack_total * 0.2
summary_data.append(snack_profit)

# Get Ticket profit and add to list
ticket_profit = ticket_sales - (5 * ticket_count)
summary_data.append(ticket_profit)

# Set up columns to be printed...
pandas.set_option('display.max_columns', None)

# Display numbers to 2 dp...
pandas.set_option('precision', 2)

print_all = input("Print all columns?? (y) for yes")
if print_all == "y":
    print(movie_frame)
else:
    print(movie_frame[['Ticket', 'Sub Total',
                       'Surcharge', 'Total']])

print()

# Tells user how many tickets are left
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets.  \n"
              "There are {} places still available"
              .format(ticket_count, MAX_TICKETS - ticket_count))

# Output data to text file