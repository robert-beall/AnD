class min_heap:
    def __init__(self):
        self.list = []
    
    def parent_index(self, i):
        return (i - 1) // 2
    
    def left_child_index(self, i):
        return (i * 2) + 1
    
    def right_child_index(self, i):
        return (i * 2) + 2
    
    def bubble_up(self):
        if len(list) == 1:
            return 
        current_i = len(self.list) - 1
        parent_i = self.parent_index(current_i)

        while list[current_i] < list[parent_i] and current_i > 0 and parent_i >= 0:
            temp = list[parent_i]
            list[parent_i] = list[current_i]
            list[current_i] = temp
            current_i = parent_i
            parent_i = self.parent_index(current_i)
    
    def insert(self, val):
        list.append(val)
        self.bubble_up()
    
    def bubble_down(self):
        current_i = 0
        current = self.list[current_i]
        left_child = self.list[self.left_child_index(current_i)]
        right_child = self.list[self.right_child_index(current_i)]

        if len(self.list) <= 1:
            return
        while current > left_child or current > right_child:
            temp = self.list[current_i]
            smallest_i = self.left_child_index(current_i) if left_child < right_child else self.right_child_index(current_i)
            self.list[current_i] = self.list[smallest_i]
            self.list[smallest_i] = temp

            current_i = smallest_i
            left_child = self.left_child_index(current_i)
            right_child = self.right_child_index(current_i)



    
    def remove(self):
        top = self.list[0] # get the root
        bottom = self.list.pop() # remove the last leaf

        self.list[0] = bottom # put the last leaf in the root

        return top
            