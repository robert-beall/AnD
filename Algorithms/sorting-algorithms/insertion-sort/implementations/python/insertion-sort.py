def insertion_sort(list):

    for i in range(1, len(list)):
        j = i - 1
        key = list[i]
        
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list

list = [2, 15, 6, 7, 90, 1, 0]

print (insertion_sort(list))

