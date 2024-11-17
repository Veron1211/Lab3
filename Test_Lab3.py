import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == test_arr)

def test_bubble_sort_descending():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert (result == test_arr)

def test_bubble_sort_10_number():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 23, 5, 4]

    result = Lab3.bubble_sort(input_arr, any)
    assert (result == 1)

def test_bubble_sort_0_number():
    input_arr = []

    result = Lab3.bubble_sort(input_arr, any)
    assert (result == 0)

def test_bubble_sort_not_number():
    input_arr = ["veron", "ngbee"]

    result = Lab3.bubble_sort(input_arr, any)
    assert (result == 2)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])