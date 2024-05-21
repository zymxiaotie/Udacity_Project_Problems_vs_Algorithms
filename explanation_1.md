This problem requires an integer as input and aims to find its integer square root with a time complexity of O(log n). This is a typical binary search algorithm.

Fisrtly, we take consideration of some edge cases: 
- Negative numbers don't have real square roots, the function first checks for this case and returns None if the input is negative.
- The square root of zero is defined as zero. This sets the search space for the binary search to range from 1 to the input number.

There are two main approaches to implement this algorithm: recursion and iteration.

Recursive approach: Here, the space complexity is also O(log n). Each function call adds itself to the call stack, which consumes memory. The maximum depth of the call stack will be equal to the depth of the binary search, which is logarithmic in terms of the input size.

Iterative approach: This approach boasts a space complexity of O(1). The memory usage remains constant regardless of the input size. This is because the algorithm uses a fixed amount of space to store variables like start, end, and mid. These variables are overwritten in each iteration of the loop, and no additional memory allocation happens as the input size grows.

In this submission, I used the iterative approach as the space complexity is constant (predictable).