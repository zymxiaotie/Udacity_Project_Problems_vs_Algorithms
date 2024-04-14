def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number<0:
        return None
    return sqrt_recursive(number, 0, number)

def sqrt_recursive(number, start, end):
    # base case
    if start==end:
        return start
    # recursive case
    mid=(start+end)//2  # floor division    
    if mid*mid<=number and (mid+1)*(mid+1)>number:
        return mid
    elif mid*mid<number:
        return sqrt_recursive(number, mid+1, end)
    else:
        return sqrt_recursive(number, start, mid-1)

# Test Cases
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (3== sqrt(12)) else "Fail")
print ("Pass" if  (None== sqrt(-4)) else "Fail")