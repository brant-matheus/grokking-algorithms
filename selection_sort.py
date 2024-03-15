#gets a unsorted list, turn into a sorted list.
import random

# Generate a list of 20 random integers between 1 up to 100.
unsorted_list = [random.randint(1, 100) for i in range(20)]


#search lowest number in list.
def search_lowest(unsorted_list):
    lowest = unsorted_list[0] #initial value.
    lowest_index = 0          #initial index.   

    for index in range(1, len(unsorted_list)): #stars at position 1.
        value = unsorted_list[index] 
        if value < lowest:
            lowest = value
            lowest_index = index
        
    return lowest_index

