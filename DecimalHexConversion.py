def decimalToHex():
    print("Enter an int number in base 10: ")
    x = int(input())
    xDu = x
    l = []
    i = 0
    total = ""

    while x >= 16:
        l.append(x % 16)
        x = x // 16

    l.append(x)
    l.reverse()
    for i in range(len(l)):
        total += hexToDeciDict[l[i]]

    print("decimal numebr {} in hex is: {}. ".format(xDu, total))
    return total

hexToDeciDict = "0123456789ABCDEF"



def HexToDecimal():
    print("Enter an int number base 16: ")
    x = input()
    xDu = x     # create a duplicate of x
    l = []  # store each digit(string representation) of x
    i = 0
    total = 0
    k = 0

    while len(x) >= 1:
        l.append(x[0])
        x = x[1:]


    while k < len(l):
        total += hexToDeciDict.index(l[k]) * 16 ** (len(l) - k - 1)
        k += 1

    print("hex num {} in decimal is {}. ".format(xDu, total))
    return total


if __name__ == "__main__":
    while True:
        print("=========================================================================")
        print()
        print()
        print("Do you wanna convert decial to hex[type1] or hex to ddecial[type2]?")
        x1 = input(("Please type [1] or [2]. "))
        if x1 == "1":
            print("You are now converting decimal to hex!")
            decimalToHex()
        else:
            print("You are now converting hex to decimal!")
            HexToDecimal()
        print("Do you wanna using our conversion service again?")
        x2 = input(("Please type [yes] or [no]. "))
        if x2 == "yes":
            print()
            print()
            print("=========================================================================")
        else:
            print()
            print()
            print("=========================================================================")
            print("Thanks for using our service!")
            break;