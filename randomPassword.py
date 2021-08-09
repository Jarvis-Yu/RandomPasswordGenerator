import sys
from random import randint

class SymbolSet:
    
    def __init__(self, string: str, weight: int) -> None:
        self.__str = string
        self.__weight = weight

    def getWeight(self) -> int:
        return self.__weight

    def getChar(self) -> str:
        index = randint(0, len(self.__str) - 1)
        return self.__str[index]

def argOfCorrectFormat(arg: str) -> bool:  # of syntax "-*"

    if len(arg) == 0:
        return False
    if arg[0] == "-":
        return True
    return False

def main() -> int:

    if len(sys.argv) <= 1:
        return 0

    passwordLen = int(sys.argv[1])
    if passwordLen <= 0:
        return 0

    lowerCases = SymbolSet(
            "abcdefghijklmnopqrstuvwxyz", 
            260)
    upperCases = SymbolSet(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 
            260)
    numbers = SymbolSet(
            "1234567890", 
            400)
    symbols = SymbolSet(
            "~`! @#$%^&*()_-+={[}]|\:;\"'<,>.?/", 
            200)

    password = ""
    listOfSymbols = []

    if len(sys.argv) <= 2:
        listOfSymbols = [lowerCases, upperCases, numbers, symbols]
    else:
        for arg in sys.argv[2:]:
            if argOfCorrectFormat(arg):
                arg_sub = arg[1:]
                if arg_sub == "lc":
                    listOfSymbols.append(lowerCases)
                elif arg_sub == "uc":
                    listOfSymbols.append(upperCases)
                elif arg_sub == "n":
                    listOfSymbols.append(numbers)
                elif arg_sub == "s":
                    listOfSymbols.append(symbols)
                else:  # invalid arg
                    print("Invalid Argument Error: only -lc -uc -n -s are allowed")

    totalWeight = sum([i.getWeight() for i in listOfSymbols])

    for i in range(passwordLen):

        randomNumber = randint(0, totalWeight - 1)

        for symbolSet in listOfSymbols:
            if symbolSet.getWeight() <= randomNumber:
                randomNumber -= symbolSet.getWeight()
            else:
                password += symbolSet.getChar()
                break

    print(password)
    return 0

if __name__ == "__main__":
    main()
