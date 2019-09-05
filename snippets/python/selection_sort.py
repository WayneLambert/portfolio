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


if __name__ == '__main__':
    random_array = [49, 81, 1, 9, 36, 64, 81, 100, 4, 16, 25]

    sorted_list = selection_sort(random_array)
    print(f'The sorted list is {sorted_list}')
