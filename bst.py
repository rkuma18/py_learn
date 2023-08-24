#Function that implements a binary search tree
#Author: Roushan Kumar
#Date: 08/24/2023
#Version: 1.0
#---------------------------------------------
def binary_search_tree(lst, item):
    """Function that implements a binary search tree
    Args:
        lst: list of elements
        item: item to be searched
    Returns:
        True if item is found, False otherwise
    """
    if len(lst) == 0: #base case
        return False
    else:
        mid = len(lst) // 2 #find the middle element
        if lst[mid] == item:
            return True #base case
        else:
            return binary_search_tree(lst[:mid], item) or binary_search_tree(lst[mid + 1:], item) #recursive call
        
print(binary_search_tree([1,2,3,4,5,6,7,8,9,10], 5))
print(binary_search_tree([1,2,3,4,5,6,7,8,9,10], 11))
print(binary_search_tree([1,2,3,4,5,6,7,8,9,10], 0))
print(binary_search_tree([1,2,3,4,5,6,7,8,9,10], 1))
print(binary_search_tree([1,2,3,4,5,6,7,8,9,10], 10))
print(binary_search_tree([1,2,3,4,5,6,7,8,9,10], 6))
print(binary_search_tree([1,2,3,4,5,6,7,8,9,10], 7))
print(binary_search_tree([1,2,3,4,5,6,7,8,9,10], 8))
print(binary_search_tree([1,2,3,4,5,6,7,8,9,10], 9))
print(binary_search_tree([1,2,3,4,5,6,7,8,9,10], 2))
print(binary_search_tree([1,2,3,4,5,6,7,8,9,10], 3))
print(binary_search_tree([1,2,3,4,5,6,7,8,9,10], 4))

