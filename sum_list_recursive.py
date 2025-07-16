 #Write a recursive function sum_list(lst) that returns the sum of all elements in a list. For example, sum_list([1, 2, 3]) returns 6.
def sum_list(lst):
    if not lst:
        return 0  # base case: empty list has sum 0
    return lst[0] + sum_list(lst[1:])  # first element + sum of rest of list

# Example usage:
print(sum_list([1, 2, 3]))  # Output: 
6
