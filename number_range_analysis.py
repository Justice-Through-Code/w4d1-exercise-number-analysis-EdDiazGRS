#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):

    sum = 0  # to initiate variable
    for num in range(start, end +1):  # loop from the start until the end of range(must add 1)
        sum += num         # accumulator 
    return sum             #returns and stores the calculated sum
    
# calculate_sum(4,7)


"""
    Calculate the sum of numbers within the specified range.
    ehh
    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.

def find_smallest_number(start, end):

    smallest_number = start  #start is the beginning of the range and to initialize
    for num in range(start, end + 1):  #looping through the entire range inluding the last int
            if num < smallest_number:   # condition
                 smallest_number = num  

    return smallest_number

# find_smallest_number(5,56)



"""
   Find the smallest number within the specified range.
    
    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
"""
    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.

def find_largest_number(start, end):

    largest_number = start #start is the beginning of the range and to initialize 
    for num in range(start, end + 1):  #looping through the entire range inluding the last int
            if num > largest_number:   # condition
                 largest_number = num  

    return largest_number
 
# find_largest_number(4,97)
"""
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.

def count_even_numbers(start, end):

    count = 0   #initialize the accumulator
    for num in range(start, end + 1):  # loop through the entire range
         if num %2 == 0:      # check to see if it is an even number
              count += 1      # increase the count by 1
    return count          #return the count
# count_even_numbers(2,20)

"""
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.

def count_odd_numbers(start, end):

    count = 0   #initialize the accumulator
    for num in range(start, end + 1):  # loop through the entire range
         if num %2 != 0:      # check to see if it is a odd number
              count += 1      # increase the count by 1
    return count         #return the count
# count_odd_numbers(1,10)
"""
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.