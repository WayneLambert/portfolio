# Selection sort algorithm
""" The code is purposefully not written using Pythonic idioms """

def selection_sort(array):
    for i in range(0, len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


random_array = [13, 25, 26, 17, 48, 78, 34, 78, 12, 56, 89, 45]

sorted_list = selection_sort(random_array)
print(f'The sorted list is {sorted_list}')
