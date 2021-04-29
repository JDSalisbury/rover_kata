import random


class GridMap:
    random_items_list = []

 

    def __init__(self, x=5, y=5) -> None:
        self.x_axis = x
        self.y_axis = y
        self.grid =["x" for i in range(x*y)]


    def _coords_to_list_position(self, coords):
        in_row = self.y_axis - coords[1]
        place_in_row = in_row * self.x_axis
        return place_in_row+coords[0] -1


    def place_item_at(self,item, coords):
        position = self._coords_to_list_position(coords)
        self.grid[position] = item
        return position
        
    def get_item_at(self, coords):
        return self.grid[self._coords_to_list_position(coords)]
    



    def place_items_randomly(self, num_of_items, item):
        items_placed_at = set()
        print('')
        for i in range(num_of_items):
            rand_index = random.randrange(len(self.grid))
            if self.grid[rand_index] == 'x':
                self.grid[rand_index] = item
                items_placed_at.add(rand_index)

        self.random_items_list.append({item:list(items_placed_at)})

        return self.random_items_list



    def __str__(self) -> None:
        start = 0
        stop = self.x_axis
        print('Grid')
        for i in range(self.y_axis):
            i = i+1
            print(self.grid[start: stop])
            start = i * self.x_axis
            stop = i * self.x_axis + self.x_axis
   

        return 'test'