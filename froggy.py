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
    readList()

# This will read the froggy books and add book info into an array
def readList():
    read_file = open("FroggyBooks.txt", "r")
    books = read_file.readlines()
    read_file.close()
    # print(books)
    aryBooks = []
    for book in books:
        print(book)

    
    

main()