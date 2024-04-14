This problem involves finding a number in a sorted array that has been rotated, with a time complexity of O(log n).

Finding a number in a sorted array is straightforward. Therefore, it's beneficial to create a function (find_start_of_arr) that identifies the smallest point in the rotated array. This smallest point represents the starting point of the array before it was rotated.

We employ a binary search to locate the smallest point in the rotated array, which takes O(log n) time. Consequently, we can divide the problem into two smaller tasks: finding the number in the two sorted subarrays.

We can then use binary search to find a number in a sorted array, which also takes O(log n) time. Due to the recursive nature of binary search algorithms, the maximum depth of the binary tree is O(log n). Therefore, the space complexity is also O(log n) to accommodate the recursive calls in memory.

In conclusion, both the time complexity and space complexity of this problem are O(log n)