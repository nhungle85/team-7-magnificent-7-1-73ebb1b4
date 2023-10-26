class GameMap:

    default_w = 10
    default_h = 10
    num_positions = 100


    def __init__(self, width = 10, height = 10):
        self.width = width
        self.height = height
        self.position = (5, 5)

    #def get_character_position (self, x, y):
    #    self.x_position

    def validate_postion(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return True
        else:
            return False

    

     

  

