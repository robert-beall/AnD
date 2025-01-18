def bubble_sort(list):
    swap = False

    for i in range(0, len(list) - 1):
        if list[i] > list[i + 1]:
            temp = list[i+1]
            list[i + 1] = list[i]
            list[i] = temp
            swap = True

    if swap == True:
        return bubble_sort(list)
    else: 
        return list

list = [2, 15, 6, 7, 90, 1, 0]

print (bubble_sort(list))

