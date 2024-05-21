def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return [0, 0]
    if len(input_list) == 1:
        return [input_list[0], 0]
    if len(input_list) == 2:
        return input_list
    
    # sort the input list in descending order
    input_list = merge_sort(input_list)
    num1 = 0
    num2 = 0
    # distribute the digits of the sorted list to num1 and num2 sequentially
    for i in range(len(input_list)):
        if i % 2 == 0:
            num1 = num1 * 10 + input_list[i]
        else:
            num2 = num2 * 10 + input_list[i]
    return [num1, num2]

def merge_sort(input_list):
    """
    sort the input list using merge sort algorithm.
    Args:
         input_list(list): Input List
    Returns:
            list: sorted list
    """
    if len(input_list) <= 1:
        return input_list
    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    """
    merge two sorted lists.
    Args:
         left(list): sorted list
         right(list): sorted list
    Returns:
            list: merged list
    """
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(right[right_index])
            right_index += 1
        else:
            result.append(left[left_index])
            left_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[], [0, 0]])
test_function([[4], [4, 0]])
test_function([[4,1], [4, 1]])
test_function([[4, 3, 9], [94, 3]])