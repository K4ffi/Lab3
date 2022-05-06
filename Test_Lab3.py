import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 10, 91, 14]
    test_arr = [10, 11, 12, 14, 22, 25, 34, 64, 90, 91]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 10, 91, 14]
    test_arr = [91, 90, 64, 34, 25, 22, 14, 12, 11, 10]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = 0
    input_arr = [6, 34, 25, 12, 22, 11, 'a']
    test_arr = 3

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_more10():
    result = 0
    input_arr = [69, 420, 34, 25, 12, 22, 11, 90, 91, 10, 76]
    test_arr = 1

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_less10():
    result = 0
    input_arr = [25, 12, 22, 11, 90]
    test_arr = 2

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_zero():
    result = 0
    input_arr = []
    test_arr = 0

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

