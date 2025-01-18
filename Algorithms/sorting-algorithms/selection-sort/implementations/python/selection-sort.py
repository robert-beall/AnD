def selection_sort(list):
    for i in range (0, len(list)):
        smallest = list[i]
        swap_index = i
        for j in range (i, len(list)):
            if list[j] < smallest:
                smallest = list[j]
                swap_index = j
        temp = list[i]
        list[i] = list[swap_index]
        list[swap_index] = temp
    return list

list = [2, 15, 6, 7, 90, 1, 0]

print (selection_sort(list))