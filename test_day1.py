import day1
import pytest

@pytest.fixture
def inputDataFilePath():
    return "./test_data_day1"

@pytest.fixture
def inputDataLinesNb():
    return 4

@pytest.fixture
def combinedNumberByLine():
    return [12,38,15,77]

@pytest.fixture
def expectedSum():
    return 142

def test_get_numbers_for_each_line(inputDataFilePath, inputDataLinesNb):
    numbers = day1.getNumbersArrayFromFile(inputDataFilePath)

    assert isinstance(numbers, list)
    assert len(numbers) == inputDataLinesNb
    
    assert numbers[0][0] == 1
    assert numbers[0][1] == 2

    assert numbers[1][0] == 3
    assert numbers[1][1] == 8

    assert numbers[2][0] == 1
    assert numbers[2][1] == 5

    assert numbers[3][0] == 7
    assert numbers[3][1] == 7


def test_get_combined_number_for_each_line(inputDataFilePath,combinedNumberByLine):
    numbers = day1.getNumbersArrayFromFile(inputDataFilePath)

    combinedNumbers = day1.getDigitsFromNumberArray(numbers)

    assert len(combinedNumbers) == len(numbers)

    for index in range(len(combinedNumbers)):
        assert combinedNumbers[index] == combinedNumberByLine[index]


def test_get_sum_of_lines(inputDataFilePath, expectedSum):
    numbers = day1.getNumbersArrayFromFile(inputDataFilePath)
    combinedNumberByLine = day1.getDigitsFromNumberArray(numbers)
    sum = day1.getSum(combinedNumberByLine)

    assert sum == expectedSum
    

