def getLinesFromFile(filePath): 
    f = open(filePath, "r")
    return f.readlines()

""" def turnCharArrayIntoIntArray(charArray):
    numbers = []
    for line in charArray:
        lineOfNumbers = []
        for char in line:
            lineOfNumbers.append(int(char))
        numbers.append(lineOfNumbers)
    
    return numbers """

def getNumbersArrayFromFile(filePath):

    numbers = []  
    lines = getLinesFromFile(filePath)

    for line in lines:
        all_numbers_in_current_line = getDigitsFromString(line)
        firstAndLastNumbers = [all_numbers_in_current_line[0], all_numbers_in_current_line[-1]]
        numbers.append(firstAndLastNumbers)
    return numbers

def getDigitsFromNumberArray(numbersArray):
    combinedNumbers = []

    for line in numbersArray:
        combinedNumbers.append(int(''.join(map(str, line))))
    
    return combinedNumbers

def getSum(combinedNumbers):
    return sum(combinedNumbers)

def removeDigitFromString(line):

    digits = [str(x) for x in range(1,10)]
    newLine = line

    for digitChar in digits:
            newLine = newLine.replace(digitChar,'')

    return newLine

""" def removeNonDigitFromString(line):

    digits = [str(x) for x in range(1,10)]

    newLine = ''

    for letter in  line:
        if(letter in digits):
            newLine += letter

    return newLine
 """
def getDigitsFromString(line):
    spelledNumbers = {'one' : 1,'two' : 2, 'three': 3 , 'four':4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}

    if len(line) == 0:
        return []
    
    digits = []

    if(line[0].isnumeric()):
        digits.append(int(line[0]))
    else:
        for spelledNumber in spelledNumbers:
            if line.startswith(spelledNumber):
                digits.append(spelledNumbers[spelledNumber])
                break

    
    line = line[1::]
        
    return digits + getDigitsFromString(line)

def resolveDay1():
    filePath = "./day1_data"
    numbers = getNumbersArrayFromFile(filePath)
    combinedNumberByLine = getDigitsFromNumberArray(numbers)
    sum = getSum(combinedNumberByLine)
    print(numbers)
    print(combinedNumberByLine)
    print(sum)

resolveDay1()