def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1
    if len(input_list) == 1:
        return 0 if input_list[0] == number else -1
    
    # find the index of the minimum element in the rotated array
    pivot = find_start_of_arr(input_list)   
    
    # if the input array is not sorted
    if pivot == -1:
        return -1
    
    if input_list[pivot] == number:
        return pivot
    
    # sorted array on the left side of pivot
    if input_list[0] <= number and input_list[pivot-1] >= number:
        return binary_search(input_list[:pivot], number)
    elif input_list[pivot] <= number and input_list[-1] >= number:
        return pivot + binary_search(input_list[:pivot], number)
    else:
        return -1
  

def find_start_of_arr(input_list):
    """
    Find the index of the minimum element of a sorted array after rotation.
    Args:
       input_list(array): The rotated input array to search
    Returns:
       int: Index of the minimum element
    """
    start = 0
    end = len(input_list) - 1
    
    while start < end:
        mid = (start + end) // 2
        if input_list[start] < input_list[mid] and input_list[mid] < input_list[end]:
            return start
        elif input_list[mid] < input_list[start]:
            if input_list[mid] < input_list[mid-1]:     
                return mid
            else:
                end = mid - 1
        elif input_list[mid] > input_list[end]:
            if input_list[mid] > input_list[mid + 1]:
                return mid + 1
            else:
                start = mid + 1
    if start == end:
        return start
    return -1 # if the input array is not sorted


def binary_search(input_list, number):
    """
    Find the index of a number in a sorted array using binary search.
    Args:
       input_list(array): Input array to search 
       number(int): The target number to search
    Returns:
       int: Index of the number or -1 if not found
    """
    start = 0
    end = len(input_list) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if input_list[mid] == number:
            return mid
        if input_list[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
