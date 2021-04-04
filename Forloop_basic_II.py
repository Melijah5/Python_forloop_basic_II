# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# # Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]


def biggest_size(list):
    new_list =[]
    for i in range (len(list)):
        if list[i]>0:
            list[i]='big'
    new_list.append(i)
    return new_list
print(biggest_size([5,2,-3,8,-8,2]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positive(list):
    count = 0
    for i in range(len(list)):
        if list[i]>0:
            count = count + 1
        list[len(list)-1] = count
    return list
print(count_positive([2,4,-5,-47,5,-2]))


# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(list):
    sum = 0
    for i in range(len(list)):
        sum = sum +list[i]
    return sum
print(sum_total([2,5,-5,8,1]))


# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def average(list):
    sum=0
    avg=0
    for i in range(len(list)):
        sum = sum + list[i]
        avg = sum / len(list)
    return avg

print(average ([5,2,-5,8,9,6]))


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length (list):
      for i in range(len(list)):
        return len(list)
    
print(length([2,2,24,4,5]))


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def min(list):
    if len(list)<0:
        return false
    min= list[0]  
    for i in range(0, len(list)-1):
        for j in range(1, len(list)):
            if list[j]< list[i]:
              min = list[j]
    return min

print(min([4,5,2,1,9]))



# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def max(list):
    if len(list)<0:
        return false
    max= list[0]  
    for i in range(0, len(list)-1):
        for j in range(1, len(list)):
            if list[j]> list[i]:
              max = list[j]
    return max

print(max([4,5,2,1,9]))




# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }


def Ultimate_Analysis(list):
    new_dict = {'sumTotal': 0, 'average': 0, 'minimum': list[0], 'maximum': list[0], 'length': len(list) }

    for i in range(len(list)):
    
        if new_dict['minimum']>list[i]:
            new_dict['minimum'] = list[i]
        if new_dict['maximum']<list[i]:
          new_dict['maximum'] = list[i]
        new_dict['sumTotal'] = new_dict['sumTotal'] + list[i]
        new_dict['average'] =new_dict['sumTotal'] /len(list)
    return new_dict

print(Ultimate_Analysis([8,5,4,9,2,0,4]))




# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(list):
    end = len(list)-1
    mid = int(end/2)+1
    
    for i in range(mid):
        list[i],list[end] = list[end],list[i]
        end = end -1
        
    return list

print(reverse_list([5,3,2,4]))

    
    


# with another list

def reverse_list(list):
    new_list = []
    reverse_index = len(list) - 1
    for index in range(len(list)):
        new_list.append(list[reverse_index - index])
    return new_list
    
print(reverse_list([5,3,2,4]))