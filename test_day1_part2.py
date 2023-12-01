import day1
import pytest

@pytest.fixture
def inputDataFilePath():
    return "./test_data_day1_part2"

@pytest.fixture
def inputDataLinesNb():
    return 7

@pytest.fixture
def combinedNumberByLine():
    return [29, 83, 13, 24, 42, 14, 76]

@pytest.fixture
def expectedSum():
    return 281

@pytest.fixture
def lineWithDigits():
    return "4nineeightseven2"

@pytest.fixture
def lineWithoutDigits():
    return "nineeightseven"

@pytest.fixture
def lineWithDigitsInstead():
    return '49872'

@pytest.fixture
def arrayOfDigits():
    return [9,8,7]

def test_remove_digits(lineWithDigits, lineWithoutDigits):
    noDigitString =  day1.removeDigitFromString(lineWithDigits)

    assert noDigitString == lineWithoutDigits    

def test_get_digits_from_spelling(inputDataFilePath,inputDataLinesNb, combinedNumberByLine):
    
    lines = day1.getLinesFromFile(inputDataFilePath)

    numbers = []

    for line in lines:
        numbers.append(day1.getDigitsFromString(line))
    
    
    assert len(numbers) == inputDataLinesNb

    assert numbers[0] == [2,1,9]
    assert numbers[1] == [8,2,3]
    assert numbers[2] == [1,2,3]
    assert numbers[3] == [2,1,3,4]
    assert numbers[4] == [4,9,8,7,2]
    assert numbers[5] == [1,8,2,3,4]
    assert numbers[6] == [7,6]


def test_get_sum_of_lines(inputDataFilePath, expectedSum):
    numbers = day1.getNumbersArrayFromFile(inputDataFilePath)
    combinedNumberByLine = day1.getDigitsFromNumberArray(numbers)
    sum = day1.getSum(combinedNumberByLine)

    assert sum == expectedSum
