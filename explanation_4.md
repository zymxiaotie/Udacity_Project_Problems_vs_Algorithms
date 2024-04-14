This problem involves sorting three digits (0, 1, 2) in ascending order by traversing the input array once.

We use three pointers (low, mid, high) to track the front indices of these three digits. The 'low' pointer is the front index of digit 0, starting at the beginning of the array and moving forward. The 'high' pointer is the front index of digit 2, starting from the end of the array and moving backward. The 'mid' pointer traverses the input array from the start, moving forward. When we encounter an element, if it's 0, we move 'low' and 'mid' one index forward. If it's 2, we move 'high' one index backward. If it's 1, we only move 'mid' one index forward to continue the traversing.

By traversing once, we place all 0s at the beginning of the array and all 2s at the end, leaving all 1s in the middle of the array.

The time complexity is O(n) in the worst case, as we traverse the array once. The space complexity is O(1) as we swap elements within the same array.