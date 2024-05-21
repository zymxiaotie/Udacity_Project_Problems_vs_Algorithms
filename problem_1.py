def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # a negative number does not have a square root
    if number<0:
        return None 
    # 0 is the square root of 0
    if number==0:
        return 0
    # binary search to find the square root
    start=1
    end=number
    while start<=end:
        mid=(start+end)//2
        if mid*mid<=number and (mid+1)*(mid+1)>number:
            return mid
        elif mid*mid<number:
            start=mid+1
        else:
            end=mid-1

# Test Cases
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (3== sqrt(12)) else "Fail")
print ("Pass" if  (None== sqrt(-4)) else "Fail")