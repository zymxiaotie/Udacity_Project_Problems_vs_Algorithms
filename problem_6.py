def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    min = ints[0]
    max = ints[0]

    for i in ints:
        if i < min:
            min = i
        if i > max:
            max = i

    return (min, max)

### Example Test Case of Ten Integers
import random
# Test case with all positive integers
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# Test case with an empty list
print ("Pass" if (None == get_min_max([])) else "Fail")
# Test case with a list containing a single integer of 0
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
print ("Pass" if ((0, 0) == get_min_max([0, 0, 0])) else "Fail")
# Test case with a large list of integers
large_list = [i for i in range(-1000000, 1000001)]
random.shuffle(large_list)
print("Pass" if ((-1000000, 1000000) == get_min_max(large_list)) else "Fail") # Test case with negative integers
# Test case with a list of all negative integers
print("Pass" if ((-10, -1) == get_min_max([-5, -10, -3, -1, -7])) else "Fail")
# Test case with a single positive integer
print("Pass" if ((1, 1) == get_min_max([1])) else "Fail")
# Test case with a single negative integer
print("Pass" if ((-1, -1) == get_min_max([-1])) else "Fail")