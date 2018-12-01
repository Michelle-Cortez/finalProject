def main():

    shirtOrdered = menu()
    # print(shirtOrdered)
    processOrder(shirtOrdered)

def processOrder(whatShallIProcess):
    print(whatShallIProcess)
 
def menu():

    shirts = readTheData()
    cntr = 0
    for shirt in shirts:
        strmenuItem = ""
        
        for item in shirt:
            strmenuItem += item + " "
        strmenuItem = str(cntr) + " - " + strmenuItem
        cntr += 1
        print(strmenuItem)
    ordered = int(input("Which would you like?"))
    # print(ordered)
    # print (shirts[ordered])
    return shirts[ordered]
   

   


def readTheData():

    read_file = open("shirts.txt", "r")
    lines = read_file.readlines()
    read_file.close()

    aryShirts = []
    for line in lines:
        line = line.strip()
        aryShirts.append(line.split(','))

    return aryShirts

main()