class GameMap:


    num_positions = 100

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = (5, 5)

    def move(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.position = (x, y)
        else:
            raise ValueError("Invalid move")

     

  

