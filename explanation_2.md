This problem requires to find a number in a rotated sorted array with time complexity of O(log n). Finding a number in a sorted array is a with a complexity of O(logn) is a typical binary search problem. The challenge arises when the array is rotated at an unknown number of times. We can divide the problem into two sub-problems: finding the number in two sorted sub-arrays.

The key idea lies in identifying the "pivot" element, which is the smallest element in the rotated array. This pivot effectively separates the original sorted array into two sorted sub-arrays. Once we find the pivot using binary search (which itself takes O(log n) time), the problem reduces to finding the number in two separate sorted sub-arrays.

Binary search can then be applied to each sub-array independently. Since the original array of size n is split into sub-arrays of size a and b (where a + b = n), the time complexity for each binary search operation becomes O(log a) and O(log b) respectively. As both a and b are smaller than n, this sum remains O(log n).

Similar to problem 1, the space complexity here remains O(1). The algorithm utilizes variables like start, end, mid, and pivot, whose memory usage is independent of the input size.

In total, the time complexity is O(logn) while space complexity is O(1)