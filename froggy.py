"""
    Programmer: Michelle Cortez
    Date: November 29th 2018
    Assignment: Froggy Book Store POS, must include read and write
    
"""
""" 
    For notes while working on project:

    Need to finish read list see note above. working on for loop want to better understand

"""
# main module in charge of beginning and ending program
def main():
    quantity()

# write Customer's order to an array

#Loop to take customers order
def quantity():
    ask = input("Would you like to place an order today?(Y or N) ")
    ask = ask.lower
    choices = [" "," "," "," "]
    qtys = []
    while ask == "y":
        choice = receiveOrder()
        choices.append(choice)
        qty = input("How many would you like? ")
        qtys.append(qty)
        ask = input("would you like to order another book? (Y or N) ")
        ask = ask.lower
    print(choices, qtys)
    

# This is to show a menu and take an order
def receiveOrder():
    books = readList()
    count = 0
    # print(books)
    for book in books:
        strOrderItem = " "

        for item in book:
            strOrderItem += item + " "
        strOrderItem = str(count) + " : " + strOrderItem
        count += 1
        print(strOrderItem)
    ordered = int(input(("Which book would you like to order? select a number: ")))
    return books[ordered]
    
# This will read the froggy books and add book info into an array
def readList():
    read_file = open("FroggyBooks.txt", "r")
    items = read_file.readlines()
    read_file.close()
    # print(books)
    aryBooks = []
    for item in items:
        item = item.strip()
        aryBooks.append(item.split(','))
    return aryBooks
      


main()