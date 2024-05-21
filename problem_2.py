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
    pivot = -1

    start = 0
    end = len(input_list) - 1    
    while start <= end:
        mid = (start + end) // 2
        # if the array is sorted
        if input_list[start] < input_list[mid] and input_list[mid] < input_list[end]:
            pivot = start
            break
        elif input_list[mid] < input_list[start]:
            if input_list[mid] < input_list[mid-1]:     
                pivot = mid
                break
            else:
                end = mid - 1
        elif input_list[mid] > input_list[end]:
            if input_list[mid] > input_list[mid + 1]:
                pivot = mid + 1
                break
            else:
                start = mid + 1
    # find the number in the rotated array
    # the array is not sorted: return -1
    if pivot == -1:
        return -1    
    # search for the number in the left side of the pivot 
    start = 0
    end = pivot 
    while start <= end:
        mid = (start + end) // 2
        if input_list[mid] == number:
            return mid
        elif input_list[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    # search for the number in the right side of the pivot 
    start = pivot 
    end = len(input_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if input_list[mid] == number:
            return mid
        elif input_list[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    # if the number is not found, return -1
    
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
test_function([[1], 10])
test_function([[1], 1])
test_function([[], 10])
