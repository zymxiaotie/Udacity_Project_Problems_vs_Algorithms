Code Design: 
    This problem requires to take an integer input and generates a integer square root output with time complexity O(log n). This is a typical binary search algorithm.

    As integers include negative numbers, the function firstly checks on such situation and returns None as square root of a negative number is not a real number. 

    Next, we use binary search algorithm to find the square root of the input integer. we built a help function(sqrt_recursive) to recursively break the problem into the upper range of median and lower range of median search subproblems.  

    The sqrt_recursive function is called with three arguments: number, 0, and the number, which represent the input number for which we want to find the square root, and the start and end of the range within which we are searching for the square root.

    The sqrt function then returns the value returned by the sqrt_recursive function, which is the floored square root of number.

Efficiency: 
    The function sqrt uses a binary search algorithm (as in helper function sqrt_recursive) to find the integer square root(floor) of a given number.

    The time complexity of finding square root function is O(log n). This is because with each recursive call, the function reduces the search space by half.

    The space complexity is also O(log n) as each recursive call is added to the call stack which takes up space in memory. The maximum size of the call stack will be log n which is also the maximum depth of the binary search algorithm
