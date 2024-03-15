# MUST BE a sorted list.
# 0(log n) worst case. log base 2 of n.

size_list = (1*(10**2))+1
sorted_list = [i for i in range(1, size_list)] #generating a list from 1 up to size_list.


def binary_search(sorted_list, item):
    #postion variables.
    low = 0
    high = len(sorted_list)-1

    while (low<=high): 
        mid = (low + high) // 2 #position.
        guess = sorted_list[mid] #actual item.

        if guess == item:
            return mid #retuns it's position in sorted list.
        
        elif guess < item: #eliminates mid and what came before.
            low = mid + 1

        else: #guess > item # eliminates mid nad what comes after.
            high = mid - 1
    
    return None #item not in list.
item = 12
print(binary_search(sorted_list, item))
