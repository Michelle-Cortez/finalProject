"""
    Name: Michelle Cortez
    Date: November 27th, 2018
    Assignment: Read from shirts.txt, use functions to create an array from info in  shirts file, ask the client what they want to order


"""


def main():
   getMenu()


#Read the Shirts file and place in array
def getMenu():
    getItems = open("shirts.txt", "r")
    items = getItems.readlines()
    getItems.close()
    
    menu = []
    for item in items:
        item = item.strip()
        # arypull = item.split(":")
        menu.append(item.split(":"))  
    setArray(menu)
    
#pull items into array
def setArray(arylists):
    lists = []
    lists = arylists
    for list in lists:
        listLine= f"{list[0]},{list[1]},{list[2]}\n"
        printShirts(listLine)
        


#print out a menu and ask client what they would like to order
def printShirts(orderForm):
    test = orderForm
    print(test)
    

#Output an item list and total

main()